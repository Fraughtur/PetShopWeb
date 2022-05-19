   
fetch("https://fraughtur.github.io/abcw/index.json")
.then(Response => {
    return Response.json();})
$.get("https://fraughtur.github.io/abcw/index.json",
function(data){
    $.each(data.products,function(i, item){
        $("#categorias").append('<div class="card" style"width: 18rem;">'+ '<img src="'+item.image+'"class="card-img-top w-100V2" alt="...">'+
            '<div class="card-body">'+'<h5 class="card-title">'+item.name+'</h5>'+ '  <br><br><br>'+
                '<p class="card-text btncategorytext2">'+item.text+'</p>'+
                ' <button class="btn btn-secundary">Mas informacion</button></div>') 
                
                
                })})
                
                
                
              


                 type="text/javascript">
                  $(document).ready(function(){  
                      $("#category2").click(function(){
                          $.get("https://fraughtur.github.io/abcw/index.json",
                          function(data){
                              $.each(data.products2,function(i, item){ 
                                  $("#categorias2").append('<div class="card" style"width: 18rem;">'+ '<img src="'+item.image+'"class="card-img-top w-100V2" alt="...">'+
            '<div class="card-body">'+'<h5 class="card-title">'+item.name+'</h5>'+ '  <br><br><br>'+
                '<p class="card-text btncategorytext2">'+item.text+'</p>'+
                ' <button class="btn btn-secundary">Mas informacion</button></div>')
                              });
                          });
                      });
                  })
            
              
               type="text/javascript">
                $(document).ready(function(){  
                    $("#category3").click(function(){
                        $.get("https://fraughtur.github.io/abcw/index.json",
                        function(data){
                            $.each(data.products3,function(i, item){ 
                                $("#categorias3").append('<div class="card" style"width: 18rem;">'+ '<img src="'+item.image+'"class="card-img-top w-100V2" alt="...">'+
          '<div class="card-body">'+'<h5 class="card-title">'+item.name+'</h5>'+ '  <br><br><br>'+
              '<p class="card-text btncategorytext2">'+item.text+'</p>'+
              ' <button class="btn btn-secundary">Mas informacion</button></div>')
                            });
                        });
                    });
                })

                   

