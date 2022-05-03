from random import randint
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View, UpdateView, CreateView, ListView

from mixins import AnonymousUserMixin
from utils import send_otp_code

from .forms import UserLoginForm, UserRegisterForm, VerifyCodeForm, UserForm, AdminForm
from .models import OtpCode

user = get_user_model()


class UserRegisterView(AnonymousUserMixin, View):
    template_name = "account/register.html"
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"from": form})

    def post(self, request):
        form = self.form_class(request.POST)
        clean_data = form.cleaned_data
        if form.is_valid():
            random_number = randint(1000, 9999)
            send_otp_code(form.cleaned_data["phone"], random_number)
            OtpCode.objects.create(
                phone_number=clean_data["phone_number"], code=random_number
            )
            request.session["user_registration_info"] = {
                "phone_number": form.cleaned_data["phone"],
                "email": form.cleaned_data["email"],
                "full_name": form.cleaned_data["full_name"],
                "password": form.cleaned_data["password"],
            }
            messages.success(request, "", "")
            return redirect("")
        messages.error(request, "", "")
        return render(request, self.template_name, {"form": form})


class VerifyUserView(View):
    template_name = "account/verify.html"
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        user_session = request.session["user_registration_info"]
        code_instance = OtpCode.objects.get(phone_number=user_session["phone_number"])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd["code"] == code_instance.code:
                user_obj = user.objects.create_user(
                    user_session["phone_number"],
                    user_session["email"],
                    user_session["full_name"],
                    user_session["password"],
                )
                login(request, user_obj)
                code_instance.delete()
                messages.success(request, "", "success")
                return redirect("")
            else:
                messages.error(request, "", "danger")
                return redirect("")
        return render(request, self.template_name, {"form": form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "", "success")
        return redirect()


class UserLoginView(AnonymousUserMixin, View):
    form_class = UserLoginForm
    template_name = "accounts/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, phone_number=cd["phone"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "", "info")
                return redirect("home:home")
            messages.error(request, "", "warning")
        return render(request, self.template_name, {"form": form})


def home(request):
    return render(request, 'panel/tables-editable.html')


class UserUpdateView(UpdateView):
    model = user
    template_name = 'account/update.html'
    success_url = reverse_lazy('account:home')
    slug_field = 'id'
    slug_url_kwarg = 'user_id'
    form_class = UserForm


class CreateAdminView(CreateView):
    model = user
    template_name = 'account/create_admin.html'
    success_url = reverse_lazy('account:admin_list')
    form_class = AdminForm


class AdminListView(ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = 'account/admin_list.html'
