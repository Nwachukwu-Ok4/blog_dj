from django.shortcuts import render, redirect
from .forms import NewBlog
from .models import Blog
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.

@login_required(login_url="userLogin")
def blogHome(request):
    allBlogs = Blog.objects.all()
    return render(request, "blog/blogHome.html", {"allBlogs" : allBlogs})

def addblog(request):
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogHome")
    else:
      newForm = NewBlog
    return render(request, "blog/addblog.html", {"form" : newForm})

def blogDetails(request, pk):
      blog = Blog.objects.get(pk = pk)
      return render(request, "blog/blogDetails.html", {"blog": blog} )

#! new .....................
# create a delete function that will delete a blog post and redirect to the blog homepage
def is_admin(user):
    return user.is_superuser or user.is_staff


@user_passes_test(is_admin)
###.. deleteBlog(request, id):
def deleteBlog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect("blogHome")

