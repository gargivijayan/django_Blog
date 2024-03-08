from django.shortcuts import render,redirect,HttpResponse
from blog.models import blog
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages

# Create your views here.
def index(request):
    obj= blog.objects.all()
    return render(request,'index.html',{"hello": obj})
def about(request):
    return render(request,'about.html')
def recentposts(request):
    return render(request,'recent-posts.html')
def add(request):
    if request.method == "POST":
        title = request.POST.get('bname')
        image = request.FILES.get('pic')
        if image:
            file_path = f"media/article_images/{image.name}"
            default_storage.save(file_path, ContentFile(image.read()))
        description = request.POST.get('explain')
        date = timezone.now().date()
        query = blog(title= title, image=image, description=description, date=date)
        query.save()
        messages.success(request,"Details Added Successfully")
     
    return render(request,'add.html')

def detailed(request,id):
    data={
        "content":blog.objects.get(id=id)
        
    }
    return render(request,'details.html',data)

def delete(request,id):
    dlt=blog.objects.get(id=id)
    dlt.delete()
   
    return redirect("/")

def edit(request, id):
    edit_post = blog.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        new_image = request.FILES.get('image')  # Get the new image
        description = request.POST.get('description')
        date = timezone.now().date()
        
       
        if new_image:
            if edit_post.image:
           
                default_storage.delete(edit_post.image.path)
     
            file_path = f"media/article_images/{new_image.name}"
            default_storage.save(file_path, ContentFile(new_image.read()))
        
        edit_post.title = title
        edit_post.image = new_image if new_image else edit_post.image 
        edit_post.description = description
        edit_post.date = date
        edit_post.save() 
        messages.success(request,"Details Updated Successfully")
        return render(request,'edit.html')
 

    return render(request, 'edit.html', {"content": edit_post})




