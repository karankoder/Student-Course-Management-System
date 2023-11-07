from django.contrib import admin
from Courses.models import *

admin.site.register(department)
admin.site.register(Course)
admin.site.register(sem_courses)
admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Material)

# Register your models here.
