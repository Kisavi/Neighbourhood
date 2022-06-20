from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .forms import SignupForm, LoginForm, UpdateUserForm, UpdateProfileForm, ProfileForm, PostForm, CommentForm, \
    BusinessForm, AlertForm
from django.contrib.auth.views import LoginView
from .models import Post, Business, Alert
from django.http import HttpResponseRedirect
from django.urls import reverse


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

            return redirect(to='login')

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


# def home(request):
#     current_user = request.user
#     posts = Post.objects.all()
#     business_form = BusinessForm()
#     alert_form = AlertForm()
#     if request.method == 'POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             post = post_form.save(commit=False)
#             post.poster = current_user
#             post.save()
#         return redirect('home')
#     else:
#         post_form = PostForm()
#
#     return render(request, 'main/home.html',
#                   {'posts': posts, 'post_form': post_form, 'business_form': business_form, 'alert_form': alert_form})


def home(request):
    current_user = request.user
    posts = Post.objects.all()
    businesses = Business.objects.all()
    alerts = Alert.objects.all()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            alert_form = AlertForm(request.POST)
            if alert_form.is_valid():
                alert = alert_form.save(commit=False)
                alert.poster = current_user
                alert.save()
            return redirect('home')
        elif request.POST.get("form_type") == 'formTwo':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.poster = current_user
                post.save()
            return redirect(reverse('home') + '#formThree')
        else:
            business_form = BusinessForm(request.POST)
            if business_form.is_valid():
                business = business_form.save(commit=False)
                business.poster = request.user
                business.save()
            return redirect('home')
    else:
        alert_form = AlertForm()
        post_form = PostForm()
        business_form = BusinessForm()

    return render(request, 'main/home.html',
                  {'posts': posts, 'alerts': alerts, 'businesses': businesses, 'post_form': post_form,
                   'business_form': business_form, 'alert_form': alert_form})


def hoodProfile(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if hood_form.is_valid():
            profile = hood_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')
    else:
        hood_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/hoodform.html', {'hood_form': hood_form})


def comment(request, id):
    current_user = request.user
    post = get_object_or_404(Post, pk=id)
    comments = post.comment.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.commentor = current_user
            comment.save()
        return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        }
    return render(request, 'main/comment.html', context)


# def post_business(request):
#     if request.method == 'POST':
#         business_form = BusinessForm(request.POST)
#         if business_form.is_valid():
#             business = business_form.save(commit=False)
#             business.poster = request.user
#             business.save()
#         return redirect('home')
#     else:
#         business_form = BusinessForm()
#     return render(request, 'main/home.html', {'business_form': business_form})
#
#
# def post_alert(request):
#     alert_form = AlertForm()
#     return render(request, 'main/home.html', {'alert_form': alert_form})


#
# def comment(request):
#     comment_form = CommentForm()
#     return render(request, 'main/view_post.html', {'comment_form': comment_form})


def update_profile(request):
    posts = request.user.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'You have successfully updated your profile')
            return redirect(to='profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    # context = {
    #         'user_form': user_form,
    #         'profile_form': profile_form
    # }

    return render(request, 'main/profile.html', {'user_form': user_form, 'profile_form': profile_form, 'posts': posts})


def view_post(request):
    return render(request, 'main/view_post.html')
