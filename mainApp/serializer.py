from .models import *
from rest_framework import permissions, serializers
from django.contrib.auth.models import User
#from .permissions import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        if not User.objects.filter(username =email).exists():
            user, created = User.objects.get_or_create(username = email,email = email,**validated_data)
            user.set_password(password)
            user.save()
            return user

class Custom_UserSerializer(serializers.ModelSerializer):
    """ 
    Custom User Serializer
    https://medium.freecodecamp.org/nested-relationships-in-serializers-for-onetoone-fields-in-django-rest-framework-bdb4720d81e6
    """
    user = UserSerializer(required=True)

    class Meta:
        model = Custom_User
        fields = ['id', 'user',]

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = UserSerializer.create(UserSerializer(), validated_data=user_data)

        custom_user, created = Custom_User.objects.update_or_create(user=user,address=address, **validated_data)
        return custom_user

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('created_at','updated_at','branch')
        read_only_fields = ('created_at','updated_at')

class c_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_class
        fields = ('created_at','updated_at','branch','year')
        read_only_fields = ('created_at','updated_at')

class TeacherSerializer(serializers.ModelSerializer):
    user = Custom_UserSerializer(required = True)
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','user']
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Custom_UserSerializer.create(Custom_UserSerializer(), validated_data=user_data)
        teacher ,created = Teacher.objects.update_or_create(user = user ,**validated_data)
        return teacher
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['created_at','updated_at','name','code']
        read_only_fields = ('created_at','updated_at')

class TeachesClassSerializer(serializers.ModelSerializer):
    c_class = c_classSerializer(read_only=True)
    teacher = serializers.PrimaryKeyRelatedField(many=False, queryset=Teacher.objects.all())
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','name','code','teacher','c_class']
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        pass

class TeachesTeacherSerializer(serializers.ModelSerializer):
    c_class = serializers.PrimaryKeyRelatedField(many=False, queryset=c_class.objects.all())
    teacher = TeacherSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','name','code','teacher','c_class']
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        pass

class TeachesAddSerializer(serializers.ModelSerializer):
    c_class = serializers.PrimaryKeyRelatedField(many=False, queryset=c_class.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(many=False, queryset=Teacher.objects.all())
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','name','code','c_class','teacher']
        read_only_fields = ('created_at','updated_at')

class StudentSerializer(serializers.ModelSerializer):
    c_class = c_classSerializer(read_only=True)
    user = Custom_UserSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','user','c_class']
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        pass

class StudentAddSerializer(serializers.ModelSerializer):
    c_class = serializers.PrimaryKeyRelatedField(many=False, queryset=c_class.objects.all())
    user = Custom_UserSerializer()
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','user','c_class']
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Custom_UserSerializer.create(Custom_UserSerializer(), validated_data=user_data)
        student ,created = Student.objects.update_or_create(user = user ,**validated_data)
        return student

class AssignmentSerializer(serializers.ModelSerializer):
    c_class = serializers.PrimaryKeyRelatedField(many=False, queryset=c_class.objects.all())
    teaches = TeachesAddSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','user','rollno','c_class']
        read_only_fields = ('created_at','updated_at')

class SubmissionSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['created_at','updated_at','student','assignment']
        read_only_fields = ('created_at','updated_at')
