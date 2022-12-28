from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Job, Identity, Quotation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuotationForm
# Create your views here.
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

@login_required
def myjob_index(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/myjob.html', {'jobs': jobs} )


def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    quotation_form = QuotationForm()
    if not request.user.is_authenticated:
      return redirect('/accountslogin')
    identity = Identity.objects.get(user=request.user)
    return render(request, 'jobs/detail.html', {'job': job, 'quotation_form': quotation_form, 'identity': identity})

@login_required
def add_quotation(request, job_id):
  form = QuotationForm(request.POST)
  if form.is_valid():
    new_quotation = form.save(commit=False)
    new_quotation.job_id = job_id
    new_quotation.user = request.user
    new_quotation.save()
  return redirect('job_detail', job_id=job_id)

class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['work', 'location', 'description', 'start_date', 'duration']
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['work', 'location', 'description', 'start_date', 'duration']

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = ''

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