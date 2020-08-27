from django.urls import path, re_path
# from blog.views import index
from blog.views import indexPage,PostListView,PostFormView,search_code,view_by_cat_button,BtnBlogDetails, ContactFormView, post_edit_form_view,  PostDetailsView,PostFormUpdateView,PostFormDeleteView


urlpatterns = [
    # path("index", indexPage),
    path("", PostListView.as_view(template_name="blog/index.html"), name="index"),
    # path("<int:id>", post_details),
    # path("<int:pk>", PostDetailsView.as_view()),
    path("posts", PostFormView.as_view(template_name="blog/post.html"), name="post"),
    # path("posts", post_form_view),
    path("search/", search_code, name="search"),
    path("contact", ContactFormView.as_view(template_name="blog/contact.html"), name="contact"),
    path("filter/<int:id>", view_by_cat_button),
    path("filter/<slug:slug>", BtnBlogDetails.as_view()),
    path("<slug:slug>", PostDetailsView.as_view(), name="post-detail"),
    path("posts/<slug:slug>", PostFormUpdateView.as_view(), name="update-blog"),
    path("delete/<slug:slug>", PostFormDeleteView.as_view(),name="delete-blog",)
]