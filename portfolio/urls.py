from django.urls import path
from portfolio import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('about',views.about,name='about'),
    #path('profile',views.profile,name='profile'),
    path('checkout/',views.checkout,name='Checkout'),
    path('contact',views.contact,name='contact'),
    #path('blog',views.blog,name='blog'),
    path('handlerequest/',views.handlerequest,name='HandleRequest'),
    
]
 