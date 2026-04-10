# courses/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from courses.models import Course as CourseModel

# -----------------------------
# Courses CRUD
# -----------------------------
class CourseDetailView(APIView):
    def get(self, request, slug):
        print("slug :", slug)
        try:
            course = CourseModel.objects.get(slug=slug)
        except CourseModel.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, slug):
        try:
            course = CourseModel.objects.get(slug=slug)
        except CourseModel.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
# class CourseDetailView(APIView):
#     def get_object(self, slug):
#         try:
#             return Course.objects.get(slug=slug)
#         except Course.DoesNotExist:
#             return None

#     def get(self, request, slug):
#         course = self.get_object(slug)
#         if not course:
#             return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         course = self.get_object(slug)
#         if not course:
#             return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseSerializer(course, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         course = self.get_object(slug)
#         if not course:
#             return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
#         course.delete()
#         return Response({"message": "Course deleted"}, status=status.HTTP_204_NO_CONTENT)


# -----------------------------
# Generic CRUD for Sections
# -----------------------------
def create_section_crud(class_name, model, serializer):
    class SectionView(APIView):

        def get_object(self, pk):
            try:
                return model.objects.get(pk=pk)
            except model.DoesNotExist:
                return None

        # ✅ GET (by course slug) or single row by id
        def get(self, request, *args, **kwargs):
            pk = kwargs.get("pk")
            if pk is not None:
                obj = self.get_object(pk)
                if not obj:
                    return Response({"error": f"{class_name} not found"}, status=404)
                return Response(serializer(obj).data)

            slug = kwargs.get("slug")

            try:
                course = CourseModel.objects.get(slug=slug)
            except CourseModel.DoesNotExist:
                return Response({"error": "Course not found"}, status=404)

            objects = model.objects.filter(course=course)
            serializer_obj = serializer(objects, many=True)
            return Response(serializer_obj.data)

        # ✅ POST (attach using slug)
        def post(self, request, *args, **kwargs):
            slug = kwargs.get("slug")

            try:
                course = CourseModel.objects.get(slug=slug)
            except CourseModel.DoesNotExist:
                return Response({"error": "Course not found"}, status=404)

            serializer_obj = serializer(data=request.data)

            if serializer_obj.is_valid():
                serializer_obj.save(course=course)
                return Response(serializer_obj.data, status=status.HTTP_201_CREATED)

            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

        # ✅ PUT
        def put(self, request, *args, **kwargs):
            pk = kwargs.get("pk")
            obj = self.get_object(pk)
            if not obj:
                return Response({"error": f"{class_name} not found"}, status=404)

            serializer_obj = serializer(obj, data=request.data, partial=True)
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data)

            return Response(serializer_obj.errors, status=400)

        # ✅ DELETE
        def delete(self, request, *args, **kwargs):
            pk = kwargs.get("pk")
            obj = self.get_object(pk)
            if not obj:
                return Response({"error": f"{class_name} not found"}, status=404)

            obj.delete()
            return Response({"message": f"{class_name} deleted"}, status=204)

    return SectionView
    
# -----------------------------
# Section CRUD Classes
# -----------------------------
SkillView = create_section_crud("Skill", Skill, SkillSerializer)
ToolView = create_section_crud("Tool", Tool, ToolSerializer)
CurriculumView = create_section_crud("Curriculum", Curriculum, CurriculumSerializer)
ProjectView = create_section_crud("Project", Project, ProjectSerializer)
SalaryView = create_section_crud("Salary", Salary, SalarySerializer)
FAQView = create_section_crud("FAQ", FAQ, FAQSerializer)
BatchView = create_section_crud("Batch", Batch, BatchSerializer)
BlogView = create_section_crud("Blog", Blog, BlogSerializer)
TrainerView = create_section_crud("Trainer", Trainer, TrainerSerializer)
AboutView = create_section_crud("About", About, AboutSerializer)
PlacementSupportView = create_section_crud("PlacementSupport", PlacementSupport, PlacementSupportSerializer)
CorporateTrainingView = create_section_crud("CorporateTraining", CorporateTraining, CorporateTrainingSerializer)


class CourseSectionMetaView(APIView):
    def get(self, request, slug):
        try:
            course = CourseModel.objects.get(slug=slug)
        except CourseModel.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)

        obj, _ = CourseSectionMeta.objects.get_or_create(course=course)
        return Response(CourseSectionMetaSerializer(obj).data)

    def put(self, request, slug):
        try:
            course = CourseModel.objects.get(slug=slug)
        except CourseModel.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)

        obj, _ = CourseSectionMeta.objects.get_or_create(course=course)
        serializer = CourseSectionMetaSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)