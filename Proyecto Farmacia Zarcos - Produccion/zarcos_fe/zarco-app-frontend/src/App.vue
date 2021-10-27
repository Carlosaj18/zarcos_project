<template>
  <div id="app" class="app">
    <div class="header">
      <img id="logo" src="./assets/imgs/logoFarmaciaGral.png" />
      <h1>Farmacia Zarcos</h1>
      <nav class="navbar navbar-green bg-green px-3">
        <!-- En lugar de ser una página totalmente estática, sea una página dinámica que se construya 
        y modifique a partir de ciertos eventos y valores-->
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth" v-on:click="loadEventos">Eventos</button>
        <!--<button v-if="is_auth">Personas</button>-->
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>

        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
        <!-- <button v-if="!is_auth" > Buscar categoria </button> -->
      </nav>
    </div>

    <!-- Que esta haciendo los componentes del main? -->
    <div class="main-component" style="overflow-y:auto;">
      <!-- Me permite enrutar las vistas de login y signup, es un visualizador 
          y en ese espacio me puede colocar el resultado de esa redireccion del router y carga el 
          componente. Lo anterior pasa a partir de la funcion de JS que se complete
          A través del elemento Router se facilita el manejo de la URL y  permite 
          cargar de manera dinámica el componente correspondiente a la URL actual de la aplicación-->
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <footer>
      <div class="container-footer-all">
        <div class="container-body">
          <div class="colum1">
            <h1>Mas informacion de la compañia</h1>
            <p>
              Somos una compañía que ofrece los servicios de Farmacia, además de
              organizar eventos relacionados con el campo de la salud. Nos
              sentimos orgullosos de poder brindar a nuestros residentes y
              visitantes una experiencia unica, mientras que pueden agendarse a
              nuestra programación de eventos, con los cuales podrá fortalecer
              su experiencia con nosotros.
            </p>
          </div>
          <div class="colum2">
            <h1>Redes Sociales</h1>
            <div class="row">
              <img src="./assets/imgs/facebook.png" /><label
                >Siguenos en Facebook</label
              >
            </div>
            <div class="row">
              <img src="./assets/imgs/twitter.png" /><label
                >Siguenos en Twitter</label
              >
            </div>
            <div class="row">
              <img src="./assets/imgs/instagram.png" /><label
                >Siguenos en Instagram</label
              >
            </div>
            <div class="row">
              <img src="./assets/imgs/pinterest.png" /><label
                >Siguenos en Pinterest</label
              >
            </div>
          </div>
          <div class="colum3">
            <h1>Informacion Contactos</h1>
            <div class="row2">
              <img src="./assets/imgs/house.png" />
              <label
                >Avenida Los Rosales # 245 - 16 of. 302 Edificio Mutantes -
                Bogotá, República de Colombia</label
              >
            </div>
            <div class="row2">
              <img src="./assets/imgs/smartphone.png" /><label
                >(60) 300 555 5555</label
              >
            </div>
            <div class="row2">
              <img src="./assets/imgs/contact.png" /><label
                >farmaciazarcos_clientes@zarcos.com</label
              >
            </div>
          </div>
        </div>
      </div>
      <div class="container-footer">
        <div class="footer">
          <div class="copyright">
            © 2021 Todos los Derechos Reservados |
            <a
              class="a-style"
              @click="linkDownload('https://www.misiontic2022.gov.co/portal/')"
            >
              Misión Tic 2022</a
            >
          </div>
          <div class="information">
            <a href="">Informacion Compañia</a> |
            <a href="">Privacion y Politica</a> |
            <a href="">Terminos y Condiciones</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
/** se exporta el objeto que define por medio de llaves/valores, 
        los atributos y métodos del componente. Se asinga a una cadena
        el nombre del componente, y este nombre sera usado por otros componentes*/
