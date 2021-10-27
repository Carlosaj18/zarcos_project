<template>
  <div>
    <div>
      Detail Tipo Eventos
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Tipo Evento</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input disabled v-model="tipoEventoSelected.id" /></td>
              <td>
                <input type="text" v-model="tipoEventoSelected.tipo_evento" />
                <!-- {{ categorySelected ? categorySelected.nombre_categoria : "" }} -->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="d-flex justify-content-center" style="gap:2%;">
        <div>
          <button
            class="btn btn-success"
            v-on:click="tipoEventoUpdate(tipoEventoSelected)"
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
            v-on:click="tipoEventoPost()"
          >
            Crear Tipo Evento
          </button>
        </div>
      </div>
    </div>
    <div class="row">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Codigo</th>
            <th scope="col">Tipo Evento</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tipoEvento in tipoEventos" :key="tipoEvento.id">
            <td>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="tipoEventoGet(tipoEvento.id)"
              >
                {{ tipoEvento.id }}
              </button>
            </td>
            <td>{{ tipoEvento.tipo_evento }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="tipoEventoRemove(tipoEvento.id)"
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
  name: "ListaTipoEvento",

  data: function() {
    return {
      tipoEventos: [],
      tipoEventoCreate: { tipo_evento: "" },
      tipoEventoSelected: { id: "", tipo_evento: "" },
      tipoEventoEdit: { tipo_evento: "" },
    };
  },

  methods: {
    /**async categoriaAll() {
      const res = await axios.get(
        "https://zarcos-web-be.herokuapp.com/categoriaLista/"
      );
      this.categories = res.data;
      console.log(res.data);
      console.log("sigue corriendo");
    },*/

    tipoEventoPost: function() {
      this.tipoEventoCreate.tipo_evento = this.tipoEventoSelected.tipo_evento;
      axios
        .post(
          "https://zarcos-web-be.herokuapp.com/tipoEvento/",
          this.tipoEventoCreate,
          { headers: {} }
        )
        .then((result) => {
          this.tipoEventoAll();
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    tipoEventoAll() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/tipoEventoLista/")
        .then((result) => {
          console.log(result.data);
          this.tipoEventos = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    tipoEventoGet(tipoEventoId) {
      axios
        .get(`https://zarcos-web-be.herokuapp.com/tipoEvento/${tipoEventoId}/`)
        .then((result) => (this.tipoEventoSelected = result.data))
        .catch((error) => console.log(error));
    },
    tipoEventoUpdate(tipoEvento) {
      console.log("Editando categoria");
      this.tipoEventoEdit.tipo_evento = this.tipoEventoSelected.tipo_evento;

      axios
        .put(
          `https://zarcos-web-be.herokuapp.com/tipoEvento/update/${tipoEvento.id}/`,
          this.tipoEventoEdit
        )
        .then((result) => this.tipoEventoAll())
        .catch((error) => console.log(error));
    },
    tipoEventoRemove(tipoEventoId) {
      axios
        .delete(
          `https://zarcos-web-be.herokuapp.com/tipoEvento/remove/${tipoEventoId}/`
        )
        .then((result) => this.tipoEventoAll())
        .catch((e) => console.log(e));
    },
    cleanEntries() {
      console.log("Seteando los datos");
      this.tipoEventoSelected = { id: "", tipo_evento: "" };
    },
  },
  created: function() {
    this.tipoEventoAll();
  },
};
</script>

<style></style>
