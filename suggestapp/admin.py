from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import feedback, new_prompt

# Register your models here
admin.site.register(feedback)
admin.site.register(new_prompt)
