$(document).ready(function(){
    FiltroInputBuscar();
    FiltroRadioButtons();
  });

function FiltroInputBuscar() {
    $("#search").on("keyup", function() {
      var value = $(this).val().toLowerCase();

      $(".filter").filter(function() {
        $(this).toggle($("h4", this).text().toLowerCase().indexOf(value) > -1);
      });
    });
    $("#search2").on("keyup", function() {
        var value = $(this).val().toLowerCase();

        $(".filter2").filter(function() {
          $(this).toggle($("h4", this).text().toLowerCase().indexOf(value) > -1)
        });
      });
      $("#search3").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".filter3").filter(function() {
          $(this).toggle($("h4", this).text().toLowerCase().indexOf(value) > -1)
        });
      });
}
function FiltroRadioButtons() {
    var $radios = $('input[type="radio"]');
        var $radio_activado = $("#rdo-1").prop('checked',true);
        var $default = $("#rdo-1").filter(':checked');

         $(".oport").filter(function() {
              $(this).toggle($(".oport-search", this).text().indexOf($default.val()) > -1);
            });
      $radios.change(function(){

          var $filtered = $radios.filter(':checked');
            $(".oport").filter(function() {
              $(this).toggle($(".oport-search", this).text().indexOf($filtered.val()) > -1);
            });
      });
}