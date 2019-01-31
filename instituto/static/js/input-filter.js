$(document).ready(function(){
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

      var $radios = $('input[type="radio"]');
      $radios.change(function(){
          var $filtered = $radios.filter(':checked');
         
            console.log($filtered.val());
            $(".oport").filter(function() {
              $(this).toggle($(".oport-search", this).text().indexOf($filtered.val()) > -1);
            }); 
      });
  });

