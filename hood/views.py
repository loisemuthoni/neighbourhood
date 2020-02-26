from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Business,NeighborHood,Userprofile,Post,PoliceCenters,HealthCenter,Comment
from .forms import NewProfileForm,NewNeighborhoodForm,UpdateForm,NewPostForm,NewBusinessForm,NewCommentForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):

    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()
    posts=Post.get_all_posts()

    current_user=request.user
    if request.method == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)

            comment.commenter = current_user

            comment.save()
        return redirect('homepage')
    else:
        form=NewCommentForm()


    return render(request,'homepage.html',{"businesses":businesses,"neighborhoods":neighborhoods,"posts":posts,"form":form})

def comments(request):

    comments=Comment.get_comments()

    return render(request,'comments.html',{"comments":comments})

def new_comment(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)

            comment.commenter = current_user

            comment.save()
        return redirect('homepage')
    else:
        form=NewCommentForm()
    return render(request,'comment.html',{"form":form})

def post(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.owner = current_user
            post.save()
        return redirect('homepage')
    else:
        form=NewPostForm()
    return render(request,'post.html',{"form":form})




def business(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('homepage')
    else:
        form=NewBusinessForm()
    return render(request,'business.html',{"form":form})