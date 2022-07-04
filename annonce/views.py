
from site import USER_SITE
from django.shortcuts import render,redirect
from acceuil.models import Clients
from annonce.models import Annonces
from .forms import Annonces_Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

# Create your views here.

def annonce(request):
    annonce = Annonces.objects.all()
    
    return render(request,'annonces.html',{'annonce':annonce})


def menu_annonces(request,element_annonce):
    annonce = Annonces.objects.filter(A_type__icontains=element_annonce)
  
    return render(request,'filter_annonce.html',{'annonce':annonce})


def details_annonce (request,id):
    id_annonce = Annonces.objects.get(id=id)
    vendeur_nom = id_annonce.vendeur. nomclient
    vendeur_prenom = id_annonce.vendeur.prenomclient
    vendeur_email = id_annonce.vendeur.emailclient
    vendeur_numero = id_annonce.vendeur.numero
    vendeur_profil = id_annonce.vendeur.profil

    return render(request,'details_annonce.html',{'id_annonce':id_annonce,'vendeur_nom':vendeur_nom,
    
    'vendeur_prenom':vendeur_prenom,'vendeur_email':vendeur_email,'vendeur_numero':vendeur_numero,'vendeur_profil':vendeur_profil,
    })

def recherche_annonce(request):
    mot = request.GET['mot_annonce']
    
    trouver_annonce = Annonces.objects.filter(desi_annonce__icontains=mot)
   
    return render(request,'recherche_annonce.html',{'trouver':trouver_annonce,'mot':mot})

def ajout_annonce(request):
    if request.method =='POST':
        form = Annonces_Form(request.POST,request.FILES)
        try:
            user_connect = request.user
            user_info = Clients.objects.get(nomutilisateur=user_connect)
            numero_connect = user_info.numero
            email_connect = user_connect.email
            EA = Annonces()   #EA enregistrement des annonces
            EA.numero = numero_connect
            EA.email_vendeur = email_connect
            EA. vendeur = user_info
            EA.desi_annonce = request.POST['desi_annonce']
            EA.prix_annonce = request.POST['prix_annonce']
            EA.nature = request.POST['nature']
            EA.A_type = request.POST['A_type']
        
            EA.desc_annonce = request.POST['desc_annonce']
            EA_attendant = form.save(commit=False) #Permet de creer un model intermediaire pour l'insertion des donneés
            EA_attendant.numero_vendeur = numero_connect
            EA_attendant.vendeur = user_info
            form.save()
            return redirect('annonce')
        except:
            form = Annonces_Form()



        
    else:
        form= Annonces_Form()
    return render(request,'ajout_annonce.html',{'form':Annonces_Form})