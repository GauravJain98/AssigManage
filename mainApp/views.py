from django.shortcuts import render
from .serializer import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .models import *
# Create your views here.

def exp(request):
    teches =Teacher.objects.prefetch_related('taught_by').filter(id=1)
    print(teches)
    print("wtf")
    return Response({})

class BranchList(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class c_classList(viewsets.ModelViewSet):
    queryset = c_class.objects.all()
    serializer_class = c_classSerializer

class TeacherList(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectList(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeachesClassList(viewsets.ModelViewSet):
    queryset = Teaches.objects.all()
    serializer_class = TeachesClassSerializer

class TeachesAddList(viewsets.ModelViewSet):
    queryset = Teaches.objects.all()
    serializer_class = TeachesAddSerializer

class TeachesTeacherList(viewsets.ModelViewSet):
    queryset = Teaches.objects.all()
    serializer_class = TeachesTeacherSerializer

class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentAddSerializer

class AssignmentList(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class SubmissionList(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
