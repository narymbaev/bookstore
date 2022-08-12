from django.contrib import admin
from .models import Book, Review
# Register your models here.
class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1
    

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ('title', 'author', 'price',)

admin.site.register(Book, BookAdmin)