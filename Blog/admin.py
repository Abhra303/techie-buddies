from django.contrib import admin
from .models import Author,Blog,Tag,Comment,Like

# Register your models here.


admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Like)