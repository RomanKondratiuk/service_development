from django.contrib import messages

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class ConfirmEmailView(View):
    def get(self, request, token):
        User = get_user_model()
        try:
            user = User.objects.get(email_verification_token=token)
            user.is_active = True
            user.email_verification_token = None  # delete token
            user.save()
            messages.success(request, 'Your email has been successfully confirmed. You can now log in.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email verification token.')
        return redirect('users:login')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # We create a user, but do not save it yet
        user = form.save(commit=False)

        # Additional logic for sending a confirmation email
        user.generate_email_verification_token()  # Generating a token
        user.is_active = False  # Making the user inactive until the email is confirmed
        user.save()

        # send an email with a link to confirm your email
        self.send_verification_email(user)

        # return super().form_valid(form)
        return render(self.request, 'users/verification_sent.html')

    def send_verification_email(self, user):
        # Generating a URL with a token to confirm your email
        verification_url = self.request.build_absolute_uri(
            reverse('users:confirm_email', args=[user.email_verification_token]))

        # send an email with a link to confirm your email
        subject = 'Confirmation email'
        message = f'To confirm your email, follow the following link:\n\n{verification_url}'
        from_email = 'roma.kondratiuk2001@mail.ru'  # local email
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm

    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
