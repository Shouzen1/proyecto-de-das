document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario para validaciones

    const rut = document.getElementById('Rut').value;
    const apellidoPat = document.getElementById('ApellidoPat').value;
    const apellidoMat = document.getElementById('ApellidoMat').value;
    const nombre = document.getElementById('Nombre').value;

    // Validar RUT
    if (!/^\d{0,9}k?$/i.test(rut)) {
        alert('El RUT debe tener un máximo de 10 caracteres y solo puede contener la letra "k".');
        return;
    }

    // Validar Apellido Paterno
    if (/\d/.test(apellidoPat)) {
        alert('El Apellido Paterno no puede contener números.');
        return;
    }

    // Validar Apellido Materno
    if (/\d/.test(apellidoMat)) {
        alert('El Apellido Materno no puede contener números.');
        return;
    }

    // Validar Nombre
    if (/\d/.test(nombre)) {
        alert('El Nombre no puede contener números.');
        return;
    }

    // Si todas las validaciones pasan, se puede enviar el formulario
    alert('Formulario enviado correctamente.');
    this.submit();
});