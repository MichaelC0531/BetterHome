from django.urls import path
from . import views

urlpatterns = [
  path('', views.JobList.as_view(), name='job'),
  path('about/', views.about, name='about'),
  path('myjob/', views.myjob_index, name='myjob'),
  path('job/<int:job_id>/', views.job_detail, name='job_detail'),
  path('job/create/', views.JobCreate.as_view(), name='job_create'),
  path('job/<int:pk>/update/', views.JobUpdate.as_view(), name='job_update'),
  path('job/<int:pk>/delete/', views.JobDelete.as_view(), name='job_delete'),
  path('job/<int:job_id>/add_quotation', views.add_quotation, name='add_quotation'),
  #add photo
  path('job/<int:job_id>/add_photo', views.add_photo, name='add_photo'),
  #add quot
  path('job/<int:job_id>/add_quotation/', views.add_quotation, name='add_quotation'),
  #sign up and pick ac 
  path('accounts/signup/', views.signup, name='signup'),
  path('identifier/', views.Identifier.as_view(), name='identifier')
]