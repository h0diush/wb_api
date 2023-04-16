from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import users

router = DefaultRouter()

urlpatterns = [
    path('users/reg/', users.RegistrationView.as_view(), name='reg'),
    path('generate_code/', users.GenerateCodeForTelegram.as_view(),
         name='generate-code'),
]
