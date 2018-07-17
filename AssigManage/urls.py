from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from mainApp import views
from AssigManage     import settings

router = DefaultRouter()

router.register(r'branch', views.BranchList)
router.register(r'c_class', views.c_classList)
router.register(r'teacher', views.TeacherList)
router.register(r'subject', views.SubjectList)

router.register(r'teaches/teacher', views.TeachesTeacherList)
router.register(r'teaches/add', views.TeachesAddList)
router.register(r'teaches/class', views.TeachesClassList)
router.register(r'student', views.StudentList)
router.register(r'assignment', views.AssignmentList)
router.register(r'submission', views.SubmissionList)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('exp/', views.exp),
    url(r'^', include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns