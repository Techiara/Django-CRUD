from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Post._meta.get_fields()]
