from django.contrib import admin
from .models import UserProfile, EvaluationMasters, Companies

admin.site.register(UserProfile)
admin.site.register(Companies)
admin.site.register(EvaluationMasters)
