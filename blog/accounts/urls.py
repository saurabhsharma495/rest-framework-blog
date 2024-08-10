from django.urls import path
from accounts.views import RegisterView, loginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', loginView.as_view(), name='login'),
]