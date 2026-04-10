from django.db import models

class BlogPost(models.Model):
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.DateField()
    read_time = models.CharField(max_length=50)
    excerpt = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    image_url = models.URLField(blank=True, default="")
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class BlogParagraph(models.Model):
    post = models.ForeignKey(BlogPost, related_name="paragraphs", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Paragraph for {self.post.title}"


class TableOfContent(models.Model):
    post = models.ForeignKey(BlogPost, related_name="toc", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# 🔷 BLOG PAGE META TAGS (SEO) - Singleton
class MetaTags(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.meta_title or "Blog MetaTags"