from django.contrib import admin
from user_content import models

# Register your models here.
admin.site.register(models.Courses)
admin.site.register(models.SiteUser)
admin.site.register(models.CoursesVideoLinks)


