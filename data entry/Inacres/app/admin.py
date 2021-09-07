from django.contrib import admin
from .models import New_registration, New_project, Document_details, PostImage
# Register your models here.

admin.site.register(New_registration)
admin.site.register(New_project)
admin.site.register(Document_details)
admin.site.register(PostImage)

'''
class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Document_details)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Document_details
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
'''
