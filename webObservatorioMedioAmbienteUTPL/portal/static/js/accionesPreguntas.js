$(document).ready(function(){

 <!-- Script acciones button pregunta 3-->
    $(".P3Año16").on('click', function(){
        $("#P3Año17Esconder").hide();
        $("#P3Año16Esconder").show();

    });
    $(".P3Año17").on('click', function(){
        $("#P3Año17Esconder").show();
        $("#P3Año16Esconder").hide();

    });


});

