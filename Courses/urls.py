from django.contrib import admin
from django.urls import path,include
from Courses import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dash/', views.myCourses,name="dash"),
    path('dash/<str:code>/', views.course_page, name='course'),
    path('assignment/<str:code>/<int:id>/',
         views.assignmentPage, name='assignmentPage'),
    path('profile/', views.profile, name='profile'),
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


