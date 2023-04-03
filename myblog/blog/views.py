from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm  # import PostForm here
from django.shortcuts import render, redirect  # import redirect function
from django.utils import timezone
from django.urls import reverse




def post_list(request):
    posts = Post.objects.all()
    recent_posts = Post.objects.order_by('-created_at')[:5]  # use the 'created_at' field instead of 'published_date'
    return render(request, 'blog/post_list.html', {'posts': posts, 'recent_posts': recent_posts})




def post_detail(request, pk):
    print(pk)  # Add this line to check the pk value
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'pk': pk})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    print(form.errors) # Debugging statement
    return render(request, 'blog/post_new.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
  







def my_view(request):
    post = Post.objects.get(id=16)
    url = reverse('post_update', kwargs={'pk': post.pk})
    # ...


