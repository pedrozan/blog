from django.urls import reverse
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from blog.forms import BlogForm
from blog.models import Blog


class NewBlogView(CreateView):
    form_class = BlogForm
    template_name = 'blog_settings.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)

        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Blog.objects.filter(owner=user).exists():
            return HttpResponseForbidden('You can not create more than one blog per account')
        else:
            return super(NewBlogView, self).dispatch(request, *args, **kwargs)
