from django.urls import path

from api.views import PracticeListCreateAPIView, PracticeDetailAPIView

urlpatterns = [
    path('practices/list/create', PracticeListCreateAPIView.as_view(), name='practices_list'),
    path('practices/detail/update/delete/<pk>', PracticeDetailAPIView.as_view(), name='practices_detail')
]