from django.contrib import admin
from .models import BlogPost, BlogPostSection, BlogPostImage, ContentBlock

class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 1
    fields = ('content_type', 'content', 'code', 'image', 'image_title','image_url')  # Only relevant fields per content type

class BlogPostSectionInline(admin.TabularInline):
    model = BlogPostSection
    extra = 1
    fields = ('subtitle', 'order')  # Simplified fields, as detailed content now goes in ContentBlock
    ordering = ['-order']
    inlines = [ContentBlockInline]  # Nested inline for flexible content blocks

class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 1
    fields = ('image', 'alt_text')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'tag', 'featured')
    list_filter = ('publish_date', 'tag', 'featured')
    search_fields = ('title', 'author', 'tag')
    inlines = [BlogPostSectionInline, BlogPostImageInline]
    ordering = ['-publish_date']

@admin.register(BlogPostSection)
class BlogPostSectionAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'subtitle', 'order')
    list_filter = ('blog_post',)
    inlines = [ContentBlockInline]  # Allow adding ContentBlocks directly within each BlogPostSection

@admin.register(BlogPostImage)
class BlogPostImageAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'alt_text')
    list_filter = ('blog_post',)
