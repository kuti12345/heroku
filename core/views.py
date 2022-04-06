from django.shortcuts import render, redirect,get_object_or_404
from core.models import *
from core.views import*
from .forms import CommentForm
from django.http import Http404
from django.db.models import Count
# Create your views here.
def cotagory(request):
    cotagory=Category.objects.all()
    detail=Post.objects.all() 
    col_visit=Post.objects.all().values("visit").aggregate(Count('visit'))
    return render(request, 'block_and_include/bl_index.html', {'cotagory': cotagory,'detail': detail,"col_visit":col_visit})

def post_detail(request, id):
    cotagory=Category.objects.all()
    detail = Post.objects.filter(category=id)
   
    return render(request, 'block_and_include/bl_index.html', {'detail': detail,'cotagory': cotagory})

def vivod(request,id):
    vivod=Post.objects.get(id=id)
    vivod.visit+=1
    vivod.save()
    comment=Comment.objects.filter(post=vivod)
    return render(request, 'block_and_include/bl_detailview.html', {'vivod': vivod,'comment':comment})
    
def delete(request,id, vivod_id):
    Comment.objects.get(id=id).delete()
    return redirect('vivod', vivod_id)

def create_view(request,id):
    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if form.is_valid():
            instance_comment = form.save(commit=False)
            instance_comment.post_id = id
            instance_comment.save()
            return redirect('vivod', id)
    else:
        form =CommentForm()
        vivod=Post.objects.get(id=id)
        context = {
            'form': form
        }
        return render(request, 'create.html', context)

def update_view(request, id,vivod_id):
    old_data = Comment.objects.get(id=id)
    
    if request.method =='POST':
        form = CommentForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect('vivod', vivod_id)
    else:
        form = CommentForm(instance = old_data)
        context ={
            'form':form
        }
        return render(request, 'create.html', context)
