
!function($) {
    "use strict";

    var SweetAlert = function() {};

    //examples 
    SweetAlert.prototype.init = function() {
        
    //Basic
    $('#sa-basic').click(function(){
        swal("Here's a message!");
    });

    //A title with a text under
    $('#sa-title').click(function(){
        swal("Here's a message!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat eleifend ex semper, lobortis purus sed.")
    });

    //Success Message
    $('#sa-success').click(function(){
        swal("Good job!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat eleifend ex semper, lobortis purus sed.", "success")
    });

    //Warning Message
    $('#sa-warning').click(function(){
        swal({   
            title: "¿Estas seguro?",   
            text: "¡Este usuario se eliminará definitivamente!",   
            type: "warning", 
            showCancelButton: true,  
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Si, elimínalo!",   
            closeOnConfirm: false 
        }, function(){   
            swal("Eliminado!", "Your imaginary file has been deleted.", "success"); 
        });
    });

    //Parameter
    $('.sa-params').click(function(){
        swal({   
            title: "¿Está seguro?",   
            text: "¡Este usuario se eliminará definitivamente!",   
            type: "warning",   
            showCancelButton: true,   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Si, elimínalo!",   
            cancelButtonText: "No, cancelar!",   
            closeOnConfirm: false,   
            closeOnCancel: false 
        }, function(isConfirm){   
            if (isConfirm) {     
                swal("Eliminado!", "El usuario ha sido eliminado correctamente.", "success");   
            } else {     
                swal("Cancelled", "Registro no eliminado.", "error");   
            } 
        });
    });

    //Custom Image
    $('#sa-image').click(function(){
        swal({   
            title: "Govinda!",   
            text: "Recently joined twitter",   
            imageUrl: "../assets/images/users/profile.png" 
        });
    });

    //Auto Close Timer
    $('#sa-close').click(function(){
         swal({   
            title: "Auto close alert!",   
            text: "I will close in 2 seconds.",   
            timer: 2000,   
            showConfirmButton: false 
        });
    });


    },
    //init
    $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.SweetAlert.init()
}(window.jQuery);