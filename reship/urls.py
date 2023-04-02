from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.signin, name="login"),
    path('signup', views.signup, name="register"),
    # path('index-2/', views.index_2, name='index-2'),
    # path('index-3/', views.index_3, name='index-3'),
    path('about-us/', views.about_us, name='about-us'),
    path('pricing-plans/', views.pricing_plans, name='pricing-plans'),
    path('contact-us/', views.contact_us, name='contact-us'),
    # path('blog-left/', views.blog_left, name='blog-left'),
    # path('blog/', views.blog, name='blog'),
    # path('coming-soon/', views.coming_soon, name='coming-soon'),
    # path('get-quote/', views.get_quote, name='get-quote'),
    # path('index-animation/', views.index_animation, name='index-animation'),
    # path('single-blog/', views.single_blog, name='single-blog'),
    # path('tracking/', views.tracking, name='tracking'),
]