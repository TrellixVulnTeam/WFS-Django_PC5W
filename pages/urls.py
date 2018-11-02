
from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('jobs/', views.jobs_list, name='jobs'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	# path('create/', views.create_form, name="create_form"),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
