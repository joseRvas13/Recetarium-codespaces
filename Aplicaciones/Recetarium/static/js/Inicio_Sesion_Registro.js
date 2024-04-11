document.getElementById('crearCuenta').addEventListener('click', function() {
  document.getElementById('formularioInicio').classList.add('formulario-izquierda');
  document.getElementById('formularioRegistro').classList.add('formulario-derecha');
  setTimeout(function() {
      document.getElementById('formularioInicio').style.display = 'none';
      document.getElementById('formularioRegistro').style.display = 'block';
  }, 300);
});

document.getElementById('volverInicio').addEventListener('click', function() {
  document.getElementById('formularioRegistro').classList.remove('formulario-derecha');
  document.getElementById('formularioInicio').classList.remove('formulario-izquierda');
  setTimeout(function() {
      document.getElementById('formularioRegistro').style.display = 'none';
      document.getElementById('formularioInicio').style.display = 'block';
  }, 300);
});
