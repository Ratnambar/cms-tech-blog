from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import ContactForm
from blog.forms import PostForm
from django.views import View
from blog.models import Post, Category
from account.models import User,Profile
from django.views.generic import ListView,CreateView, DetailView,FormView, UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def indexPage(request,*args,**kwargs):
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})
    # posts = Post.objects.filter(status="D")
    # post_titles = [post.title for post in posts]
    # title_str = ("\n\n").join(post_titles)
    # return HttpResponse(title_str)


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # context['author'] = Author.objects.all()
        return context


class PostFormView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    # model = Post
    template_name = 'blog/post.html'
    form_class = PostForm

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     user = User.objects.get(username= self.request.user)
    #     kwargs.update({'initial':{'author': user}})
    #     return kwargs
    #
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


def search_code(request):
    search_term = ""
    articles = []
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        posts = Post.objects.all()
        for post in posts:
            if search_term.lower() in post.title.lower() or search_term in post.title.lower():
                print(search_term)
                print(post.title)
                articles.append(post)
        # articles = Post.objects.filter(title=search_term)
        # print(articles)
        # print(search_term)
        return render(request, "blog/search.html", context={'articles': articles})
    else:
        return render(request, "blog/search.html")


def view_by_cat_button(request, id,*args,**kwargs):
    category = Category.objects.all()
    posts = Post.objects.filter(category__id=id)
    # print(posts)
    context = {
        'category': category,
        'posts': posts
        }
    return render(request, 'blog/cat_views.html', context)


class BtnBlogDetails(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Post
    template_name = "blog/btn-details.html"


class PostDetailsView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Post
    template_name = "blog/details.html"


class PostFormUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # success_url = "contact"
    template_name = "blog/post.html"

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     user = Profile.objects.get(username=self.request.user)
    #     kwargs.update({'initial': {'author': user}})
    #     return kwargs
    #
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class PostFormDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('profile')
    template_name = "blog/confirm-delete.html"


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = "contact"
    template_name = "blog/contact.html"

    def form_valid(self, form):
        return super().form_valid(form)


def Trending_Posts(request,*args,**kwargs):
    trending_posts = Trending_Posts.objects.all()
    print(trending_posts)
    return render(request, "blog/index.html", context={"trending_posts": trending_posts})


def post_edit_form_view(request,id,*args,**kwargs):
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponse("Invalid Post ID")

    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, "blog/post.html", context={"form": form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse("welcome")

        return render(request, "blog/post.html", context={"form": form})
    return render(request, "blog/post.html", context={"form": form})



