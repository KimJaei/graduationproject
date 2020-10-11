from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def index(request):
    return render(request, 'index.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)   # 첫번째 인자는 어떤 클래스로부터 객체를 받을지, 두번째는 검색조건(pk)
    return render(request, 'detail.html', {'details':details})

# new.html 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()   # 쿼리셋 메소드 중 하나. 위의 객체를 데이터베이스에 저장해라. ex) 객체.delete : ~?
    return redirect ('/blog/' + str(blog.id))

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():   # 잘 입력되었는지 확인
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('notice')
            
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def notice(request):
    blogs = Blog.objects   # 쿼리셋
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 7)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'notice.html', {'blogs':blogs, 'posts':posts})

def result(request):
    posts = Blog.objects.all()
    query = request.GET.get('query')
    if query:
        posts = posts.filter(title__icontains=query)
    return render(request, 'result.html', {'posts':posts})