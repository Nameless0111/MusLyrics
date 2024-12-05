from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ('songs',)

admin.site.register(Author, AuthorAdmin)