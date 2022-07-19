jQuery(document).ready(function(){
    jQuery("#contact").validate({
        rules:{
            full_name:"required",
            email:"required",
           

        },
        messages:{
            full_name:"Please Enter Your Full Name.",
            email:"Please Enter An Email.",
    
        },
        
});
    jQuery('.testrow').slick({
        slidesToShow: 3,
        slidesToScroll:3,
        autoplay:true,
        pauseOnHover:false,

    });
    jQuery('.brands_row').slick({
        slidesToShow: 4,
        slidesToScroll:1,
        autoplay:true,
        pauseOnHover:false,

    });
});



  
  