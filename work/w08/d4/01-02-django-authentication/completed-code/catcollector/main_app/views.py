from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
import os
from .models import Cat, Toy, Photo
from .forms import FeedingForm

# View functions

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cats_index(request):
  cats = Cat.objects.filter(user=request.user)
  # You could also retrieve the logged in user's cats like this
  # cats = request.user.cat_set.all()
  return render(request, 'cats/index.html', { 'cats': cats })

@login_required
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # Get the toys that the cat doesn't have
  toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the detail.html template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    'cat': cat,
    'feeding_form': feeding_form,
    'toys': toys_cat_doesnt_have
  })


class CatCreate(LoginRequiredMixin, CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class CatUpdate(LoginRequiredMixin, UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(LoginRequiredMixin, DeleteView):
  model = Cat
  success_url = '/cats/'

@login_required
def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in the posted form
  form = FeedingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

@login_required
def add_photo(request, cat_id):
  # photo-file will be the "name" attribute on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # build a unique filename keeping the image's original extension
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, cat_id=cat_id)
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', cat_id=cat_id)

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('detail', cat_id=cat_id)

@login_required
def unassoc_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.remove(toy_id)
  return redirect('detail', cat_id=cat_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)