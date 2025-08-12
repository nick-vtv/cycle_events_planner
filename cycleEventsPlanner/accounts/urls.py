from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import DeleteView

from accounts.views import AccountRegisterView, ProfileDetailView, ProfileUpdateView, ProfileDeleteView, ProfileListView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailView.as_view(), name='profile-detail'),
        path('edit/', ProfileUpdateView.as_view(), name='profile-update'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]) ),
    path('profiles/all/', ProfileListView.as_view(), name='all-profiles'),
]