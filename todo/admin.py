from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    search_fields=('task',)
    list_display=('task','is_completed','updated_at')

admin.site.register(Task,TaskAdmin)