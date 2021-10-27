<template>
  <div>
    <div class="row">
      Detail Evento
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Nombre Evento</th>
            </tr>
          </thead>
          <!-- INPUTS-->
          <tbody>
            <tr>
              <td><input disabled v-model="eventoSelected.id" /></td>
              <td>
                <input type="text" v-model="eventoSelected.nombre_evento" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="d-flex justify-content-center">
        <!-- Botones de Accion-->
        <div class="col-2">
          <button
            class="btn btn-success"
            v-on:click="eventoUpdate(eventoSelected)"
          >
            Buscar Evento
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
            <th scope="col">Nombre Evento</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="evento in eventos" :key="evento.id">
            <td>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="eventoGet(evento.id)"
              >
                {{ evento.id }}
              </button>
            </td>
            <td>{{ evento.nombre_evento }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="eventoDetalle(evento.id)"
              >
                Detalle Evento
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
  name: "ListaEventos",

  data: function() {
    return {
      eventos: [],
      eventoCreate: {
        nombre_evento: "",
        categoria_FK: "",
        tipoEvento_FK: "",
        fecha: "",
        hora: "",
        duracion: "",
        lugar_FK: "",
        precio: "",
        cupo_maximo: "",
      },
      eventoSelected: {
        id: "",
        nombre_evento: "",
        categoria_FK: {
          id: "",
        },
        tipoEvento_FK: {
          id: "",
        },
        fecha: "",
        hora: "",
        duracion: "",
        lugar_FK: {
          id: "",
        },
        precio: "",
        cupo_maximo: "",
      },
      eventoEdit: {
        nombre_evento: "",
        categoria_FK: "",
        tipoEvento_FK: "",
        fecha: "",
        hora: "",
        duracion: "",
        lugar_FK: "",
        precio: "",
        cupo_maximo: "",
      },
    };
  },

  methods: {
    eventosAll() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/eventoLista/")
        .then((result) => {
          console.log(result.data);
          this.eventos = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    eventoGet(eventoId) {
      axios
        .get(`https://zarcos-web-be.herokuapp.com/evento/${eventoId}/`)
        .then((result) => (this.eventoSelected = result.data))
        .catch((error) => console.log(error));
    },
    eventoDetalle() {
        this.$router.push({ name: "eventoDetails" });
    }
  },
  created: function() {
    this.eventosAll();
  },
};
</script>

<style></style>
