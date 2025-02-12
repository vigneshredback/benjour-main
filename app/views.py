from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import JournalName , Volume, Issue, Paper
# Create your views here.

@login_required(login_url='login')
def index(request):
    journal_name = JournalName.objects.all()
    return render(request, 'pages/index.html',{'journal_name':journal_name})


@login_required(login_url='login')
def aim(request):
    return render(request, 'pages/aim.html')

@login_required(login_url='login')
def scope(request):
    return render(request, 'pages/scope.html')

@login_required(login_url='login')
def team(request):
    return render(request, 'pages/team.html')

@login_required(login_url='login')
def privacy(request):
    return render(request, 'pages/privacy.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'pages/contact.html')

@login_required(login_url='login')
def submission(request):
    return render(request, 'pages/submission.html')

@login_required(login_url='login')
def journal_volume(request,journal_id):
    journal_volume = Volume.objects.filter(journal_name_id=journal_id)
    return render(request, 'pages/volume.html',{'journal_volume':journal_volume})

@login_required(login_url='login')
def journal_issue(request,journal_id):
    journal_issue = Issue.objects.filter(volume_id=journal_id)
    return render(request, 'pages/issue.html',{'journal_issue':journal_issue})

@login_required(login_url='login')
def journal_paper(request,journal_id):
    journal_paper = Paper.objects.filter(journal_issue_number_id=journal_id)
    print(journal_paper)
    return render(request, 'pages/paper.html',{'journal_paper':journal_paper})

@login_required(login_url='login')
def journal_paper_view(request,journal_id):
    paper_view = Paper.objects.get(id=journal_id)
    return render(request, 'pages/paper_view.html',{'paper_view':paper_view})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'pages/register.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate username
        if not username:
            return redirect('register')

        # Validate passwords match
        if password != confirm_password:
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return redirect('register')

        if User.objects.filter(email=email).exists():
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return redirect('login')
   
    return render(request, 'pages/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('index')  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'pages/login.html')


def logout_view(request):
    logout(request)  # Logs the user out
    messages.success(request, "You have been successfully logged out!")
    return redirect('login')  # Redirect to the login page or home page