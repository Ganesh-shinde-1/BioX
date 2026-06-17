from django.shortcuts import render , redirect , get_object_or_404
from .models import Research, Blog ,News  , AboutUs , ContactMessage , Post , Site_Active_models , ExamCategory  ,Exam , AdmitCard , Result
from django.shortcuts import render, get_object_or_404




def error_400(request, exception):
    return render(request, "400.html", status=400)


def error_403(request, exception):
    return render(request, "403.html", status=403)


def error_404(request, exception):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)







def home(request):
    activations =Site_Active_models.objects.filter().first()

    if activations.home ==False :
        return render(request, 'maintan.html')


    posts = Post.objects.filter(active=True).order_by('-publish')[:3]

    news = News.objects.filter(active=True).order_by('-date')[:3]

    exam_updates = Exam.objects.filter(active=True).order_by('-created_at')[:3]

    research = Research.objects.filter(active=True).order_by('-published_date')[:3]

    blogs = Blog.objects.filter(active=True).order_by('-date_of_publish')[:3]
    about = AboutUs.objects.filter(active=True).first()



    context = {
        'posts': posts,
        'news': news,
        'updates': exam_updates,
        'researches': research,
        'blogs': blogs, 
        'about':about
    }

    return render(request, 'index.html', context)



def posts(request, slug=None):
    activations = Site_Active_models.objects.first()

    if not activations.reasearch:
        return render(request, 'maintan.html')

    researches = Post.objects.filter(
        active=True
    ).order_by('-publish')

    # Latest blog if no slug provided
    if slug:
        selected_blog = get_object_or_404(
            Post,
            slug=slug,
            active=True
        )
    else:
        selected_blog = researches.first()

    about = AboutUs.objects.filter(active=True).first()

    context = {
        'selected_blog': selected_blog,
        'posts': researches,
        'about': about,
    }

    return render(request, 'post.html', context)




def about(request):
    activations =Site_Active_models.objects.filter().first()

    if activations.about  ==False :
        return render(request, 'maintan.html')

    about = AboutUs.objects.filter(active=True).first()

    return render(request, 'about.html', {'about': about})




def blogs(request, slug=None):
    activations = Site_Active_models.objects.first()

    if not activations.reasearch:
        return render(request, 'maintan.html')

    researches = Blog.objects.filter(
        active=True
    ).order_by('-created_at')

    # Latest blog if no slug provided
    if slug:
        selected_blog = get_object_or_404(
            Blog,
            slug=slug,
            active=True
        )
    else:
        selected_blog = researches.first()

    about = AboutUs.objects.filter(active=True).first()

    context = {
        'selected_blog': selected_blog,
        'blogs': researches,
        'about': about,
    }


    return render(request, 'blog.html', context)



def news(request , slug=None):
    activations = Site_Active_models.objects.first()

    if not activations.reasearch:
        return render(request, 'maintan.html')

    researches = News.objects.filter(
        active=True
    ).order_by('-created_at')

    # Latest blog if no slug provided
    if slug:
        selected_blog = get_object_or_404(
            News,
            slug=slug,
            active=True
        )
    else:
        selected_blog = researches.first()

    about = AboutUs.objects.filter(active=True).first()

    context = {
        'selected_blog': selected_blog,
        'blogs': researches,
        'about': about,
    }



    return render(request, 'news.html', context)






def contact(request):
    activations =Site_Active_models.objects.filter().first()

    if activations.contanct  ==False :
        return render(request, 'maintan.html')
    contact = AboutUs.objects.filter(active=True).first()
    about = AboutUs.objects.filter(active=True).first()
    
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('contact')

    return render(request, 'contact.html' , {'contact': contact, 'about':about})

# def research(request):
#     activations =Site_Active_models.objects.filter().first()

#     if activations.reasearch  ==False :
#         return render(request, 'maintan.html')
#     researches = Research.objects.filter(active=True).order_by('-published_date')
#     about = AboutUs.objects.filter(active=True).first()

#     context = {
#         'researches': researches,
#         'about':about
#     }

#     return render(request, 'research.html', context)



def research(request, slug=None):
    activations = Site_Active_models.objects.first()

    if not activations.reasearch:
        return render(request, 'maintan.html')

    researches = Research.objects.filter(
        active=True
    ).order_by('-published_date')

    # Latest blog if no slug provided
    if slug:
        selected_blog = get_object_or_404(
            Research,
            slug=slug,
            active=True
        )
    else:
        selected_blog = researches.first()

    about = AboutUs.objects.filter(active=True).first()

    context = {
        'selected_blog': selected_blog,
        'researches': researches,
        'about': about,
    }

    return render(request, 'research.html', context)






def exams(request):

    activations = Site_Active_models.objects.first()
    if activations and not activations.update:
        return render(request, 'maintan.html')


    categories = ExamCategory.objects.filter(
        active=True
    ).order_by('name')

    exams = Exam.objects.filter(
        active=True
    ).select_related(
        'category'
    ).order_by('-created_at')

    admit_cards = AdmitCard.objects.filter(
        active=True
    ).order_by('-created_at')

    results = Result.objects.filter(
        active=True
    ).order_by('-created_at')

    context = {
        'categories': categories,
        'exams': exams,
        'admit_cards': admit_cards,
        'results': results,
    }

    return render(
        request,
        'exam.html',
        context
    )


def exam_list(request, category):
    activations = Site_Active_models.objects.first()
    if activations and not activations.update:
        return render(request, 'maintan.html')


    category = get_object_or_404(
        ExamCategory,
        name=category,
        active=True
    )

    categories = ExamCategory.objects.filter(
        active=True
    ).order_by('name')


    exams = Exam.objects.filter(
        category=category,
        active=True
    ).order_by('-created_at')

    context = {
        'category': category,
        'categories':categories,
        'category':category,
        'exams': exams,
    }

    return render(
        request,
        'exam_list.html',
        context
    )


def exam_detail(request, slug):

    activations = Site_Active_models.objects.first()
    if activations and not activations.update:
        return render(request, 'maintan.html')

    exam = get_object_or_404(
        Exam,
        slug=slug,
        active=True
    )

    categories = ExamCategory.objects.filter(
        active=True
    ).order_by('name')

    related_exams = Exam.objects.filter(
        category=exam.category,
        active=True
    ).exclude(
        id=exam.id
    )[:10]

    context = {
        'exam': exam,
        'category':categories,
        'related_exams': related_exams,
    }

    return render(
        request,
        'exam_detail.html',
        context
    )



