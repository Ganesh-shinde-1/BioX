from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),

    # research
    path('research/', views.research, name='research'),
    path('research/<slug:slug>/', views.research, name='research_slug'),

    # posts
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.posts, name='posts'),

    # blogs
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<slug:slug>/', views.blogs, name='blogs'),

    # news
    path('news/', views.news, name='news'),
    path('news/<slug:slug>/', views.news, name='news'),



 
    # contanct info
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),


    path( 'exams/', views.exams, name='exams' ), 
    path( 'exam/<slug:category>/', views.exam_list, name='exam_list' ),
    path( 'exams/<slug:slug>/', views.exam_detail, name='exam_detail' ),
]