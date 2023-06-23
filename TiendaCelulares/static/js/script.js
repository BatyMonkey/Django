document.getElementById("icon-menu").addEventListener("click", mostrar_menu);

function mostrar_menu() {
  document.getElementById("move-content").classList.toggle("move-container-x");
  document.getElementById("show-menu").classList.toggle("show-lateral");
}

$(function () {
  var Page = (function () {
    var $navArrows = $("#nav-arrows").hide(),
      $shadow = $("#shadow").hide(),
      slicebox = $("#sb-slider").slicebox({
        onReady: function () {
          $navArrows.show();
          $shadow.show();
        },
        orientation: "r",
        cuboidsRandom: true,
        disperseFactor: 30,
      }),
      init = function () {
        initEvents();
      },
      initEvents = function () {
        // add navigation events
        $navArrows.children(":first").on("click", function () {
          slicebox.next();
          return false;
        });

        $navArrows.children(":last").on("click", function () {
          slicebox.previous();
          return false;
        });
      };

    return {
      init: init,
    };
  })();

  Page.init();
});

$("#formulario1").validate({
  rules: {
    username: {
      required: true,
      minlength: 4,
      maxlength: 15,
    },
    nombres: {
      required: true,
      minlength: 4,
    },
    apellido: {
      required: true,
      minlength: 4,
    },
    email: {
      required: true,
      minlength: 8,
      email: true,
    },
    password1: {
      required: true,
      minlength: 4,
    },
    password2: {
      required: true,
      equalTo: "#id_password1",
    },
  },
  messages: {
    username: {
      required: "Ingrese un Nombre de usuario",
      minlength: "Debe tener un mínimo de 4 caracteres",
      maxlength: "Debe tener un máximo de 15 caracteres",
    },
    nombres: {
      required: "Ingrese su Nombre",
      minlength: "Debe tener un mínimo de 4 caracteres",
    },
    apellido: {
      required: "Ingrese su Apellido",
      minlength: "Debe tener un mínimo de 4 caracteres",
    },
    email: {
      required: "Ingrese su Email",
      minlength: "El email debe tener un mínimo de 8 caracteres",
      email: "El formato de email es: ejemplo@gmail.com",
    },
    password1: {
      required: "Ingrese su Contraseña",
      minlength: "Mínimo 4 caracteres",
    },
    password2: {
      required: "Repita la Contraseña",
      equalTo: "Las contraseñas deben ser iguales",
    },
  },
});

function confirmation() {
  if (confirm("¿Realmente desea eliminar?")) {
    return true;
  }
  return false;
}
