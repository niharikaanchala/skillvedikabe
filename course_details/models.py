# courses/models.py
from django.db import models
from courses.models import Course

# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)
#     description = models.TextField()
#     duration = models.CharField(max_length=50)
#     price = models.CharField(max_length=20)
#     rating = models.FloatField(default=0)

#     def __str__(self):
#         return self.title

# -----------------------------
# Sections as separate models
# -----------------------------
class Skill(models.Model):
    course = models.ForeignKey(Course, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name

class Tool(models.Model):
    course = models.ForeignKey(Course, related_name='tools', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Curriculum(models.Model):
    course = models.ForeignKey(Course, related_name='curriculum', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    course = models.ForeignKey(Course, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Salary(models.Model):
    course = models.ForeignKey(Course, related_name='salaries', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    range = models.CharField(max_length=50)

    def __str__(self):
        return self.role

class FAQ(models.Model):
    course = models.ForeignKey(Course, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Batch(models.Model):
    course = models.ForeignKey(Course, related_name='batches', on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    seats = models.CharField(max_length=50)
    limited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.title} - {self.date}"

class Blog(models.Model):
    course = models.ForeignKey(Course, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

class Trainer(models.Model):
    course = models.ForeignKey(Course, related_name='trainers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    exp = models.CharField(max_length=50, blank=True)
    skills = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


# -----------------------------
# Additional sections
# -----------------------------
class About(models.Model):
    course = models.ForeignKey(Course, related_name="about_sections", on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True, default="")
    content = models.TextField()

    def __str__(self):
        return f"About - {self.course.title}"


class PlacementSupport(models.Model):
    course = models.ForeignKey(Course, related_name="placement_support_sections", on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True, default="")
    content = models.TextField()

    def __str__(self):
        return f"Placement Support - {self.course.title}"


class CorporateTraining(models.Model):
    course = models.ForeignKey(Course, related_name="corporate_training_sections", on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True, default="")
    content = models.TextField()

    def __str__(self):
        return f"Corporate Training - {self.course.title}"


class CourseSectionMeta(models.Model):
    """
    Single row per course storing headings for each section.
    Keeps headings separate from list items (skills/tools/etc).
    """
    course = models.OneToOneField(Course, related_name="section_meta", on_delete=models.CASCADE)
    about_heading = models.CharField(max_length=200, blank=True, default="")
    skills_heading = models.CharField(max_length=200, blank=True, default="")
    tools_heading = models.CharField(max_length=200, blank=True, default="")
    curriculum_heading = models.CharField(max_length=200, blank=True, default="")
    projects_heading = models.CharField(max_length=200, blank=True, default="")
    salary_heading = models.CharField(max_length=200, blank=True, default="")
    placement_support_heading = models.CharField(max_length=200, blank=True, default="")
    corporate_training_heading = models.CharField(max_length=200, blank=True, default="")
    trainers_heading = models.CharField(max_length=200, blank=True, default="")
    batches_heading = models.CharField(max_length=200, blank=True, default="")
    blogs_heading = models.CharField(max_length=200, blank=True, default="")
    faqs_heading = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return f"Section Meta - {self.course.title}"