from django.http import HttpResponse
from django.shortcuts import render
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

class PhotoUpdate(UpdateView):
    model = Photo
    fields = '__all__' 
    
class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')
    fields = '__all__'

def base(request):
    return render(request, 'base.html')

class CategoryListView(ListView):
	model = Category

class CategoryDetailView(DetailView):
	model = Category

class PhotoListView(ListView):
	model = Photo

class PhotoDetailView(DetailView):
	model = Photo


def category(request):
	category_list = Category.objects.all()
	context = {'object_list': category_list}
	return render(request, 'album/category.html', context)

def category_detail(request, category_id):

	category = Category.objects.get(id=category_id)
	context = {'object': category}
	return render(request, 'album/category_detail.html', context)

