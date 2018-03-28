from django.db import models
from django.contrib.auth.models import User


USER_TYPE = (
    ('1', 'Administrator'),
    ('2', 'Client user | Company'),
    ('3', 'Normal user | Construction worker')
)
SCREENS = (
    ('1', 'Register'),
    ('2', 'Work Details'),
    ('3', 'Family'),
    ('4', 'Education Background'),
    ('5', 'Work Condition')
)
EVALUATION_TYPE = (
    ('1', 'Behaviour of working'),
    ('2', 'Technical skill'),
    ('3', 'Collaboration'),
    ('4', 'Hard work')
)


class Companies(models.Model):
    company_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='')
    # staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    company_name_type = models.CharField(max_length=100, choices=USER_TYPE, null=True, blank=True)
    # company_email = models.CharField(max_length=100, null=True, blank=True)
    # company_password = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, null=True, blank=True)
    availability = models.BooleanField(default=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True, blank=True, default='')
    country = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    current_designation = models.CharField(max_length=100, null=True, blank=True)
    working_years_cc = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    experiences = models.CharField(max_length=100, null=True, blank=True)
    no_coworker = models.CharField(max_length=100, null=True, blank=True)
    disability = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    current_salary = models.CharField(max_length=100, null=True, blank=True)
    current_salary_duration = models.CharField(max_length=100, null=True, blank=True)
    family_member = models.CharField(max_length=100, null=True, blank=True)
    father_occupation = models.CharField(max_length=100, null=True, blank=True)
    no_siblings = models.CharField(max_length=100, null=True, blank=True)
    no_relative = models.CharField(max_length=100, null=True, blank=True)
    current_asset = models.CharField(max_length=100, null=True, blank=True)
    training = models.CharField(max_length=100, null=True, blank=True)
    training_methods = models.CharField(max_length=100, null=True, blank=True)
    duration_training = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    expect_salary = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    salary_duration = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)

    # def __str__(self):
    #     return self.user.username


class EvaluationMasters(models.Model):
    user_evaluations = models.ManyToManyField(UserProfile, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    evaluator = models.CharField(max_length=50, null=True, blank=True)
    receiver = models.CharField(max_length=100, null=True, blank=True)
    evaluation_type = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False, blank=True)







