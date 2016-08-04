from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ("title","slug","published","author",)
	list_filter = ("status","created","published","author",)
	search_field = ("title","body",)
	prepopulate_fields = {'slug':('title',),}
	raw_id_fields = ('author',)
	date_hierarchy = "published"
	ordering = ['status','published',]

admin.site.register(Post,PostAdmin)

# Register your models here.
