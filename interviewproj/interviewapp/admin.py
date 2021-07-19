from django.contrib import admin
from .models import question,topics,usertohandle,company,experience
admin.site.register(question)
admin.site.register(topics)
admin.site.register(usertohandle)
admin.site.register(company)
admin.site.register(experience)

# Register your models here.
