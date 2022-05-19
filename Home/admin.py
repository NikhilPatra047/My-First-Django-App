from django.contrib import admin
from Home.models import Contact

# Register your models here.
#NOTE FROM ME: After creating the models, they have to be registered within the admin.py
admin.site.register(Contact)
