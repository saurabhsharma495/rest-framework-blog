from django.urls import path
from core.views import BlogView

urlpatterns = [
    path('create-blog/', BlogView.as_view(), name='create-blog'),
]