$(document).ready(function(){
    
    $('img').hover(function(){
        $(this).attr('src','sky.jpg');
    },function(){
        $(this).attr('src','beach.jpg'); 
    });
});