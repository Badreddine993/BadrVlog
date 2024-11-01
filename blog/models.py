from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now_add=True)
    read_time = models.IntegerField()
    tag = models.CharField(max_length=50)
    content = models.TextField(default="Default content")
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class BlogPostSection(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='sections')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Section: {self.subtitle or f'Order {self.order}'}"

class ContentBlock(models.Model):
    CONTENT_TYPES = [
        ('text', 'Text'),
        ('math', 'Math'),
        ('code', 'Code'),
        ('image', 'Image'),
    ]

    section = models.ForeignKey(BlogPostSection, on_delete=models.CASCADE, related_name='content_blocks')
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    content = models.TextField(blank=True, null=True, help_text="Enter text or LaTeX for math content.")
    code = models.TextField(blank=True, null=True, help_text="Enter code snippet if content type is code.")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text="Upload an image if content type is image.")
    image_title = models.CharField(max_length=255, blank=True, null=True, help_text="Optional title for the image.")

    def __str__(self):
        return f"{self.get_content_type_display()} for Section {self.section.order}"

class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.blog_post.title}"
