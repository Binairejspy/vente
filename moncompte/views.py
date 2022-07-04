from django.shortcuts import redirect, render
from acceuil.models import *
from annonce.models import *

# Create your views here.

def moncompte(request):
    user_connect =request.user
    try:
        info_user = Clients.objects.get(nomutilisateur=user_connect)
        
        concept_user= concepts_freelance.objects.filter(nomfreelance_id=info_user.id)
        annonce_user=Annonces.objects.filter(vendeur_id=info_user.id)
        print(annonce_user)
    except:
        return redirect('connexion')

   
    return render(request,'moncompte.html',{'info':info_user,'concept':concept_user,'annonce_user':annonce_user})