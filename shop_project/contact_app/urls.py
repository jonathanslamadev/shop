from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
  path('', views.contact, name='contact'),
  path('contact_succes/', views.contact_succes, name=contact_succes)


]