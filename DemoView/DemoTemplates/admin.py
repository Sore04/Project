from django.contrib import admin
from .models import Item, Book

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("name", "description")
  
admin.site.register(Item, MemberAdmin)


class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author")


admin.site.register(Book, BookAdmin)
