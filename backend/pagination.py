"""
Opt-in list pagination for APIView endpoints.

Without ``page`` / ``page_size`` query params, responses stay bare arrays
(backward compatible). With either param, responses use a DRF-style envelope:

  { count, next, previous, page, page_size, total_pages, results }
"""

from __future__ import annotations

from math import ceil
from typing import Any, Optional
from urllib.parse import urlencode

from rest_framework.request import Request
from rest_framework.response import Response

DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100


def wants_pagination(request: Request) -> bool:
    return "page" in request.query_params or "page_size" in request.query_params


def parse_page_params(request: Request) -> tuple[int, int]:
    try:
        page = int(request.query_params.get("page") or 1)
    except (TypeError, ValueError):
        page = 1
    try:
        page_size = int(request.query_params.get("page_size") or DEFAULT_PAGE_SIZE)
    except (TypeError, ValueError):
        page_size = DEFAULT_PAGE_SIZE

    page = max(1, page)
    page_size = max(1, min(page_size, MAX_PAGE_SIZE))
    return page, page_size


def _replace_query(request: Request, **updates: Any) -> Optional[str]:
    """Build URL with updated query params; drop keys set to None."""
    params = request.query_params.copy()
    for key, value in updates.items():
        if value is None:
            params.pop(key, None)
        else:
            params[key] = str(value)
    query = urlencode(sorted(params.items()), doseq=True)
    try:
        base = request.build_absolute_uri(request.path)
    except Exception:
        base = request.path or "/"
    return f"{base}?{query}" if query else base


def paginate_list(
    request: Request,
    queryset,
    serializer_class,
    *,
    context: Optional[dict] = None,
) -> Response:
    """
    Serialize ``queryset`` as a bare array, or as a paginated envelope when
    ``page`` / ``page_size`` are present.
    """
    ctx = context or {}
    if not wants_pagination(request):
        serializer = serializer_class(queryset, many=True, context=ctx)
        return Response(serializer.data)

    page, page_size = parse_page_params(request)
    total = queryset.count()
    total_pages = ceil(total / page_size) if page_size and total else 0
    if total_pages and page > total_pages:
        page = total_pages

    start = (page - 1) * page_size
    end = start + page_size
    page_qs = queryset[start:end]
    serializer = serializer_class(page_qs, many=True, context=ctx)

    next_url = (
        _replace_query(request, page=page + 1, page_size=page_size)
        if page < total_pages
        else None
    )
    previous_url = (
        _replace_query(request, page=page - 1, page_size=page_size)
        if page > 1
        else None
    )

    return Response(
        {
            "count": total,
            "next": next_url,
            "previous": previous_url,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "results": serializer.data,
        }
    )
