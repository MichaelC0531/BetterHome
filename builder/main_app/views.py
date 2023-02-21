import uuid
import boto3
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Job, Identity, Quotation, Photo
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuotationForm
S3_BASE_URL = 'https://s3-us-east-1.amazonaws.com/'
BUCKET = 'betterhomeproject'

# def home(request):
#     return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Identifier(LoginRequiredMixin, CreateView):
    model = Identity
    fields = ['identity']
    success_url = '/'
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class JobList(ListView):
    model = Job
    paginate_by = 10
    def get_queryset(self):
      queryset = super().get_queryset()
      search_term = self.request.GET.get('search_term', '')
      if search_term:
          queryset = queryset.filter(Q(work__contains=search_term) | 
                            Q(location__contains=search_term) | 
                            Q(description__contains=search_term))
      print(queryset.query)
      return queryset

@login_required
def myjob_index(request):
    jobs_table = None
    if request.user.identity.get_identity_display() == 'Client':
      jobs = Job.objects.filter(user=request.user)
      jobs_table = jobs
    elif request.user.identity.get_identity_display() == 'Service Provider':
      quoted_jobs = Quotation.objects.filter(user=request.user)
      jobs_table = quoted_jobs
    search_term = request.GET.get('search_term', '')
    if search_term:
        jobs_table = jobs_table.filter(Q(work__contains=search_term) | 
                          Q(location__contains=search_term) | 
                          Q(description__contains=search_term))
    paginator = Paginator(jobs_table, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jobs/myjob.html', {'page_obj': page_obj})
      
def job_detail(request, job_id):
    if not request.user.is_authenticated:
      return redirect('/accountslogin')
    job = Job.objects.get(id=job_id)
    quotation = Quotation.objects.filter(job_id=job_id)
    quotation_form = QuotationForm()
    identity = Identity.objects.get(user=request.user)
    if identity.get_identity_display() == 'Service Provider' and not quotation.filter(user=request.user).exists():
        show_quotation_form = True
    else:
        show_quotation_form = False
    return render(request, 'jobs/detail.html', {'job': job, 'quotation_form': quotation_form, 'identity': identity, 'quotation': quotation, 'show_quotation_form': show_quotation_form})

@login_required
def add_quotation(request, job_id):
  form = QuotationForm(request.POST)
  if form.is_valid():
    new_quotation = form.save(commit=False)
    new_quotation.job_id = job_id
    new_quotation.user = request.user
    new_quotation.save()
    messages.success(request, 'Quotation submission successful')
  return redirect('job_detail', job_id=job_id)

class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['work', 'location', 'description', 'start_date', 'duration']
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_date'].widget = DateInput(attrs={'class': 'datepicker'})
        return form

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['work', 'location', 'description', 'start_date', 'duration']

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/myjob/'


@login_required
def add_photo(request, job_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        photo = Photo(url=url, job_id=job_id)
        photo.save()
    except:
        print('An error occurred uploading file to S3')
  return redirect('job_detail', job_id=job_id)

def signup(request):
  error_message = ''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('identifier')
    else:
      print(form.errors)
      error_message = 'invalid signup, try again'
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  })