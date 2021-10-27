<template>
  <div>
    <div>
      Detail Evento
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Nombre Evento</th>
              <th scope="col">Categoria</th>
              <th scope="col">Tipo Evento</th>
              <th scope="col">Fecha</th>
              <th scope="col">Hora</th>
              <th scope="col">Duraccion</th>
              <th scope="col">Lugar</th>
              <th scope="col">Precio</th>
              <th scope="col">Cupo Maximo</th>
            </tr>
          </thead>
          <!-- INPUTS-->
          <tbody>
            <tr>
              <td><input disabled v-model="eventoSelected.id" /></td>
              <td>
                <input type="text" v-model="eventoSelected.nombre_evento" />
              </td>
              <td>
                <input type="number" v-model="eventoSelected.categoria_FK.id" />
              </td>
              <td>
                <input
                  type="number"
                  v-model="eventoSelected.tipoEvento_FK.id"
                />
              </td>
              <td><input type="date" v-model="eventoSelected.fecha" /></td>
              <td><input type="time" v-model="eventoSelected.hora" /></td>
              <td><input type="number" v-model="eventoSelected.duracion" /></td>
              <td>
                <input type="number" v-model="eventoSelected.lugar_FK.id" />
              </td>
              <td><input type="number" v-model="eventoSelected.precio" /></td>
              <td>
                <input type="number" v-model="eventoSelected.cupo_maximo" />
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
            Editar Evento
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
            v-on:click="eventoPost()"
          >
            Crear Evento
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
            <th scope="col">Categoria id</th>
            <th scope="col">Categoria Nombre</th>
            <th scope="col">Tipo id</th>
            <th scope="col">Tipo Evento</th>
            <th scope="col">Fecha</th>
            <th scope="col">Hora</th>
            <th scope="col">Duraccion</th>
            <th scope="col">Lugar id</th>
            <th scope="col">Lugar</th>
            <th scope="col">Ciudad</th>
            <th scope="col">Precio</th>
            <th scope="col">Cupo Maximo</th>
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
            <td>{{ evento.categoria_FK.id }}</td>
            <td>{{ evento.categoria_FK.nombre_categoria }}</td>
            <td>{{ evento.tipoEvento_FK.id }}</td>
            <td>{{ evento.tipoEvento_FK.tipo_evento }}</td>
            <td>{{ evento.fecha }}</td>
            <td>{{ evento.hora }}</td>
            <td>{{ evento.duracion }}</td>
            <td>{{ evento.lugar_FK.id }}</td>
            <td>{{ evento.lugar_FK.ciudad }}</td>
            <td>{{ evento.lugar_FK.direccion }}</td>
            <td>{{ evento.precio }}</td>
            <td>{{ evento.cupo_maximo }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="eventoRemove(evento.id)"
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
    eventoPost: function() {
      console.log("Creando USER");
      this.eventoCreate.nombre_evento = this.eventoSelected.nombre_evento;
      this.eventoCreate.categoria_FK = this.eventoSelected.categoria_FK.id;
      this.eventoCreate.tipoEvento_FK = this.eventoSelected.tipoEvento_FK.id;
      this.eventoCreate.fecha = this.eventoSelected.fecha;
      this.eventoCreate.hora = this.eventoSelected.hora;
      this.eventoCreate.duracion = this.eventoSelected.duracion;
      this.eventoCreate.lugar_FK = this.eventoSelected.lugar_FK.id;
      this.eventoCreate.precio = this.eventoSelected.precio;
      this.eventoCreate.cupo_maximo = this.eventoSelected.cupo_maximo;

      axios
        .post(
          "https://zarcos-web-be.herokuapp.com/evento/",
          this.eventoCreate,
          {
            headers: {},
          }
        )
        .then((result) => {
          this.eventosAll();
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
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
    eventoUpdate(evento) {
      console.log("Editando EVENTO");
      this.eventoEdit.nombre_evento = this.eventoSelected.nombre_evento;
      this.eventoEdit.categoria_FK = this.eventoSelected.categoria_FK.id;
      this.eventoEdit.tipoEvento_FK = this.eventoSelected.tipoEvento_FK.id;
      this.eventoEdit.fecha = this.eventoSelected.fecha;
      this.eventoEdit.hora = this.eventoSelected.hora;
      this.eventoEdit.duracion = this.eventoSelected.duracion;
      this.eventoEdit.lugar_FK = this.eventoSelected.lugar_FK.id;
      this.eventoEdit.precio = this.eventoSelected.precio;
      this.eventoEdit.cupo_maximo = this.eventoSelected.cupo_maximo;

      axios
        .put(
          `https://zarcos-web-be.herokuapp.com/evento/update/${evento.id}/`,
          this.eventoEdit
        )
        .then((result) => this.eventosAll())
        .catch((error) => console.log(error));
    },
    eventoRemove(eventoId) {
      axios
        .delete(
          `https://zarcos-web-be.herokuapp.com/evento/remove/${eventoId}/`
        )
        .then((result) => this.eventosAll())
        .catch((e) => console.log(e));
    },
    cleanEntries() {
      console.log("Seteando los datos");
      this.eventoSelected = {
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
      };
    },
  },
  created: function() {
    this.eventosAll();
  },
};
</script>

<style></style>
