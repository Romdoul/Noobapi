from tokenize import Comment

from rest_framework import serializers
from backend.users.models import UserProfile, Companies
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class DisplayUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'company', 'availability', 'age', 'phone', 'skills')


class DisplayCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('id', 'user', 'company_user', 'company_name_type')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user, user_type=3)
        return user


class CompanySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    print("company serializer")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        company_user = super(CompanySerializer, self).create(validated_data)
        print(str(company_user))
        company_user.set_password(validated_data['password'])
        company_user.save()
        Companies.objects.create(company_user=company_user, company_name_type=2)
        return company_user


class Screen1Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('country', 'full_name', 'age', 'date_of_birth', 'address', 'phone', 'email')


class Screen2Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('job', 'location', 'expect_salary', 'payment_method', 'salary_duration')


class Screen3Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('current_designation', 'working_years_cc', 'skills', 'experiences', 'no_coworker', 'disability', 'department', 'current_salary', 'current_salary_duration')


class Screen4Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('family_member', 'father_occupation', 'no_siblings', 'no_relative', 'current_asset')


class Screen5Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('training', 'training_methods', 'duration_training')