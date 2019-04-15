$(document).ready(function()
{
    enviar_ajax();
    estado_empresa();
    enviar_calificacion_ajax();
    calificacion_estudiante();
    visualizar_cv();
});
function enviar_ajax() {

$(".checkbox").on( 'change', function() {
    var valor_id = $(this).attr("id");
    // console.log(valor_id);
    if( $(this).is(':checked') ) {
        $('#modalActivacion').modal("show");
        $("#confirmacion").on('click',function () {
            $.ajax({
            url: "cambiar_estado/"+valor_id,
            type: 'POST',
        });
        });
        $("#cancelar").on('click',function () {
            $(".checkbox").attr('checked',false);
        });
    } else {
         $('#modalDesactivacion').modal("show");

         $("#confirmacion2").on('click',function () {
            $.ajax({
            url: "cambiar_estado/"+valor_id,
            type: 'POST',
        });
         });
         $("#cancelar2").on('click',function () {
            location.reload();
        });
    }
});
}
function estado_empresa() {

        $("input").each(function () {
        var valor_id = $(this).attr("id");
/*        console.log(valor_id);*/

        var id = "#".concat(valor_id);
        var valor = $(id).val();
/*        console.log(valor);*/
         if(valor === 'A'){
            $(id).attr('checked',true);

        }else {
             $(id).attr('checked', false);

         }
        });

    }
    
// function calificacion_estudiante() {
//
//     $("input").each(function () {
//         var valor_id = $(this).attr("id");
//         console.log(valor_id);
//         var id = "#".concat(valor_id);
//         var valor = $(id).val();
//          console.log(valor);
// var oblig = $('input:radio[name=customRadio]').attr('checked', true);
// oblig.filter('[value='+valor_id+']').attr('checked', true);
//          if(valor === 'MB'){
//
//          }
//     })
//
// }

function enviar_calificacion_ajax() {
    $("input[name=radio-hide]").each(function () {
         var identificador = $(this).attr("id");
        console.log(identificador);

    $("input[name=customRadio"+identificador+"]").on( 'change', function() {

        var valor_id = $(this).attr("id");
         // console.log(valor_id);

         var valor = $(this).val();
         // console.log(valor);

    if( $(this).is(':checked') ) {

        $.ajax({
            url: "/oportunidad/calificar/"+valor_id+"/"+valor,
            type: 'POST',
        });
    }
});
});

}

function calificacion_estudiante() {

    $("input[name=radio-hide]").each(function () {
        var valor_id = $(this).attr("id");
        // console.log(valor_id);

        var id = "#".concat(valor_id);
        // console.log(id);
        var valor = $(id).val();
        // console.log(valor);

        if(valor === 'MB'){
            $("input[id ="+valor_id+"]").filter('[value=1]').attr('checked', true);

        }else if(valor === 'B'){
            $("input[id ="+valor_id+ " ]").filter('[value=2]').attr('checked', true);

        }else if(valor === 'R'){
            $("input[id ="+valor_id+ " ]").filter('[value=3]').attr('checked', true);

        }
        });
}

function visualizar_cv() {


            $("input[name=radio-hide]").each(function () {
                var identificador = $(this).attr("id");
                // console.log(identificador);

                $(".ver-cv").on('click',function () {
                    // alert("hola");
                //     $.ajax({
                //     url: "/oportunidad/ver_cv/6",
                //     type: 'POST',
                //
                // });
            });

    });
}