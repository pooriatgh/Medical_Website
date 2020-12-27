from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileDetailView, UserCreateView, ProfileUpdateView, UserDeleteView, HospitalDetailView

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='base_panel/home.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='page-login.html'), name='login'),

    path('hospital/<int:hospital_id>', HospitalDetailView.as_view(), name='hospital-detail'),

    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('registration/', UserCreateView.as_view(), name='profile-create'),
    path('profileUpdate/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='user-delete'),
]
