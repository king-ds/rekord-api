from django.urls import path
from rekord_api import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('transportation', views.CreateTransportation.as_view()),
    path('transportation/list', views.ListTransportation.as_view()),
    path('transportation/update/<int:id>', views.UpdateTransportation.as_view()),
]