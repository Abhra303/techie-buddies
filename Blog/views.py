from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Author,Tag
import datetime,random
# Create your views here.

#building the home page of news section
def index(request,index='1'):
    week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    tag = Tag.objects.get(name='Politics')
    blogtag = tag.blogs.all()
    tags = Tag.objects.all()
    pagination = ''
    current_page = int(index)
    limit = 8 * current_page
    offset = limit - 8
    blog_list = Blog.objects.all()[offset:limit]  # limiting contacts based on current_page
    total_blogs = Blog.objects.all().count()  
    total_pages = total_blogs // 8
    if total_blogs % 8 != 0:
        if total_blogs > 8:
            total_pages += 1 # adding one more page if the last page will contains less contacts 
        pagination = make_pagination_html(current_page, total_pages)
    popular_posts = Blog.objects.filter(publish_date__gte=week_ago).order_by('-read')
    return render(request,'Techblog/news.html',{'blogs':blog_list,'popular_posts':popular_posts,'tags':tags,'blogtag':blogtag,'pagination': pagination})

# update the latest post section on the basis of tags
def tagindex(request,value=''):
    blogtag=[]
    if value: 
        tag = Tag.objects.get(name=value)
        allblogs = tag.blogs.all()
        for blog in allblogs:
            if blog.was_published_recently() == True:
                blogtag.append(blog)
    return render(request,'Techblog/newspart.html',{'blogtag':blogtag})

#displaying posts depending on tags
def tagpost(request,name,index='1'):
    tag = Tag.objects.get(name=name)
    tags = Tag.objects.all()
    #for default recent article section
    tag2 = Tag.objects.get(name='Politics')
    blogtag = tag2.blogs.all()
    pagination = ''
    current_page = int(index)
    path = request.path
    if path.find('page')!= -1:
        path = ''
    print(path)
    limit = 8 * current_page
    offset = limit - 8
    blog_list = tag.blogs.all()[offset:limit]  # limiting contacts based on current_page
    total_blogs = tag.blogs.all().count()  
    total_pages = total_blogs // 8
    if total_blogs % 8 != 0:
        if total_blogs > 8:
            total_pages += 1 # adding one more page if the last page will contains less contacts 
        pagination = make_pagination_html(current_page, total_pages,path)
    return render(request,'Techblog/tagpost.html',{'blogs':blog_list,'tags':tags,'blogtag':blogtag,'pagination':pagination})


# algorithm to calculate pagination section

def make_pagination_html(current_page, total_pages,path=''):
    pagination_string = ""
    pagination_string += "<li class='active'>%s</li>"  % (current_page)
    count_limit = 1
    value = current_page - 1
    while value > 0 and count_limit < 5:
        if not path:
            pagination_string = '<li><a href="./page/%s" onclick="if(location.href.search(' %(value) + "'page') != -1){this.href='%s'}" %(value) +'">%s</a></li>' % (value) + pagination_string
        else:
            pagination_string = '<li><a href="..'+ path +'/page/%s" onclick="if(location.href.search(' %(value) + "'page') != -1){this.href='%s'}" %(value) +'">%s</a></li>' % (value) + pagination_string
        value -= 1
        count_limit += 1
    if current_page > 1:
        if not path:
            pagination_string = '<a href="./page/%s"  onclick="if(location.href.search(' %(current_page - 1) +"'page') != -1){this.href='%s'}" %(current_page - 1) +'">←</a>' + pagination_string
        else:
            pagination_string = '<a href="..'+ path +'/page/%s"  onclick="if(location.href.search(' %(current_page - 1) +"'page') != -1){this.href='%s'}" %(current_page - 1) +'">←</a>' + pagination_string
    value = current_page + 1
    while value < total_pages  and count_limit < 10:
        if not path:
            pagination_string =  pagination_string +'<li><a href="./page/%s"  onclick="if(location.href.search(' % (value) + "'page') != -1){this.href='%s'}" %(value) +'">%s</a></li>' % (value)
        else:
            pagination_string =  pagination_string +'<li><a href="..'+ path +'/page/%s"  onclick="if(location.href.search(' % (value) + "'page') != -1){this.href='%s'}" %(value) +'">%s</a></li>' % (value)
        value += 1
        count_limit +=1
    if current_page < total_pages:
        if not path:
            pagination_string += '<a href="./page/%s"  onclick="if(location.href.search(' % (current_page + 1) + "'page') != -1){this.href='%s';console.log(this.href)}"  % (current_page + 1) +'">→</a>'
        else:
            pagination_string += '<a href="..' +path +'/page/%s"  onclick="if(location.href.search(' % (current_page + 1) + "'page') != -1){this.href='%s';console.log(this.href)}"  % (current_page + 1) +'">→</a>'
    return pagination_string


def post(request,val):
    blog = Blog.objects.get(pk = val)
    tags = blog.tags.all()
    num_of_tags = tags.count()
    recommended_blogs = []
    num_of_blogs = 0
    while num_of_blogs < 8 :
        if num_of_tags is 1:
            rand = 0
        elif num_of_tags:
            rand = random.randint(0,num_of_tags -1)
        print(rand)
        print(num_of_tags)
        blogs = tags[rand].blogs.all()
        count_of_blogs = blogs.count()
        if count_of_blogs > num_of_blogs:
            recommended_blogs.append(blogs[num_of_blogs])
        else:
            random1 = 0
            if count_of_blogs is 1:
                random1 = random.randint(0,count_of_blogs)
            else:
                random1 = random.randint(0,count_of_blogs-1)
            recommended_blogs.append(blogs[random1])
        num_of_blogs = num_of_blogs + 1
    if not blog:
        return render(request,'Techblog/error.html')
    return render(request,'Techblog/post.html',{'blog':blog,'recommended':recommended_blogs})


