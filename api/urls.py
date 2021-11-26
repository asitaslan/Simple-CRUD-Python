from django.urls import path

from api.views import PracticeListCreateAPIView, PracticeDetailAPIView

urlpatterns = [
    path('practices/', PracticeListCreateAPIView.as_view(), name='practices_list'),
    path('practices/detail/<pk>', PracticeDetailAPIView.as_view(), name='practices_detail')
]