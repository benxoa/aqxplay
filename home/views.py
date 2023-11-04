from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    photos = Publish.objects.all()
    # user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Publish.objects.filter()
    else:
        photos = Publish.objects.filter(
            category__name=category, )

    categories = Category.objects.filter()
    context = {'categories': categories, 'x': photos}
    
    return render(request, 'home.html', context)
    
    
@login_required(login_url="/login")
def publish(request):
    categories = Category.objects.all()
    images = request.FILES.getlist('images')
    
    data = request.POST

    if request.method == 'POST':
        
        
        title = data['title']
        description = data['description']
        category = Category.objects.get(id=data['category'])
        user = request.user
        

        for image in images:
            photo = Publish.objects.create(
                user=user,
                title=title,
                category=category,
                description=description,
                image=image,
            )
        messages.success(request, "You Work Has Been Uploaded! Thanks!")
        return redirect(publish)
        

    context = {'categories': categories}
    return render(request, 'publish.html',context )

def viewWork(request, pk):
    work = Publish.objects.get(id=pk)
    return render(request, 'work.html', {'work': work, 'uploaded_by': work.user.username})

def error_404(request, exception):
    return render(request, '404.html', status=404)
    
def login_page(request):
    if request.method== "POST":
        data = request.POST.get
        username = data('username')
        password = data('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "User does'nt Exits!")
            return redirect(login)
        else:
            login(request, user)
            return redirect(publish)


        
    return render(request, 'login.html')
    
def signup(request):
    if request.method == "POST":
        data = request.POST.get
        username = data('username')
        email = data('email')
        pass1 = data('password')
        pass2 = data('password2')

        user  = User.objects.filter(username = username) or User.objects.filter(email = email)
        if user.exists():
            messages.info(request, " Username or Email Already Exits!")
            return redirect(signup)
        if pass1 != pass2:
            messages.info(request, " Password does'nt match!")
            return redirect(signup)
        
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(pass1)
        user.save()
        return redirect(login_page)
    

    return render(request, 'signup.html')

def logout_page(request):
    logout(request)
    return redirect(home)

@login_required(login_url="/login")
def dashboard(request):
    
    # Get the user's posts
    user_posts = Publish.objects.filter(user=request.user)
    
    context = {
        'user_posts': user_posts
    }
    
    return render(request, 'dashboard.html', context)
@login_required(login_url="/login")
def delete_publish(request,pk):
    delete = Publish.objects.get(id=pk)
    delete.delete()
    
    messages.success(request, "Work Deleted Successfully!")
    return redirect(dashboard)

from django.shortcuts import get_object_or_404

def edit_publish(request, pk):
    current_record = get_object_or_404(Publish, id=pk)
    data = request.POST

    if request.method == 'POST':
        # Update the fields of the current_record
        current_record.title = request.POST['title']
        current_record.description = request.POST['description']
        # Update other fields as needed

        # Save the updated record
        current_record.save()

        messages.success(request, "Work Updated!")
        return redirect(dashboard)
    # Replace 'home' with your actual URL name or path

    return render(request, 'edit_publish.html', {'current_record': current_record})
