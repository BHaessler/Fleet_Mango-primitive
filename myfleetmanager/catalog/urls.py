""" Declares urls for the web app to use and reference"""

from django.urls import path
from . import views

from .views import OwnerCreateView, owner_success_view, register_view, edit_footer_content 
from .views import user_list, add_user, edit_user, delete_user


# URL Patterns fall under here
urlpatterns = [
    path('', views.home_page, name='index'), #homepage path
    path('edit-footer/', edit_footer_content, name='edit_footer_content'), #edit footer content

    #CAR oriented paths go here
    path('cars/', views.CarListView.as_view(), name='cars'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),

    #OWNER oriented paths go here
    path('owner/create/', OwnerCreateView.as_view(), name='owner-create'),
    path('owner/success/', owner_success_view, name='owner-success'),  # Success URL
    path('owner/<int:pk>/', views.OwnerDetailView.as_view(), name='owner-detail'),
    path('owners/', views.OwnerListView.as_view(), name='owners'),
    
    #Separational View paths go here
    path('register/', register_view, name='register'),

    #Customer paths
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('customer/cars/', views.CustomerCarListView.as_view(), name='customer_cars'),

    # Admin paths
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('users/', user_list, name='user_list'),
    path('users/add/', add_user, name='add_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),

    # Mechanics paths
    path('mechanics/dashboard/', views.mechanic_dashboard, name='mechanics_dashboard'),
    ]
