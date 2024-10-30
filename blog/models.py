from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now_add=True)
    read_time = models.IntegerField()
    tag = models.CharField(max_length=50)
    content = models.TextField(default="Default content")
    featured = models.BooleanField(default=False)
    # Other fields as necessary

    def __str__(self):
        return self.title  # Optional, makes it easier to identify BlogPost instances in the admin

class BlogPostSection(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='sections')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    code = models.TextField(blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)  # Title for the image
    image_url = models.URLField(blank=True, null=True)  # URL link for the image

    class Meta:
        ordering = ['order']  # Ensures sections are displayed in the correct order

    def __str__(self):
        # Optional: Display subtitle if available, otherwise display the content preview
        return f"Section: {self.subtitle or self.content[:50]}"

class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"Image for {self.blog_post.title}"  # Provides context in admin interface
