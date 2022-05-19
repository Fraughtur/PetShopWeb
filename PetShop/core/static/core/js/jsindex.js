//Contraseña
 document
  .getElementById('contraseña')
  .addEventListener('input', function(evt) {
    const contraseña = evt.target,
          valido = document.getElementById('contraseñaOK'),
        
          alfanum = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/;

    //Se muestra un texto válido/inválido a modo de ejemplo
    if (alfanum.test(contraseña.value)) {
      valido.innerText = "válido";
    } else {
      valido.innerText = "incorrecto";
    }
  });


  //CHECK BOX -- GUARDAR CONTRASEÑA

const guardarSwitch = document.querySelector('#switch input[type="checkbox"]');
          function guardarContraseña(ev){
              if(ev.target.checked){
                  document.documentElement.setAttribute('tema', 'light');
              } else {
                  document.documentElement.setAttribute('tema', 'dark');
              }
          }
          guardarSwitch.addEventListener('change', guardarContraseña);



          
          
