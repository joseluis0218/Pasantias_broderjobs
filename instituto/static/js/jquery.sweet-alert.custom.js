
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


    //Parameter
    $('.sa-params').click(function(){

const swalWithBootstrapButtons = Swal.mixin({
  confirmButtonClass: 'btn btn-danger',
  cancelButtonClass: 'btn btn-default',
  buttonsStyling: false,
});

swalWithBootstrapButtons.fire({
  title: '¿Esta seguro de eliminar este usuario?',
  text: "No podrás revertir esta acción",
  type: 'warning',
  showCancelButton: true,
  cancelButtonText: 'No, cancelar!',
  confirmButtonText: 'Si, eliminar!',
}).then((result) => {
  if (result.value) {
    swalWithBootstrapButtons.fire(
      'Eliminado!',
      'El usuario ha sido eliminado correctamente',
      'success',
    );
  }
})
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