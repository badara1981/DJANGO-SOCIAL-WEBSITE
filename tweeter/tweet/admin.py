from django.contrib import admin

from . models import Publisher, City, Country, Author, Tweet

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = 'name address city country website'.split()
    list_display = 'name city website'.split()

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = 'first_name last_name email'.split()
    list_display = 'first_name last_name email'.split()

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    fields = 'title authors publication_date'.split()

