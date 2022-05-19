from django.contrib import admin
from Home.models import Home_contact

# Register your models here.
#NOTE FROM ME: After creating the models, they have to be registered within the admin.py
admin.site.register(Home_contact)
