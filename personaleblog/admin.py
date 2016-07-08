from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','describe','create_at','update_at')
    prepopulated_fields = {"slug": ("name",)}
    exclude = ('create_at','update_at')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','is_pass','categroy')
    exclude = ('create_at','update_at')
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    exclude = ('create_at','update_at')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)
