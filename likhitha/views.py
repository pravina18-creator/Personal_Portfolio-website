from django.shortcuts import render
from .models import Home,About,Profile,Category,Skills,Portfolio

# Create your views here.
def index(request):

    #home
    home= Home.objects.latest('updated')
    #about 
    about=About.objects.latest('updated')
    profiles=Profile.objects.filter(about=about)

    #skills
    categories=Category.objects.all()

    #portfolio
    portfolios=Portfolio.objects.all()


    context={
        'home':home,
        'about':about,
        'profiles':profiles,
        'categories':categories,
        'portfolios':portfolios,
    }

    return render(request, 'index.html',context)
