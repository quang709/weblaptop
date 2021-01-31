from django.contrib import admin

# Register your models here.

from.models import Category
from.models import Product
#dang ky model student voi admin
admin.site.register(Product)
admin.site.register(Category)


