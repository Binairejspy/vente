
from signal import pthread_kill
from django.db.models import *
from acceuil.views import apropos
from django.shortcuts import render,HttpResponse,redirect
from .models import *

def boutique(request):
    touts = Article.objects.all()
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    
    return render(request,'boutique.html',{'ts':touts,'nbr':nombre_les_commande_commendeur})

def chemise(request):
    chemise = Article.objects.filter(Type__icontains='chemise')
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    return render(request,'chemise.html',{'chemise':chemise,'nbr':nombre_les_commande_commendeur})
    
def chaussures(request):
    chaussure = Article.objects.filter(Type__icontains='chaussure')
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    return render(request,'chaussure.html',{'chaussure':chaussure,'nbr':nombre_les_commande_commendeur})

def Veste(request):
    veste = Article.objects.filter(Type__icontains='vetement')
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    return render(request,'veste.html',{'veste':veste,'nbr':nombre_les_commande_commendeur})

def telephone(request):
    telephone = Article.objects.filter(Type__icontains='telephone')
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    return render(request,'telephone.html',{'telephone':telephone,'nbr':nombre_les_commande_commendeur})

def ordinateur(request):
    ordinateur = Article.objects.filter(Type__icontains='ordinateur')
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    return render(request,'ordinateur.html',{'ordinateur':ordinateur,'nbr':nombre_les_commande_commendeur})

def voiture(request):
    voitures = Article.objects.filter(Type__icontains='voiture')
    return render(request,'voiture.html',{'voiture':voitures})



def details(request,id):
    pointe = Article.objects.get(id=id)
    return render(request,'details.html',{'pointe':pointe})



def recherche(request):
    mot = request.GET['mots']
    trouver = Article.objects.filter(designation__icontains=mot)
    try:
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)

        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        nombre_les_commande_commendeur = len(tout_commande_commendeur)
    except:
        nombre_les_commande_commendeur = 0
    return render(request,'recherche.html',{'trouver':trouver,'mot':mot,'nbr':nombre_les_commande_commendeur})




def ajout_commande(request):
    if request.method == 'GET':
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)
        
        id = request.GET['id_a']
        article_correspondant = Article.objects.get(id=id)
        cmmd = commandes()
        cmmd.nomusercommande = renseignement_commendeur
        cmmd.nomproduitcommande = article_correspondant
        cmmd.save()

        
    return HttpResponse('hello')


def panier(request):
    commendeur = request.user
    renseignement = Clients.objects.get(nomutilisateur = commendeur)
    tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement.id)
    if tout_commande_commendeur:
        pass
    else:
       
        return redirect('boutique',)
    
    total = 0
    for i in tout_commande_commendeur:
        total = i.nomproduitcommande.prix + total
    


    return render(request,'panier.html',{'tsc':tout_commande_commendeur,'total':total})


def suppression(request,id):
    commandes.objects.get(id=id).delete()
    return redirect('panier')


def all_commande(request):
    
    user = request.user
    renseignement = Clients.objects.get(nomutilisateur = user)
    tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement.id)
    for i in tout_commande_commendeur:
        cmmd= commandes_alls()
        cmmd.nomusercommande_all = renseignement
        cmmd.id_produit = i.nomproduitcommande_id
        cmmd.save()
    for i in commandes_alls.objects.all():
        print(i.nomusercommande_all.nomutilisateur)
        les_commandes = Article.objects.filter(id = i.id_produit)
        print(les_commandes)

   
    tout_commande_commendeur.delete()
    return render(request,'felicitation.html')

def one_commande(request,id):
    user = request.user
    renseignement = Clients.objects.get(nomutilisateur = user)
    cmmd = commandes_alls()
    cmmd.nomusercommande_all = renseignement
    cmmd.id_produit = id
    cmmd.save()
    for i in commandes_alls.objects.all():
        print(i.nomusercommande_all.nomutilisateur)
        les_commandes = Article.objects.filter(id = i.id_produit)
        print(les_commandes)

    return render(request,'felicitation.html')