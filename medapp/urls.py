from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('', views.front, name= 'front'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signin/index/',views.index,name='index'),
    path('signup/index/', views.index, name='index'),
    path('medstaff/', views.medstaff, name='medstaff'),
    path('meddetail/', views.meddetail, name='meddetail'),
    path('loginadmin/',views.LoginAdmin, name='loginadmin'),
    path('logadmin/admindashboard',views.admindashboard, name='admindashboard'),
    path('register/', views.register_medical_store, name='register'),
    path('unapproved_medical_stores/', views.unapproved_medical_stores, name='unapproved_medical_stores'),
    path('approve_medical_store/<int:store_id>/', views.approve_medical_store, name='approve_medical_store'),
    path('loginmedstaff/', views.Loginmedstaff, name='loginmedstaff'),
    path('loginmedstaff/medical_store_dashboard', views.medical_store_dashboard,name='medical_store_dashboard'),
    path('index/meddetail',views.meddetail,name='meddetail'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('get_medicines/', views.get_medicines, name='get_medicines'),

]