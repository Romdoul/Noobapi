from django.core.mail.backends import console
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .models import UserProfile, Companies
from django.contrib.auth.models import User
from .serializers import (UserSerializer,
                          CreateUserSerializer,
                          DisplayUserProfileSerializer,
                          CompanySerializer,
                          Screen1Serializer,
                          Screen2Serializer,
                          Screen3Serializer,
                          Screen4Serializer,
                          Screen5Serializer,
                          DisplayCompanySerializer)
from django.core import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import logging
from django.utils.six import BytesIO

logger = logging.getLogger()


class UserViewSet(viewsets.ModelViewSet):
    # authentication_class = (JSONWebTokenAuthentication,)  # Don't forget to add a 'comma' after first element to make it a tuple
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    print("hello1")
    serialized = UserSerializer(data=request.data)
    print(serializers)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_class = (JSONWebTokenAuthentication,)
    queryset = Companies.objects.all()
    # print("this is queryset ")
    print(queryset)
    serializer_class = CompanySerializer
    print(serializer_class)
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_company(request):
    serialized = CompanySerializer(data=request.data)
    # print(serializers)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        userID = []
        jsonformat = mdict()
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        users = UserProfile.objects.filter(user=token.user_id)
        serializer = DisplayUserProfileSerializer(users, many=True)
        for i in users:
            userID.append(i.id)
            print(i.id)
        for i in range(len(userID)):
            jsonformat= {'token': token.key, 'id': userID[i]}

        return Response(jsonformat)


