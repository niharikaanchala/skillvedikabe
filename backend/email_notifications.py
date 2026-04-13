import json
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, Optional

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import escape


def _normalize_recipients(raw: Optional[Iterable[str]]) -> list[str]:
    if not raw:
        return []
    return [str(x).strip() for x in raw if str(x).strip()]


def _value_to_text(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False, indent=2, default=str)
    return str(v)


def send_admin_submission_email(*, title: str, data: Dict[str, Any]) -> None:
    """
    Sends a formal HTML + plain-text email to ADMIN_NOTIFICATION_EMAILS.
    Never raises (safe to call in API handlers).
    """
    try:
        recipients = _normalize_recipients(getattr(settings, "ADMIN_NOTIFICATION_EMAILS", []))
        if not recipients:
            return

        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None) or None
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        # Plain text fallback
        text_payload = json.dumps(data, ensure_ascii=False, indent=2, default=str)
        text_body = (
            f"{title}\n"
            f"Received at: {now}\n\n"
            f"Saved data:\n{text_payload}\n"
        )

        # HTML body (corporate style)
        rows_html = []
        for k in sorted(data.keys(), key=lambda x: str(x).lower()):
            key = escape(str(k))
            val = escape(_value_to_text(data.get(k)))
            rows_html.append(
                "<tr>"
                f"<td style=\"padding:10px 12px;border-top:1px solid #e5e7eb;"
                f"font:600 13px/18px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;"
                f"color:#111827;vertical-align:top;width:220px;\">{key}</td>"
                f"<td style=\"padding:10px 12px;border-top:1px solid #e5e7eb;"
                f"font:13px/18px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;"
                f"color:#111827;white-space:pre-wrap;\">{val}</td>"
                "</tr>"
            )
        table_html = (
            "<table role=\"presentation\" cellspacing=\"0\" cellpadding=\"0\""
            " style=\"width:100%;border-collapse:collapse;border:1px solid #e5e7eb;"
            "border-radius:10px;overflow:hidden;background:#ffffff;\">"
            "<tr>"
            "<td colspan=\"2\" style=\"padding:14px 16px;background:#111827;"
            "color:#ffffff;font:700 14px/18px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;\">"
            "Submission details"
            "</td>"
            "</tr>"
            + "".join(rows_html)
            + "</table>"
        )

        html_body = f"""
<!doctype html>
<html>
  <body style="margin:0;background:#f3f4f6;padding:24px;">
    <div style="max-width:720px;margin:0 auto;">
      <div style="background:#ffffff;border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;">
        <div style="padding:18px 20px;background:#0b1220;">
          <div style="font:800 18px/22px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;color:#ffffff;">
            {escape(title)}
          </div>
          <div style="margin-top:6px;font:13px/18px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;color:#cbd5e1;">
            Received at: {escape(now)}
          </div>
        </div>
        <div style="padding:18px 20px;">
          <div style="font:14px/20px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;color:#111827;margin:0 0 14px 0;">
            A new submission has been received. The saved record is included below.
          </div>
          {table_html}
          <div style="margin-top:16px;font:12px/18px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial;color:#6b7280;">
            This is an automated notification. Please do not reply to this email.
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
""".strip()

        msg = EmailMultiAlternatives(
            subject=title,
            body=text_body,
            from_email=from_email,
            to=recipients,
        )
        msg.attach_alternative(html_body, "text/html")
        msg.send(fail_silently=True)
    except Exception:
        return
