function validarPasswords(){
    var pass = document.getElementById("clave").value;
    var repass = document.getElementById("repetirClave").value;
    
      if (pass!=repass) 
      {
          alert("Las Contraseñas no coinciden");
      }
      else
      {
          document.getElementById("frm").submit();
      }
    }

const contador = document.getElementById("contador");
const sumarBtn = document.getElementById("sumar");
const restarBtn = document.getElementById("restar");

let count = 1; // Inicializamos el contador en 1

// Función para actualizar el valor del contador en el HTML
function actualizarContador() {
  contador.innerHTML = count;
}

// Función para sumar al contador
function sumar() {
  count++;
  actualizarContador();
}

// Función para restar al contador
function restar() {
  if (count > 1) { // Validamos que el contador no sea menor que 1
    count--;
    actualizarContador();
  }
}

// Event listeners para los botones
sumarBtn.addEventListener("click", sumar);
restarBtn.addEventListener("click", restar);


//Funcion para vaciar el carrito de compra
$(document).on('click', '#BotonEliminar', function(event) {
  event.preventDefault();
  $(this).closest('#Informacioncarrito').remove();
  $("#Articuloscarrito").html("🛒<strong> No tienes</strong> ningun articulo en tu carrito")
  $("#Valortotal").html("<strong>Total:</strong>")
});

//Funcion para dejar un icono en carga de la pagina.
$(window).on('load', function () {
  setTimeout(function () {
$(".loader-page").css({visibility:"hidden",opacity:"0"})
}, 1500);
 
});


$(document).ready(function() {
  setTimeout(function() {
      $(closeModal).fadeOut(11200);
  },3000);

});