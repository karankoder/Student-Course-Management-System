from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth import get_user_model
User=get_user_model();
dept_choices=[
    ('CSE','CSE'),
    ('MNC','MNC'),
    ('ECE','ECE'),
    ('EEE','EEE'),
    ('MEC','MEC'),
    ('CER','CER'),
    ('CHE','CHE'),
    ('CIV','CIV'),
    ('MET','MET'),
    ('MIN','MIN'),
    ('PHE','PHE'),
    ('APD','APD'),
]
class department(models.Model):
    dept_id=models.CharField(max_length=50,choices=dept_choices)
    name=models.CharField(max_length=200,null=False)
    description=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=50,primary_key=True)
    course_name = models.CharField(max_length=200,null=False,unique=True)
    credits = models.IntegerField()
    department=models.CharField(max_length=20,choices=dept_choices,null=True)
    user=models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.course_id

class sem_courses(models.Model):
    sem_id=models.IntegerField()
    dept_id=models.CharField(max_length=50,choices=dept_choices)
    course_id = models.ForeignKey(
        Course,on_delete=models.CASCADE, to_field='course_id'
    )
class Announcement(models.Model):
    course_id = models.ForeignKey(
    Course, on_delete=models.CASCADE, null=False,to_field='course_id')
    datetime = models.DateTimeField(auto_now_add=True, null=False)
    description = FroalaField()
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.datetime.strftime("%d-%b-%y, %I:%M %p")

    def post_date(self):
        return self.datetime.strftime("%d-%b-%y, %I:%M %p")

class Assignment(models.Model):
    course_id = models.ForeignKey(
    Course, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    datetime = models.DateTimeField(auto_now_add=True, null=False)
    deadline = models.DateTimeField(null=False)
    file = models.FileField(upload_to='assignments/', null=True, blank=True)
    marks = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def post_date(self):
        return self.datetime.strftime("%d-%b-%y, %I:%M %p")

    def due_date(self):
        return self.deadline.strftime("%d-%b-%y, %I:%M %p")
    
class Submission(models.Model):
    assignment = models.ForeignKey(
    Assignment, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    file = models.FileField(upload_to='submissions/', null=True,)
    datetime = models.DateTimeField(auto_now_add=True, null=False)
    marks = models.DecimalField(
    max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
    def time_difference(self):
        difference = self.assignment.deadline - self.datetime
        days = difference.days
        hours = difference.seconds//3600
        minutes = (difference.seconds//60) % 60
        seconds = difference.seconds % 60

        if days == 0:
            if hours == 0:
                if minutes == 0:
                    return str(seconds) + " seconds"
                else:
                    return str(minutes) + " minutes " + str(seconds) + " seconds"
            else:
                return str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"
        else:
            return str(days) + " days " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"
    def submission_date(self):
        return self.datetime.strftime("%d-%b-%y, %I:%M %p")
class Material(models.Model):
    course_id = models.ForeignKey(
    Course, on_delete=models.CASCADE, null=False)
    description = models.TextField(max_length=2000, null=False)
    datetime = models.DateTimeField(auto_now_add=True, null=False)
    title=models.CharField(max_length=100,null=True)
    file = models.FileField(upload_to='materials/', null=True, blank=True)
    


    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def post_date(self):
        return self.datetime.strftime("%d-%b-%y, %I:%M %p")


# Create your models here.
