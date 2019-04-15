
$( "select" )
  .change(function() {
    var rama = "";
    var grado = "";
    var genero = "";
    var tiempo = "";
    var ciudad = "";
    $( "#select_rama option:selected" ).each(function() {
      rama = $( this ).text();
      console.log(rama);
    });
    $( "#select_grado option:selected" ).each(function() {
      grado = $( this ).text();
      // console.log(grado);
    });
    $( "#select_genero option:selected" ).each(function() {
      genero = $( this ).text();
      // console.log(genero);
    });
    $( "#select_tiempo option:selected" ).each(function() {
      tiempo = $( this ).text();
      // console.log(tiempo);
    });
    $( "#select_ciudad option:selected" ).each(function() {
      ciudad = $( this ).text();
      // console.log(ciudad);
    });

    var data = {
        'rama' : rama,
    };
    $.ajax({
        url : 'buscar_cvs/',
        type : 'POST',
        data : data,
        success : function (json) {
            console.log(json)
        }

    })

  });