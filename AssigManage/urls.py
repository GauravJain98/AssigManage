from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from mainApp import views

router = DefaultRouter()

router.register(r'branch', views.BranchList)
router.register(r'c_class', views.c_classList)
router.register(r'teacher', views.TeacherList)
router.register(r'subject', views.SubjectList)

router.register(r'teaches/teacher', views.TeachesTeacherList)
router.register(r'teaches/class', views.TeachesClassList)
router.register(r'student', views.StudentList)
router.register(r'assignment', views.AssignmentList)
router.register(r'submission', views.SubmissionList)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
