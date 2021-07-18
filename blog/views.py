from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
# from django.views.generic import *
#from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# class PostList(generic.ListView):
#     model = Post
#     template_name = 'post_list.html'
#     # context_object_name = 'post'
#    # queryset = Post.objects.filter(status=1).order_by('-created_on')

def PostDetail(request, slug): 
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {'post':post}) 

# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save() # saves in database
			messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
	else:
		form = ContactForm()
	return render(request,'contact.html',{'form': form})

def postlist(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	pt = Post.objects.all()
	# pt = Post.objects.filter(status=1).order_by('-created_on')
	return render(request,"blog/post_list.html", {'pt':pt})


	