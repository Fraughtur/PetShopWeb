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


//REGISTRARSE VALIDACION

const Register = document.getElementById('Register');
const username = document.getElementById('UsernameRegister');
const email = document.getElementById('EmailRegister');
const password = document.getElementById('RegisterPassword');
const password2 = document.getElementById('RegisterPasswordValidate');

form.addEventListener('submit', e => {
  e.preventDefault();

  validateInputs();
});

const setError = (element, message) => {
  const inputGroup = element.parentElement;
  const errorDisplay = inputGroup.querySelector('.errorRegister');

  errorDisplay.innerText = message;
  inputGroup.classList.add('error');
  inputGroup.classList.remove('success')
}

const isValidEmail = email => {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
  const usernameValue = username.value.trim();
  const emailValue = email.value.trim();
  const passwordValue = password.value.trim();
  const password2Value = password2.value.trim();

  if(usernameValue === '') {
      setError(username, 'Username es requerido');
  } else {
      setSuccess(username);
  }
};

if(emailValue === '') {
  setError(email, 'Email is required');
} else if (!isValidEmail(emailValue)) {
  setError(email, 'Provide a valid email address');
} else {
  setSuccess(email);
}


if(passwordValue === '') {
  setError(password, 'Password is required');
} else if (passwordValue.length < 8 ) {
  setError(password, 'Password must be at least 8 character.')
} else {
  setSuccess(password);
}

if(password2Value === '') {
  setError(password2, 'Please confirm your password');
} else if (password2Value !== passwordValue) {
  setError(password2, "Passwords doesn't match");
} else {
  setSuccess(password2);
}

