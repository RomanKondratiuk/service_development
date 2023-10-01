from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.utils import send_email_for_verify


class EmailVerify(View):
    pass


class RegisterView(CreateView):
    # model = User
    # form_class = UserRegisterForm
    template_name = 'users/register.html'

    # success_url = reverse_lazy('users:login')
    def get(self, request):
        context = {
            'form': UserRegisterForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm

    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         if form.data.get('heed_generate', False):
    #             self.object.set_password(
    #                 self.object.make_random_password(length=12)
    #             )
    #             self.object.save()
    #         return super().form_valid(form)
