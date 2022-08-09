from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here -->

# author
class Author(models.Model):
    authorID=models.CharField(max_length=200, primary_key=True)
    name=models.CharField(max_length=200,null=True, blank=True)
    phoneNumber=models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    birthDate=models.DateField(null=True, blank=True)
    deathDate=models.DateField(null=True, blank=True)

    class Meta:
        ordering=['authorID']
    def __str__(self):
        return self.name

# category
class Category(models.Model):
    categoryID=models.CharField(max_length=200, primary_key=True)
    name=models.CharField(max_length=200, null=True, blank=True)

    # class Meta:
    #     ordering=['categoryID']
    # def __str__(self):
    #     return self.name

# Books
class Book(models.Model):
    bookID=models.CharField(max_length=200, primary_key=True)
    title=models.CharField(max_length=200, null=True, blank=True)
    authorID=models.ForeignKey(Author,on_delete=models.SET_NULL, null=True, blank=True) # author model
    publisher=models.CharField(max_length=200,null=True, blank=True)
    publishDate=models.DateField(null=True, blank=True)
    categoryID=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True) # category model
    price=models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    soldCount=models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering=['bookID']
    def __str__(self):
        return self.title