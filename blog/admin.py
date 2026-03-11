from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'slug', 'status', 'created_on')
    # Fields that can be searched
    search_fields = ['title', 'content']
    # Sidebar filters
    list_filter = ('status', 'created_on')
    # Automatically populate the slug based on the title
    prepopulated_fields = {'slug': ('title',)}
    # Enable Summernote editor for the content field
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Columns to show in the comments list
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    # Filters for the comments section
    list_filter = ('approved', 'created_on')
    # Search functionality for comments
    search_fields = ('author', 'body')
    # Custom action to approve multiple comments at once
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)