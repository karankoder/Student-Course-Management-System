import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
User=get_user_model();
from Courses.models import *

def myCourses(request):
    try:
        if request.user.is_authenticated:
            student=request.user
            sem=student.semester
            dept=student.department
            courseid=sem_courses.objects.filter(sem_id=sem,dept_id=dept)
            courses=[]
            for id in courseid:
                 courses.append(Course.objects.get(course_id=id.course_id))

            context = {
                
                'courses':courses,
                'student': student,
                # 'faculty': faculty
            }

            return render(request, 'Courses/dashboard.html', context)
        else:
            return redirect('/')
    except:
       return redirect('/')

def course_page(request, code):
    try:
        course = Course.objects.get(course_id=code)
        if request.user.is_authenticated:
            try:
                announcements = Announcement.objects.filter(course_id=course.course_id)
                assignments = Assignment.objects.filter(
                    course_id=course.course_id)
                materials = Material.objects.filter(course_id=course.course_id)

            except:
                announcements = None
                assignments = None
                materials = None

            context = {
                'course': course,
                'announcements': announcements,
                'assignments': assignments[:3],
                'materials': materials,
                'student': request.user
            }

            return render(request, 'Courses/course.html', context)

        else:
            return redirect('dash')
    except:
        return redirect('/')

def assignmentPage(request, code, id):
    course = Course.objects.get(course_id=code)
    if request.user.is_authenticated:
        assignment = Assignment.objects.get(course_id=course.course_id, id=id)
        try:

            submission = Submission.objects.get(assignment=assignment, student=request.user)

            context = {
                'assignment': assignment,
                'course': course,
                'submission': submission,
                'time': datetime.datetime.now(),
                'student': request.user,
                
            }

            return render(request, 'Courses/assignment-portal.html', context)

        except:
            submission = None

        context = {
            'assignment': assignment,
            'course': course,
            'submission': submission,
            'time': datetime.datetime.now(),
            'student': request.user,
            
        }

        return render(request, 'Courses/assignment-portal.html', context)
    else:

        return redirect('/')
    
def profile(request):
    # try:
        if request.user.is_authenticated:
            student = request.user
            return render(request, 'Courses/profile.html', {'student': student})
        else:
            return redirect('/')
    # except:
    #     return redirect('/')





# Create your views here.
