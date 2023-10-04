from django.urls import path
from .views import ServicesListView,ReserveCreateView


app_name='services'
#from .views import HomeView

#from . import views

urlpatterns = [
    path("", ServicesListView.as_view(), name='services'),
    path("reserve/", ReserveCreateView.as_view(), name='reserve'),

    ]