export default {
  name: "App",

  data: function() {
    /** Se asigna una función que retorna un objeto, cuyas llaves son el nombre de la variable, 
      y los valores son el valor que se da a cada una de ellas. Estas pueden ser usadas 
      por cualquier parte del componente en sus funciones o en el codigo HTML.
     * Aqui se carga la data que necesito para correr se puede poner un valor por defecto
     * Se pueden poner todas las variables que se necesiten inicializar antes de la carga
     * Se puede usar data que se extrae de un sitio web
    */
    return {
      is_auth: false,
    };
  },

  components: {},

  methods: {
    /** Se asigna un objeto. La llaves de este objeto representan el nombre de las 
      funciones, y sus valores contienen la definición de cada función del componente
     * Todo lo que sea funcion de JS se van a poner aqui
     *  Cada funcion se separa por una coma ya que cada una es un elemento
     * Los metodos completedLogIn y completedSignUp usan el parametro de data anteriormente descrito 
     */
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false)
        /** Router Push permite cambiar la URL de la aplicación desde el script de un componente, esto resulta útil 
    cuando se desea cambiar de componentes debido a algún evento ocurrido dentro de la aplicación */
        this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "home" });
    },
    loadLogIn: function() {
      /** Accedo al router y cuando den click pongo a andar lo que este en login*/
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function() {
      this.$router.push({ name: "signUp" });
    },
    loadHome: function() {
      this.$router.push({ name: "home" });
    },
    logOut: function() {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },
    loadEventos: function() {
      console.log("Se abre la nueva pagina de eventos");
      this.$router.push({ name: "vistaEventos" });
    },
    completedLogIn: function(data) {
      /** El componente APP delegará a componentes hijos la implementación de las funcionalidades LogIn y 
      SignUp, pero este quiere controlar el resultado de estas operaciones, para ello definirá dos métodos 
      completedLogIn y completedSignUp, los cuales sus hijos podrán emitir para informar que se ha 
      finalizado el proceso */
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("access", data.token_access);
      localStorage.setItem("refresh", data.token_refresh);
      this.verifyAuth();
    },
    completedSignUp: function(data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },
  },
  /** A esta llave se asigna la función que debe ejecutar el componente cada vez que se renderice */
  created: function() {
    this.verifyAuth();
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0px;
  box-sizing: border-box;
  font-family: sans-serif;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 11vh;
  min-height: 100px;
  background-color: #37d47b;
  color: #0c233a;
  display: inline-flex;
  justify-content: space-between;
  align-items: center;
}
#logo {
  width: 12%;
  margin: 5em;
  padding: 0;
  display: flex;
  align-items: center;
}
.a-style {
  color: #c8ddce;
  cursor: pointer;
  text-decoration: underline;
}
.header h1 {
  width: 70%;
  text-align: left;
}
.header nav {
  height: 100%;
  width: 80%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: medium;
}
.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.body {
  height: calc(100vh-150px-300px);
}
.cliente-menu {
  margin: 0px;
  width: 70%;
  border-right-width: 0.5px;
  border-left-width: 0.5px;
  border-right-style: solid;
  border-left-style: solid;
  border-right-color: #7b9b20;
  border-left-color: #7b9b20;
  -webkit-transition: all 200ms ease 0s;
  -moz-transition: all 200ms ease 0s;
  -ms-transition: all 200ms ease 0s;
  -o-transition: all 200ms ease 0s;
  transition: all 200ms ease 0s;
  padding: 0;
  max-width: 1600px;
  margin-top: 1%;
  text-align: center;
  color: #15501f;
  text-decoration-color: #283747;
  text-decoration: none;
}
.cliente-menu img {
  width: 20px;
  height: 20px;
}
.cliente-menu a:hover {
  color: red;
  font-size: large;
}
.main-component {
  height: 90vh;
  margin: auto;
  background: #fdfefe;
}
footer {
  width: 100%;
  background: #104626;
  color: white;
  opacity: 0.9;
}
.container-footer-all {
  width: 100%;
  max-width: 1200px;
  margin: auto;
  padding: 40px;
}
.container-body {
  display: flex;
  justify-content: space-between;
}
.colum1 {
  max-width: 400px;
}
.colum1 h1 {
  font-size: 22px;
}
.colum1 p {
  font-size: 14px;
  color: #c7c7c7;
  margin-top: 20px;
}
.colum2 {
  max-width: 400px;
}
.colum2 h1 {
  font-size: 22px;
}
.row {
  margin-top: 20px;
  display: flex;
}
.row img {
  width: 36px;
  height: 36px;
}
.row label {
  margin-top: 10px;
  margin-left: 20px;
  color: #c7c7c7;
}
.colum3 {
  max-width: 400px;
}
.colum3 h1 {
  font-size: 22px;
}
.row2 {
  margin-top: 20px;
  display: flex;
}
.row2 img {
  width: 36px;
  height: 36px;
}
.row2 label {
  margin-top: 10px;
  margin-left: 20px;
  max-width: 140px;
}
.container-footer {
  width: 100%;
  background: #101010;
}
.footer {
  max-width: 1200px;
  margin: auto;
  display: flex;
  justify-content: space-between;
  padding: 20px;
}
.copyright {
  color: #c7c7c7;
}
.copyright a {
  text-decoration: none;
  color: white;
  font-weight: bold;
}
.information a {
  text-decoration: none;
  color: #c7c7c7;
}
@media screen and (max-width: 1100px) {
  .container-body {
    flex-wrap: wrap;
  }
  .colum1 {
    max-width: 100%;
  }
  .colum2,
  .colum3 {
    margin-top: 40px;
  }
}
</style>
