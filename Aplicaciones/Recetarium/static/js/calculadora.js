// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('imc-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar que el formulario se envíe por defecto

        var estatura = parseFloat(document.getElementById('Estatura').value);
        var peso = parseFloat(document.getElementById('Peso').value);

        if (!isNaN(estatura) && !isNaN(peso)) {
            // Realizar solicitud AJAX a la vista de Django
            var formData = new FormData();
            formData.append('estatura', estatura);
            formData.append('peso', peso);

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/calcular_imc/', true);

            xhr.onload = function() {
                if (xhr.status === 200) {
                    var resultado = JSON.parse(xhr.responseText);
                    var resultadoElement = document.getElementById('resultado-imc');
                    resultadoElement.innerHTML = '<h2>Resultado del IMC:</h2><p>Tu IMC es ' + resultado.imc.toFixed(2) + '</p>';
                } else {
                    alert('Hubo un problema al calcular el IMC. Inténtalo de nuevo más tarde.');
                }
            };

            xhr.onerror = function() {
                alert('Hubo un error de red al calcular el IMC. Inténtalo de nuevo más tarde.');
            };

            xhr.send(formData);
        } else {
            alert('Por favor ingresa números válidos para estatura y peso.');
        }
    });
});
