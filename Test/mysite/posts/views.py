from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect


from .models import Posts
from .forms import PostsForm


# Create your views here.

def index(request):
  # return HttpResponse("Hello from posts")

  if request.method == 'POST':
      form = PostsForm(request.POST)
      if form.is_valid():
        text = form.cleaned_data['text']
        ip = get_client_ip(request)
        Posts.objects.create(text=text, ip=ip).save()
        return HttpResponseRedirect('/posts')

  else:
      form = PostsForm()

  posts = Posts.objects.all().order_by('-created_at')
  context = {
    'create_post': 'Type your thoughts :)',
    'latest_posts': 'Latest Posts',
    'posts': posts,
    'form': form
  }

  return render(request, 'posts/index.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # ip = x_forwarded_for.split(',')[0]
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



