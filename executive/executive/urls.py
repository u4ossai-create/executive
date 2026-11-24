from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),
    path('portal/', views.portal, name='portal'),
    path('contact/', views.contact, name='contact'),
    
    # Result URLs
    path('results/', views.result_login, name='result_login'),
    path('results/dashboard/', views.result_dashboard, name='result_dashboard'),
    path('results/logout/', views.result_logout, name='result_logout'),
]