from django.contrib import admin

# Register your models here.
from django.contrib import admin

from reviews.models import (Publisher, Contributor, Book,
BookContributor, Review)
# Register your models here.
admin.site.register(Publisher)
# admin.site.register(Contributor)
admin.site.register(BookContributor)

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13','has_isbn')
    list_filter = ('publisher', 'publication_date')
    @admin.display(ordering='isbn', description='ISBN-13',
                   empty_value='-/-')
    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4],
                                       obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])

    @admin.display(boolean=True, description='Has ISBN', )
    def has_isbn(self, obj):
        """ '9780316769174' => True """
        return bool(obj.isbn)
class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    fieldsets = (
        ("Linkage", {"fields": ("creator", "book")}),
        ("Review content", {"fields": ("content", "rating")}),
    )
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ['last_names__startswith', 'first_names__startswith']
    list_filter = ['last_names']

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)