from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('contact/submit/', views.contact_submit_view, name='contact_submit'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),
]
