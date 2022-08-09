from django.contrib import admin

from . import models

# Register your models here.
# author
admin.site.register(models.Author)
# category
admin.site.register(models.Category)
# books
admin.site.register(models.Book)
   