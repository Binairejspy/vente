$(function(){
   
    var contenu = $('.contenu');
    jQuery.fx.speeds.slow = 4000;
    contenu.hide('slow');
    var menu = $('.nav-link');
    var close = $('.close');
    close.hide()
    var article = $('.article')
    $(menu).each(function(){
       
        $(this).on('click',function(){
            
            
            $(this).addClass('active');
            $(menu).not(this).removeClass('active');/*not(this) permet de recuperer 
            les elements qui n'ont pas été cliqué*/

           
        })

    })
    if($(location).attr('href')=='http://127.0.0.1:8000/annonces'){
        $('.annonce').css('color','red');
    }
    if($(location).attr('href')=='http://127.0.0.1:8000/apropos'){
        $('.apropos').css('color','red');
    }
    if($(location).attr('href')=='http://127.0.0.1:8000/contact'){
        $('.contact').css('color','red');
    }
    if($(location).attr('href')=='http://127.0.0.1:8000/boutique'){
        $('.boutique').css('color','red');
    }
    if($(location).attr('href')=='http://127.0.0.1:8000/#'){
        $('.acceuil').css('color','red');
        
    }
    
    if($(location).attr('href')=='http://127.0.0.1:8000/index'){
        $('.acceuil').css('color','red');
    }
    if($(location).attr('href')=='http://127.0.0.1:8000/freelance'){
        $('.freelance').css('color','red');
    }
   
   
    
var wwidth=$(window).width()
if(wwidth>=1236){
    article.mouseenter(function(){
        contenu.removeClass('cacher');
        
        
    })
   /* article.on('click',function(e){
        e.preventDefault()
       
        close.removeClass('closechacher');
        close.show()
        contenu.show();
        let  idrecup = $(this).attr('id')
        let img = $(this).attr('image')
        let img_detail=$('.img-detail').attr('src',img)
       

    })
    
    close.on('click',function(){
        contenu.hide()
        close.hide()
    })*/
} 



$('.inscription').on('click',function(){
   
    var nom=$('.nom').val()
    var prenom=$('.prenom').val()
    var email=$('.email').val()
    var motdepasse =$('.password').val()
    var confpasse = $('.Conpassword').val()
    var username = $('.username').val()
    $('.error').remove()
    if(nom==''){
        
       $('.nom').before('<p class="error" style="color:red">Donner un nom </p>')
       return false
    }
     else if (prenom =='') {
        $('.prenom').before('<p class="error" style="color:red">Donner prenom </p>')
       return false
    }
       else if (username=='') {
        $('.username').before('<p class="error" style="color:red">Donner un d\'utilisateur </p>')
        return false
    
    } else if (email=='') {
        $('.email').before('<p class="error" style="color:red">Donner votre email </p>')
        return false
    } else if (motdepasse=='') {
        $('.password').before('<p class="error" style="color:red">Donner un mot de passe </p>')
       return false
    }
    else if (confpasse=='') {
        $('.Conpassword').before('<p class="error" style="color:red">Donner un mot de passe de confirmation </p>')
        return false
}else if (confpasse=='') {
    $('.numero').before('<p class="error" style="color:red">Donner votre numero de telephone</p>')
    return false
}
     else {
        
    }
  

})

$('.ajout-commande').on('click',function(){
    var id = $(this).attr('a_id')
    $.ajax({
        url:'ajout_commande/',
        type:'GET',
        data:{
            id_a:id
        },
        success:function(data){
            $('.ajoute').html('<span class="ajoute text-center bg-primary text-white"> Vous avez ajouter un produit dans votre panier</span>')
        },
        error:function(){
            $('.ajoute').html('<span class="bg-danger text-center text-white">une erreur connecter vous pour pouvoir ajouter des produits dans votre pannier</span>')
        }
        

        
    })
})


})