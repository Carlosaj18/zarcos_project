<template>
  <div>
    <div>
      Detail Lugar
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Ciudad</th>
              <th scope="col">Direccion</th>
              <th scope="col">Nombre Lugar</th>
              <th scope="col">Complemento</th>
            </tr>
          </thead>
          <!-- INPUTS-->
          <tbody>
            <tr>
              <td><input disabled v-model="lugarSelected.id" /></td>
              <td><input type="text" v-model="lugarSelected.ciudad" /></td>
              <td><input type="text" v-model="lugarSelected.direccion" /></td>
              <td>
                <input type="text" v-model="lugarSelected.nombre_lugar" />
              </td>
              <td><input type="text" v-model="lugarSelected.complemento" /></td>
            </tr>
            <!-- FALTA EL BOTON DE POST-->
          </tbody>
        </table>
      </div>
      <div class="d-flex justify-content-center" style="gap:2%;">
        <!-- Botones de Accion-->
        <div>
          <button
            class="btn btn-success"
            v-on:click="lugarUpdate(lugarSelected)"
          >
            Editar
          </button>
        </div>
        <div>
          <button
            type="button"
            class="btn btn-warning"
            v-on:click="cleanEntries()"
          >
            Limpiar entradas
          </button>
        </div>
        <div>
          <button
            type="button"
            class="btn btn-primary"
            v-on:click="lugarPost()"
          >
            Crear Lugar
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
            <th scope="col">Ciudad</th>
            <th scope="col">Direccion</th>
            <th scope="col">Nombre Lugar</th>
            <th scope="col">Complemento</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="lugar in lugares" :key="lugar.id">
            <td>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="lugarGet(lugar.id)"
              >
                {{ lugar.id }}
              </button>
            </td>
            <td>{{ lugar.ciudad }}</td>
            <td>{{ lugar.direccion }}</td>
            <td>{{ lugar.nombre_lugar }}</td>
            <td>{{ lugar.complemento }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="lugarRemove(lugar.id)"
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
  name: "ListaLugar",

  data: function() {
    return {
      lugares: [],
      lugarCreate: {
        ciudad: "",
        direccion: "",
        nombre_lugar: "",
        complemento: "",
      },
      lugarSelected: {
        id: "",
        ciudad: "",
        direccion: "",
        nombre_lugar: "",
        complemento: "",
      },
      lugarEdit: {
        ciudad: "",
        direccion: "",
        nombre_lugar: "",
        complemento: "",
      },
    };
  },

  methods: {
    lugarPost: function() {
      this.lugarCreate.ciudad = this.lugarSelected.ciudad;
      this.lugarCreate.direccion = this.lugarSelected.direccion;
      this.lugarCreate.nombre_lugar = this.lugarSelected.nombre_lugar;
      this.lugarCreate.complemento = this.lugarSelected.complemento;
      axios
        .post("https://zarcos-web-be.herokuapp.com/lugar/", this.lugarCreate, {
          headers: {},
        })
        .then((result) => {
          this.lugarAll();
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    lugarAll() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/lugarLista/")
        .then((result) => {
          console.log(result.data);
          this.lugares = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    lugarGet(lugarId) {
      axios
        .get(`https://zarcos-web-be.herokuapp.com/lugar/${lugarId}/`)
        .then((result) => (this.lugarSelected = result.data))
        .catch((error) => console.log(error));
    },
    lugarUpdate(lugar) {
      console.log("Editando lugar");
      this.lugarEdit.ciudad = this.lugarSelected.ciudad;
      this.lugarEdit.direccion = this.lugarSelected.direccion;
      this.lugarEdit.nombre_lugar = this.lugarSelected.nombre_lugar;
      this.lugarEdit.complemento = this.lugarSelected.complemento;
      axios
        .put(
          `https://zarcos-web-be.herokuapp.com/lugar/update/${lugar.id}/`,
          this.lugarEdit
        )
        .then((result) => this.lugarAll())
        .catch((error) => console.log(error));
    },
    lugarRemove(lugarId) {
      axios
        .delete(`https://zarcos-web-be.herokuapp.com/lugar/remove/${lugarId}/`)
        .then((result) => this.lugarAll())
        .catch((e) => console.log(e));
    },
    cleanEntries() {
      console.log("Seteando los datos");
      this.lugarSelected = {
        id: "",
        ciudad: "",
        direccion: "",
        nombre_lugar: "",
        complemento: "",
      };
    },
  },
  created: function() {
    this.lugarAll();
  },
};
</script>

<style></style>
