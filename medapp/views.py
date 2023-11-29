from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile
from .models import MedStock
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MedicalStore
from django.shortcuts import render
from .models import MedicalStore
from django.shortcuts import get_object_or_404, redirect
from .models import MedicalStore
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .models import MedicalStore


def home(request):
    return render(request,'home.html')
def front(request):
    return render(request,'front.html')
def medstaff(request):
    return render(request,'medstaff.html')
def index(request):
    return render(request,'index.html')
def meddetail(request):
    return render(request,'meddetail.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # You can add more fields to the UserProfile model and save them here if needed
        user_profile = UserProfile(user=user)
        user_profile.save()

        # Log in the user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # Replace 'home' with the URL name of your homepage

    return render(request, 'home.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')  # Replace 'home' with the URL name of your homepage

    return render(request, 'home.html')

def index(request):
    return render(request,'index.html')



def admindashboard(request):
    return render(request,'admin.html')
def LoginAdmin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None and  user.is_superuser:
            login(request,user)
            return redirect('admindashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request,'loginadmin.html')


def register_medical_store(request):
    if request.method == 'POST':
        # Handle registration form submission
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        reg_number = request.POST['registration_number']

        user = User.objects.create_user(username=username, password=password)
        medical_store = MedicalStore(user=user, name=name, registration_number=reg_number)
        medical_store.save()

        return redirect('medstaff')  # Assuming you have a login view with the name 'login'

    return render(request, 'mediregform.html')


def unapproved_medical_stores(request):
    unapproved_stores = MedicalStore.objects.filter(is_approved=False)
    context = {'unapproved_stores': unapproved_stores}
    return render(request, 'unapproved_medical_stores.html',context)



def approve_medical_store(request, store_id):
    store = get_object_or_404(MedicalStore, pk=store_id)
    store.is_approved = True
    store.save()
    return redirect('unapproved_medical_stores')


def Loginmedstaff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.medicalstore.is_approved:
            login(request, user)
            return redirect('medical_store_dashboard')  # Replace 'dashboard'    with your actual dashboard URL
        else:
            messages.error(request, 'Invalid login or user not approved.')

    return render(request,
                  'medical_staff_login.html')  # Replace 'medical_store_login.html' with your actual login template


@login_required
def medical_store_dashboard(request):
    # Your dashboard logic here
    return render(request,'medstaff.html')  # Replace 'medical_store_dashboard.html' with your actual dashboard template



def add_medicine(request):
    if request.method == 'POST':
        med_name = request.POST.get('med_name')
        usage = request.POST.get('usage')
        qty = request.POST.get('qty')

        # Create a new MedStock object and save it to the database
        med_stock = MedStock(med_name=med_name, usage=usage, qty=qty)
        med_stock.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_medicines(request):
    medicines = MedStock.objects.all().values('id', 'med_name', 'usage', 'qty')
    return JsonResponse({'medicines': list(medicines)})