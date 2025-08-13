from django.contrib import admin

from common.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    ordering = ('-id',)
