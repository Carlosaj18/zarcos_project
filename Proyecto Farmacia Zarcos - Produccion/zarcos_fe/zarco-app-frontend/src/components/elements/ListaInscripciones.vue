<template>
  <div>
    <div>
      Detail Inscripcion
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Persona id</th>
              <th scope="col">Evento id</th>
              <th scope="col">Numero de Entrandas</th>
              <th scope="col">Pago Total</th>
            </tr>
          </thead>
          <!-- INPUTS-->
          <tbody>
            <tr>
              <td><input disabled v-model="inscripcionSelected.id" /></td>
              <td>
                <input
                  type="numero"
                  v-model="inscripcionSelected.persona_FK.id"
                />
              </td>
              <td>
                <input type="text" v-model="inscripcionSelected.evento_FK.id" />
              </td>
              <td>
                <input
                  type="text"
                  v-model="inscripcionSelected.numeroEntradas"
                />
              </td>
              <td>
                <input type="text" v-model="inscripcionSelected.pagoTotal" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="row">
        <!-- Botones de Accion-->
        <div class="col-2">
          <button
            class="btn btn-success"
            v-on:click="inscripcionUpdate(inscripcionSelected)"
          >
            Editar Inscripcion
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
            v-on:click="inscripcionPost()"
          >
            Crear Inscripcion
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
            <th scope="col">Persona id</th>
            <th scope="col">User</th>
            <th scope="col">Nombres</th>
            <th scope="col">Apellidos</th>
            <th scope="col">Evento id</th>
            <th scope="col">Nombre Evento</th>
            <th scope="col">Fecha Evento</th>
            <th scope="col">Hora Evento</th>
            <th scope="col">Duracion</th>
            <th scope="col">Numero de Entrandas</th>
            <th scope="col">Pago Total</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="inscri in inscripciones" :key="inscri.id">
            <td>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="inscripcionGet(inscri.id)"
              >
                {{ inscri.id }}
              </button>
            </td>
            <td>{{ inscri.persona_FK.id }}</td>
            <td>{{ inscri.persona_FK.username }}</td>
            <td>{{ inscri.persona_FK.nombres }}</td>
            <td>{{ inscri.persona_FK.apellidos }}</td>
            <td>{{ inscri.evento_FK.id }}</td>
            <td>{{ inscri.evento_FK.nombre_evento }}</td>
            <td>{{ inscri.evento_FK.fecha }}</td>
            <td>{{ inscri.evento_FK.hora }}</td>
            <td>{{ inscri.evento_FK.duracion }}</td>
            <td>{{ inscri.numeroEntradas }}</td>
            <td>{{ inscri.pagoTotal }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="inscripcionRemove(inscri.id)"
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
  name: "listaInscripciones",

  data: function() {
    return {
      inscripciones: [],
      inscripcionCreate: {
        id: "",
        persona_FK: "",
        evento_FK: "",
        numeroEntradas: "",
        pagoTotal: "",
      },
      inscripcionSelected: {
        id: "",
        persona_FK: {
          id: "",
          username: "",
          email: "",
          documento: "",
          nombres: "",
          apellidos: "",
          telefono: "",
          ciudad: "",
          direccion: "",
        },
        evento_FK: {
          id: "",
          nombre_evento: "",
          fecha: "",
          hora: "",
          duracion: "",
          precio: "",
          cupo_maximo: "",
        },
        numeroEntradas: "",
        pagoTotal: "",
      },
      inscripcionEdit: {
        id: "",
        persona_FK: "",
        evento_FK: "",
        numeroEntradas: "",
        pagoTotal: "",
      },
    };
  },

  methods: {
    inscripcionPost: function() {
      console.log("Creando USER");
      this.inscripcionCreate.persona_FK = this.inscripcionSelected.persona_FK.id;
      this.inscripcionCreate.evento_FK = this.inscripcionSelected.evento_FK.id;
      this.inscripcionCreate.numeroEntradas = this.inscripcionSelected.numeroEntradas;
      this.inscripcionCreate.pagoTotal = this.inscripcionSelected.pagoTotal;

      axios
        .post(
          "https://zarcos-web-be.herokuapp.com/inscripcion/",
          this.inscripcionCreate,
          {
            headers: {},
          }
        )
        .then((result) => {
          this.inscripcionesAll();
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    inscripcionesAll() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/inscripcionLista/")
        .then((result) => {
          console.log(result.data);
          this.inscripciones = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    inscripcionGet(inscripcionId) {
      axios
        .get(
          `https://zarcos-web-be.herokuapp.com/inscripcion/${inscripcionId}/`
        )
        .then((result) => (this.inscripcionSelected = result.data))
        .catch((error) => console.log(error));
    },
    inscripcionUpdate(inscripcion) {
      console.log("Editando INSCRIPCION");
      this.inscripcionEdit.persona_FK = this.inscripcionSelected.persona_FK.id;
      this.inscripcionEdit.evento_FK = this.inscripcionSelected.evento_FK.id;
      this.inscripcionEdit.numeroEntradas = this.inscripcionSelected.numeroEntradas;
      this.inscripcionEdit.pagoTotal = this.inscripcionSelected.pagoTotal;

      axios
        .put(
          `https://zarcos-web-be.herokuapp.com/inscripcion/update/${inscripcion.id}/`,
          this.inscripcionEdit
        )
        .then((result) => this.inscripcionesAll())
        .catch((error) => console.log(error));
    },
    inscripcionRemove(eventoId) {
      axios
        .delete(
          `https://zarcos-web-be.herokuapp.com/inscripcion/remove/${eventoId}/`
        )
        .then((result) => this.inscripcionesAll())
        .catch((e) => console.log(e));
    },
    cleanEntries() {
      console.log("Seteando los datos");
      this.inscripcionSelected = {
        id: "",
        persona_FK: {
          id: "",
          username: "",
          email: "",
          documento: "",
          nombres: "",
          apellidos: "",
          telefono: "",
          ciudad: "",
          direccion: "",
        },
        evento_FK: {
          id: "",
          nombre_evento: "",
          fecha: "",
          hora: "",
          duracion: "",
          precio: "",
          cupo_maximo: "",
        },
        numeroEntradas: "",
        pagoTotal: "",
      };
    },
  },
  created: function() {
    this.inscripcionesAll();
  },
};
</script>

<style></style>
