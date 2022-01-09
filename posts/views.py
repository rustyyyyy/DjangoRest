from django.shortcuts import render
from .models import Post
from django.http import JsonResponse


def post_list_and_create(request):
    qs = Post.objects.all()
    context = {'qs':qs}
    return render(request,'posts/main.html',context)

def load_post_data_view(request,**kwargs):
    visible = 3
    upper = kwargs.get('num_posts')
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    data = []
    for obj in qs:
        item = {
            'id' : obj.id,
            'title' : obj.title,
            'liked' : True if request.user in obj.liked.all() else False,
            'count' : obj.like_count,
            'body' : obj.body,
            'aurthor' : obj.author.user.username
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper],'size' : size})

def like_unlike_posts(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj .liked.remove(request.user)
        else:
            liked = True
            obj .liked.add(request.user)
        return JsonResponse({'liked':liked,'count':obj.like_count})