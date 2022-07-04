from email import message
from django.shortcuts import redirect, render

from boutique.models import Article  

from annonce.models import Annonces
from .models import *

# Create your views here.
def index(request):
    article =Article.objects.order_by('-id')[:6]
    annonce = Annonces.objects.all().order_by('-id')[:4]
    #free_concept = concepts_freelance.objects.order_by('-id')[:4]
    touts = Article.objects.all()[:20]
    
        
    return render(request,'index.html',{'article':article,'annonce':annonce,'ts':touts})


def apropos(request):
    

    return render(request,'apropos.html')


def contact(request):
    info=''
    if request.method=='POST':
       nom_commenteur =request.POST['name']
       message_commenteur = request.POST['message']
       cmmenteur = commenteur()
       cmmenteur.posteur=nom_commenteur
       cmmenteur.message=message
       cmmenteur.save()
       info = 'Votre commenteur  est bien reussi merci 😄😄😄 🤝🤝🤝 👍👍👍'
    else:
       redirect('contact')

    return render(request,'contact.html',{'info':info})

def help(request):
    return render(request,'help.html')