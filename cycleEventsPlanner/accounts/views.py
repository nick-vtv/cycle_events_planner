from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from accounts.forms import AccountCreationForm, ProfileEditForm
from accounts.models import Profile, Account

UserModel = get_user_model()

# Create your views here.
class AccountRegisterView(CreateView):
    model = UserModel
    form_class = AccountCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            login(self.request, self.object)

        return response


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('dashboard')
    template_name = 'accounts/profile-delete.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            account_to_deactivate = Account.objects.get(pk=self.request.user.pk)
            account_to_deactivate.is_active = False
            account_to_deactivate.save()

        return response


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'accounts/profiles-list.html'
