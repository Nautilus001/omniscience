from django.contrib import admin
from .models import Project, Container

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'client', 'status')
    search_fields = ('name', 'client')

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'status', 'project')
    list_filter = ('status', 'project')
    search_fields = ('name', 'image')