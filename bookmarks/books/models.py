from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cityes')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countrys')
    website = models.URLField()

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='authors')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self) -> str:
        return self.title
