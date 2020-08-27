from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from account.forms import SignUpForm, ProfileUpdateForm
from blog.models import Post, Category
from account.models import Profile
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.


class UserCreateView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpForm
    success_url = "/blogs"



def profile_page_view(request):
    user = request.user.id
    # users = User.objects.get(id=user)
    profiles = Profile.objects.get(user_id=user)
    posts = Post.objects.filter(author=profiles)
    print(profiles)
    context = {
        'profiles': profiles,
        'posts': posts,
    }
    return render(request, 'account/profile.html', context)


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "account/profile_update.html"
    success_url = reverse_lazy('profile')
