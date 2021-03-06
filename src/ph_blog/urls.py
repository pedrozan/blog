from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import UserRegistrationView
from blog.views import (
    NewBlogView,
    HomeView,
    UpdateBlogView,
    NewBlogPostView,
    UpdateBlogPostView,
    BlogPostDetailsView,
    ShareBlogPostView,
    SharePostWithBlog,
    StopSharingPostWithBlog,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("new-user/", UserRegistrationView.as_view(), name="user_registration"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("blog/new", NewBlogView.as_view(), name="new-blog"),
    path("blog/<pk>/update/", UpdateBlogView.as_view(), name="update-blog"),
    path("blog/post/new/", NewBlogPostView.as_view(), name="new-blog-post"),
    path(
        "blog/post/<pk>/update", UpdateBlogPostView.as_view(), name="update-blog-post"
    ),
    path("blog/post/<pk>/", BlogPostDetailsView.as_view(), name="blog-post-details"),
    path("blog/post/<pk>/share", ShareBlogPostView.as_view(), name="share-blog-post-with-blog"),
    path(
        "blog/post/<post_pk>/share/to/<blog_pk>",
        SharePostWithBlog.as_view(),
        name="share-post-with-blog",
    ),
    path(
        "blog/post/<post_pk>/stop/share/to/<blog_pk>",
        StopSharingPostWithBlog.as_view(),
        name="stop-sharing-post-with-blog",
    ),
]
