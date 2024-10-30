from django.contrib import admin
from .models import BlogPost, BlogPostSection, BlogPostImage

class BlogPostSectionInline(admin.TabularInline):
    model = BlogPostSection
    extra = 1  # Number of empty forms displayed by default
    fields = ('subtitle', 'content', 'image', 'order','image_title','image_url','code')  # Displayed fields for each section
    ordering = ['order']  # Ensures sections display in order in the admin

class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1  # Number of empty forms displayed by default
    fields = ('image', 'alt_text')  # Displayed fields for each image

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'author', 'publish_date', 'tag', 'featured')  # Columns in the list view
    list_filter = ('publish_date', 'tag', 'featured')  # Filter options
    search_fields = ('title', 'author', 'tag')  # Searchable fields
    inlines = [BlogPostSectionInline, BlogPostImageInline]  # Inline sections and images

    # Optional: Ordering and default fields
    ordering = ['-publish_date']  # Show newest posts first

@admin.register(BlogPostSection)
class BlogPostSectionAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'subtitle', 'order')  # Columns in the list view
    list_filter = ('blog_post',)  # Filter by blog post

@admin.register(BlogPostImage)
class BlogPostImageAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'alt_text')  # Columns in the list view
    list_filter = ('blog_post',)  # Filter by blog post
