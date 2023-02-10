from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=63)
    lastname = models.CharField(max_length=63)
    wikipedia = models.URLField(blank=True)

    def __str__(self):
        return  f"{self.firstname} {self.lastname}"


class Book(models.Model):
    ADVENTURE = "AD"
    THRILLER = "TH"
    FANTASTIC = "FA"
    ROMANCE = "RO"
    HORROR = "HO"
    SCIENCE_FICTION = "SF"
    CATEGORIES = [
        (ADVENTURE, "Aventure"),
        (THRILLER, "Thriller"),
        (FANTASTIC, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-Fiction"),
    ]
    title = models.CharField(max_length=63)
    price = models.FloatField(blank=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default="Aventure", blank=True)
    stock = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title
