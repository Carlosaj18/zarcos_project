<template>
  <div>
    <div class="row">
      Detail Persona
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Documento</th>
              <th scope="col">Nombres</th>
              <th scope="col">Apellidos</th>
              <th scope="col">Telefono</th>
              <th scope="col">Ciudad</th>
              <th scope="col">Direccion</th>
              <th scope="col">Password</th>
            </tr>
          </thead>
          <!-- INPUTS-->
          <tbody>
            <tr>
              <td><input disabled v-model="personaSelected.id" /></td>
              <td><input type="text" v-model="personaSelected.username" /></td>
              <td><input type="text" v-model="personaSelected.email" /></td>
              <td>
                <input type="text" v-model="personaSelected.documento" />
              </td>
              <td><input type="text" v-model="personaSelected.nombres" /></td>
              <td><input type="text" v-model="personaSelected.apellidos" /></td>
              <td><input type="text" v-model="personaSelected.telefono" /></td>
              <td><input type="text" v-model="personaSelected.ciudad" /></td>
              <td><input type="text" v-model="personaSelected.direccion" /></td>
              <td>
                <input type="password" v-model="personaSelected.password" />
              </td>
            </tr>
            <!-- FALTA EL BOTON DE POST-->
          </tbody>
        </table>
      </div>
      <div class="row">
        <!-- Botones de Accion-->
        <div class="col-2">
          <button
            class="btn btn-success"
            v-on:click="personaUpdate(personaSelected)"
          >
            Editar
          </button>
        </div>
        <div class="col-2">
          <button
            type="button"
            class="btn btn-warning"
            v-on:click="cleanEntries()"
          >
            Limpiar entradas
          </button>
        </div>
        <div class="col-2">
          <button
            type="button"
            class="btn btn-primary"
            v-on:click="personaPost()"
          >
            Crear User
          </button>
        </div>
      </div>
    </div>
    <div class="row">
      <!-- Data a representar -->
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Codigo</th>
            <th scope="col">Username</th>
            <th scope="col">Email</th>
            <th scope="col">Documento</th>
            <th scope="col">Nombres</th>
            <th scope="col">Apellidos</th>
            <th scope="col">Telefono</th>
            <th scope="col">Ciudad</th>
            <th scope="col">Direccion</th>
            <th scope="col">Password</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="persona in personas" :key="persona.id">
            <td>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="personaGet(persona.id)"
              >
                {{ persona.id }}
              </button>
            </td>
            <td>{{ persona.username }}</td>
            <td>{{ persona.email }}</td>
            <td>{{ persona.documento }}</td>
            <td>{{ persona.nombres }}</td>
            <td>{{ persona.apellidos }}</td>
            <td>{{ persona.telefono }}</td>
            <td>{{ persona.ciudad }}</td>
            <td>{{ persona.direccion }}</td>
            <td>{{ persona.password }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="personaRemove(persona.id)"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ListaPersonas",

  data: function() {
    return {
      personas: [],
      personaCreate: {
        username: "",
        email: "",
        documento: "",
        nombres: "",
        apellidos: "",
        telefono: "",
        ciudad: "",
        direccion: "",
        password: "",
      },
      personaSelected: {
        id: "",
        username: "",
        email: "",
        documento: "",
        nombres: "",
        apellidos: "",
        telefono: "",
        ciudad: "",
        direccion: "",
        password: "",
      },
      personaEdit: {
        username: "",
        email: "",
        documento: "",
        nombres: "",
        apellidos: "",
        telefono: "",
        ciudad: "",
        direccion: "",
        password: "",
      },
    };
  },

  methods: {
    personaPost: function() {
      console.log("Creando USER");
      this.personaCreate.username = this.personaSelected.username;
      this.personaCreate.email = this.personaSelected.email;
      this.personaCreate.documento = this.personaSelected.documento;
      this.personaCreate.nombres = this.personaSelected.nombres;
      this.personaCreate.apellidos = this.personaSelected.apellidos;
      this.personaCreate.telefono = this.personaSelected.telefono;
      this.personaCreate.ciudad = this.personaSelected.ciudad;
      this.personaCreate.direccion = this.personaSelected.direccion;
      this.personaCreate.password = this.personaSelected.password;

      axios
        .post(
          "https://zarcos-web-be.herokuapp.com/persona/",
          this.personaCreate,
          {
            headers: {},
          }
        )
        .then((result) => {
          this.personaAll();
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    personaAll() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/personaLista/")
        .then((result) => {
          console.log(result.data);
          this.personas = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    personaGet(personaId) {
      axios
        .get(`https://zarcos-web-be.herokuapp.com/persona/${personaId}/`)
        .then((result) => (this.personaSelected = result.data))
        .catch((error) => console.log(error));
    },
    personaUpdate(persona) {
      console.log("Editando USER");
      this.personaEdit.username = this.personaSelected.username;
      this.personaEdit.email = this.personaSelected.email;
      this.personaEdit.documento = this.personaSelected.documento;
      this.personaEdit.nombres = this.personaSelected.nombres;
      this.personaEdit.apellidos = this.personaSelected.apellidos;
      this.personaEdit.telefono = this.personaSelected.telefono;
      this.personaEdit.ciudad = this.personaSelected.ciudad;
      this.personaEdit.direccion = this.personaSelected.direccion;
      this.personaEdit.password = this.personaSelected.password;

      axios
        .put(
          `https://zarcos-web-be.herokuapp.com/persona/update/${persona.id}/`,
          this.personaEdit
        )
        .then((result) => this.personaAll())
        .catch((error) => console.log(error));
    },
    personaRemove(personaId) {
      axios
        .delete(
          `https://zarcos-web-be.herokuapp.com/persona/remove/${personaId}/`
        )
        .then((result) => this.personaAll())
        .catch((e) => console.log(e));
    },
    cleanEntries() {
      console.log("Seteando los datos");
      this.personaSelected = {
        id: "",
        username: "",
        email: "",
        documento: "",
        nombres: "",
        apellidos: "",
        telefono: "",
        ciudad: "",
        direccion: "",
        password: "",
      };
    },
  },
  created: function() {
    this.personaAll();
  },
};
</script>

<style></style>
