<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar Sesión</h2>
      <!-- El formulario va a llamar a una funcion (evento) de java script cuando se de click en enviar 
                y este hara el respectivo llamado al servicio web-->
      <form v-on:submit.prevent="processLogInUser">
        <!-- input de texto que recibo del usuario 
                    y se usara un modelo de vue (objeto) para comparar el usaurio y la contraseña con el backend
                    en el frontend voy a crear un objeto user con dos atributos -username y password
                    y vue lo que hace es guardar lo que recibe del usuaruo en user.username y user.password. 
                    Se puede guiar con los nombres del serializador del backend que es lo que espera recibir-->
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <!-- Dicho formulario tiene dos entradas que son username y password,estas 
                están asociadas al objeto user. -->
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  </div>
</template>

<script>
/** Aqui se eviencia como se consume el servicio web */
import axios from "axios";

export default {
  /** Exporte el componente Login */
  name: "LogIn",

  data: function() {
    /** Se usan las variables del username y el password del objeto user el cual
     * contiene los datos de entrada del formulario
     */
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    processLogInUser: function() {
      /** Se usa el endpont que se necesita del servicio web del backend
             * se hace uso de la herramienta axios para ejecutar una petición HTTP de tipo POST
            al componente de back-end usando la URL correspondiente, pasando como parámetro las 
            credenciales del usuario.
            */
      axios
        .post(
          "https://zarcos-web-be.herokuapp.com/login/",
          /** Le decimos la data que vamos a enviarle al backend en el body, es decir,
           * el objeto user con sus atributos username y password
           */
          this.user,
          { headers: {} }
        )
        /** Aqui van las acciones que voy a ejecutar en ese endpoint */
        .then((result) => {
          let dataLogIn = {
            /** . Luego, se procesa la respuesta del back-end, si todo es correcto se crea un
                        objeto que servirá de parámetro para emitir la función del padre completedLogIn
                     * El user es el que cree con la variable en el formulario me va a devolver los siguientes resultados 
                     * El access token y el refresh
                     * Data se llama por defecto cuando envio o recibo informacion. Entonces le digo de la data de result me va a devolver */

            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          /** Del componente hijo al padre envio infomracion con emit
           * Y ahora la App va a tener la infomracion del login a traves del objeto dataLogin que tiene tres atriburos username, acces y refresh
           */
          console.log(dataLogIn);
          this.$emit("completedLogIn", dataLogIn);
          this.$router.push({ name: "home" });
        })
        /** Con esto voy a manejar los errores */
        .catch((error) => {
          if (error.response.status == "401")
            alert("ERROR: Credenciales no válidas");
        });
    },
  },
};
</script>

<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.container_logIn_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 25%;
  height: 60%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logIn_user h2 {
  color: #283747;
}

.logIn_user form {
  width: 70%;
}

.logIn_user input {
  height: 40px;
  width: 100%;

  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;

  border: 1px solid #283747;
}

.logIn_user button {
  width: 100%;
  height: 40px;

  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
}

.logIn_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>