@permission_classes((AllowAny,))
class UserRegistration(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        snippets = UserProfile.objects.all()
        print(snippets)
        serializer = CreateUserSerializer(snippets, many=True)
        # print(serializer)
        return Response(serializer.data)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            country=request.POST['country'],
            full_name=request.POST['full_name'],
            age=request.POST['age'],
            date_of_birth=request.POST['date_of_birth'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email'],
        )
        print(user)
        print(request.POST['country'])
        serializer = Screen1Serializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     user = request.user
    #     logging.debug(user)
    #     serializer = CreateUserSerializer(data=request.POST)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # UserProfile.objects.create(
    #     user=user,
    #     country='Cambodia',
    #     full_name='bobo',
    # )


class SubmitScreen2View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            job=request.POST['job'],
            location=request.POST['location'],
            expect_salary=request.POST['expect_salary'],
            payment_method=request.POST['payment_method'],
            salary_duration=request.POST['salary_duration'],
        )
        print(user)
        serializer = Screen2Serializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SubmitScreen3View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            current_designation=request.POST['current_designation'],
            working_years_cc=request.POST['working_years_cc'],
            skills=request.POST['skills'],
            experiences=request.POST['experiences'],
            no_coworker=request.POST['no_coworker'],
            disability=request.POST['disability'],
            department=request.POST['department'],
            current_salary=request.POST['current_salary'],
            current_salary_duration=request.POST['current_salary_duration'],
        )
        print(user)
        serializer = Screen3Serializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SubmitScreen4View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            family_member=request.POST['family_member'],
            father_occupation=request.POST['father_occupation'],
            no_siblings=request.POST['no_siblings'],
            no_relative=request.POST['no_relative'],
            current_asset=request.POST['current_asset'],
        )
        print(user)
        serializer = Screen4Serializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SubmitScreen5View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            training=request.POST['training'],
            training_methods=request.POST['training_methods'],
            duration_training=request.POST['duration_training'],
        )
        print(user)
        serializer = Screen5Serializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class DisplayUserProfileView(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_id = []
        email_ = []
        jsonformat = mdict()
        user_profile = UserProfile.objects.all()
        print(user_profile)
        for i in user_profile:
            print(i.user.username)
            email_.append(i.user.email)
            user_id.append(i.user.id)
        users = UserProfile.objects.all()
        serializer1 = Screen1Serializer(users, many=True)
        print(serializer1)
        serializer1 = Screen1Serializer(users, many=True)
        serializer2 = Screen2Serializer(users, many=True)
        serializer3 = Screen3Serializer(users, many=True)
        serializer4 = Screen4Serializer(users, many=True)
        serializer5 = Screen5Serializer(users, many=True)
        for i in range(len(email_)):
            jsonformat['msg'] = {
                's1': serializer1.data[i],
                's2': serializer2.data[i],
                's3': serializer3.data[i],
                's4': serializer4.data[i],
                's5': serializer5.data[i],
            }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayScreen1View(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        users_id = []
        jsonformat = mdict()
        response = super(DisplayScreen1View, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_profile = UserProfile.objects.filter(user=token.user_id)
        serializer = Screen1Serializer(user_profile, many=True)
        print(token.user_id)
        for i in user_profile:
            print(i.user)
            users_id.append(i.user)
        for i in range(len(users_id)):
            jsonformat['screen1'] = {
                'country': serializer.data[i]['country'],
                'full_name': serializer.data[i]['full_name'],
                'age': serializer.data[i]['age'],
                'date_of_birth': serializer.data[i]['date_of_birth'],
                'address': serializer.data[i]['address'],
                'phone': serializer.data[i]['phone'],
                'email': serializer.data[i]['email']
            }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayScreen2View(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        users_id = []
        jsonformat = mdict()
        response = super(DisplayScreen2View, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_profile = UserProfile.objects.filter(user=token.user_id)
        serializer = Screen2Serializer(user_profile, many=True)
        print(token.user_id)
        for i in user_profile:
            print(i.user)
            users_id.append(i.user)
        for i in range(len(users_id)):
            jsonformat['screen2'] = {
                'job': serializer.data[i]['job'],
                'location': serializer.data[i]['location'],
                'expect_salary': serializer.data[i]['expect_salary'],
                'payment_method': serializer.data[i]['payment_method'],
                'salary_duration': serializer.data[i]['salary_duration']
            }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayScreen3View(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        users_id = []
        jsonformat = mdict()
        response = super(DisplayScreen3View, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_profile = UserProfile.objects.filter(user=token.user_id)
        serializer = Screen3Serializer(user_profile, many=True)
        print(token.user_id)
        for i in user_profile:
            print(i.user)
            users_id.append(i.user)
        for i in range(len(users_id)):
            jsonformat['screen3'] = {
                'current_designation': serializer.data[i]['current_designation'],
                'working_years_cc': serializer.data[i]['working_years_cc'],
                'skills': serializer.data[i]['skills'],
                'experiences': serializer.data[i]['experiences'],
                'no_coworker': serializer.data[i]['no_coworker'],
                'disability': serializer.data[i]['disability'],
                'department': serializer.data[i]['department'],
                'current_salary': serializer.data[i]['current_salary'],
                'current_salary_duration': serializer.data[i]['current_salary_duration']
            }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayScreen4View(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        users_id = []
        jsonformat = mdict()
        response = super(DisplayScreen4View, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_profile = UserProfile.objects.filter(user=token.user_id)
        serializer = Screen4Serializer(user_profile, many=True)
        print(token.user_id)
        for i in user_profile:
            print(i.user)
            users_id.append(i.user)
        for i in range(len(users_id)):
            jsonformat['screen4'] = {
                'family_member': serializer.data[i]['family_member'],
                'father_occupation': serializer.data[i]['father_occupation'],
                'no_siblings': serializer.data[i]['no_siblings'],
                'no_relative': serializer.data[i]['no_relative'],
                'current_asset': serializer.data[i]['current_asset']
            }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayScreen5View(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        users_id = []
        jsonformat = mdict()
        response = super(DisplayScreen5View, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_profile = UserProfile.objects.filter(user=token.user_id)
        serializer = Screen5Serializer(user_profile, many=True)
        print(token.user_id)
        for i in user_profile:
            print(i.user)
            users_id.append(i.user)
        for i in range(len(users_id)):
            jsonformat['screen5'] = {
                'training': serializer.data[i]['training'],
                'training_methods': serializer.data[i]['training_methods'],
                'duration_training': serializer.data[i]['duration_training']
            }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayUserProfileForWebView(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_name = []
        user_email = []
        jsonformat = mdict()
        user_profile = UserProfile.objects.all()
        for i in user_profile:
            # print(i.user.username)
            user_name.append(i.user.username)  # get value form queryset object from User
            user_email.append(i.user.email)
            print(i.id)
        users = UserProfile.objects.all()
        serializer = DisplayUserProfileSerializer(users, many=True)
        for i in range(len(user_name)):
            # print(serializer.data[i])
            jsonformat['userprofile'] = {'id': serializer.data[i]['id'],
                                         'availability': serializer.data[i]['availability'],
                                         'username': user_name[i],
                                         'email': user_email[i],
                                         'age': serializer.data[i]['age'],
                                         'phone': serializer.data[i]['phone'],
                                         'skills': serializer.data[i]['skills']
                                         }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayCompanyView(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        company_name = []
        compnay_email = []
        jsonformat = mdict()
        company = Companies.objects.filter(company_name_type=2)
        print(company)
        for i in company:
            # user = User.objects.get(pk=i.id)
            print(i.company_user.username)
            company_name.append(i.company_user.username)
            compnay_email.append(i.company_user.email)
        for i in range(len(company_name)):
            jsonformat['companies'] = {'companyname': company_name[i],
                                       'companyemail': compnay_email[i],
                                      }
        return Response(jsonformat)


@permission_classes((AllowAny,))
class DisplayAllUsersView(APIView):
    def get(self, request):
        companies = User.objects.all()
        serializer = UserSerializer(companies, many=True)
        print(serializer)
        return Response(serializer.data)


@permission_classes((AllowAny,))
class DisplayUserInCompany(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        company_name = []
        company_id = []
        username = []
        user_id = []
        jsonformat = mdict()
        company = Companies.objects.filter(company_name_type=2)
        for i in company:
            # print(i.company_user.username)
            company_name.append(i.company_user.username)
            company_id.append(i.id)
            # print(i.company_user.username)
            users_ = UserProfile.objects.filter(company=i.id)
            # print(users_)
            for j in users_:
                print(j.id)
                username.append(str(j.user))
                user_id.append(str(j.id))
            # print(username)
            jsonformat['user_in_company'] = {i.id: {"users": username}}
            username = []

        return Response(jsonformat)


@permission_classes((AllowAny,))
class TestingUserInCompany(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        company_name = []
        company_id = []
        username = []
        users_id = []
        jsonformat = mdict()
        response = super(TestingUserInCompany, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        companies = Companies.objects.filter(user=token.user_id)
        for i in companies:
            company_name.append(i.company_user.username)
            company_id.append(i.id)
            print(i.id)
            users_ = UserProfile.objects.filter(company=i.id)
            for j in users_:
                username.append(str(j.user))
                users_id.append(str(j.id))
                print(username)
            jsonformat['user_in_company'] = {i.id: {"users": username}}
            username = []
        return Response(jsonformat)
        # serializer = Screen5Serializer(user_profile, many=True)
        # print(token.user_id)
        # for i in user_profile:
        #     print(i.user)
        #     users_id.append(i.user)
        # for i in range(len(users_id)):
        #     jsonformat['screen5'] = {
        #         'training': serializer.data[i]['training'],
        #         'training_methods': serializer.data[i]['training_methods'],
        #         'duration_training': serializer.data[i]['duration_training']
        #     }



class mdict(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)