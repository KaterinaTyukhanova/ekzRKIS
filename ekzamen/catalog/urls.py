from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.LoginServerView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutServerView.as_view(), name='logout'),
    path('contacts/', views.contacts, name="contacts"),
    path('products/', views.products, name="products"),
    path('about/', views.about, name="about"),
    path('create/', views.TovarCreateView.as_view(), name="create_tovar"),
    path('signup/', views.signup, name='signup'),
]