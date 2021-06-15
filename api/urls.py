from django.urls import path

from api.views import NewsListAPIView, NewsRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view()),
]
