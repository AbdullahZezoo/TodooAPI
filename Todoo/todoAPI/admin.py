from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status')
    search_fields = ('status',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Task, TaskAdmin)
