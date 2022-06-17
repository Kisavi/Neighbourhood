from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView


# Create your views here.
class SignupView(View):
    form_class = SignupForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created successfully')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # set sessions as modified to force cookies to be saved as defined.
            self.request.session.modified = True
        # else session will last as long as we define it in settings.py.
        return super(CustomLoginView, self).form_valid(form)


def index(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def profile(request):
    return render(request, 'main/profile.html')


def view_post(request):
    return render(request, 'main/view_post.html')
