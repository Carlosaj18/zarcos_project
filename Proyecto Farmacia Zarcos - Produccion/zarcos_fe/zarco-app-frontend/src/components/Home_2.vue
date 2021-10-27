<template>
  <div class="greetings container">
    <div class="row">
      <div class="col d-flex justify-content-center">
        <h1>
          ¡Bienvenido <span> {{ username }} </span>!
        </h1>
      </div>
    </div>
    <div v-if="eventSelected !== null" class="row">
      <div class="col">
        {{ eventSelected.nombre_evento }}
      </div>
      <div class="col">
        {{ eventSelected.categoria_FK.nombre_categoria }}
      </div>
      <div class="col">
        {{ eventSelected.tipoEvento_FK.tipo_evento }}
      </div>
      <div class="col">
        {{ eventSelected.fecha }}
      </div>
      <div class="col">
        {{ eventSelected.lugar_FK.ciudad }}
      </div>
      <div class="col">
        {{ eventSelected.lugar_FK.direccion }}
      </div>
      <div class="col">
        {{ eventSelected.precio }}
      </div>
    </div>
    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">id</th>
              <th scope="col">Nombre</th>
              <th scope="col">Categoria</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(event, index) in events" :key="event.id">
              <td>
                <button
                  type="button"
                  class="btn btn-info"
                  v-on:click="eventGet(event.id)"
                >
                  {{ event.id }}
                </button>
              </td>
              <td v-if="isEditing[index]">
                <input v-model="event.nombre_evento" />
              </td>
              <td v-else>
                <div>{{ event.nombre_evento }}</div>
              </td>
              <td v-if="isEditing[index]">
                <input v-model="event.categoria_FK.nombre_categoria" />
              </td>
              <td v-else>
                <div>{{ event.categoria_FK.nombre_categoria }}</div>
              </td>
              <td>
                <button
                  type="button"
                  class="btn btn-warning"
                  v-on:click="eventUpdate(event, index)"
                  v-if="isEditing[index]"
                >
                  Actualizar
                </button>
                <button
                  type="button"
                  class="btn btn-warning"
                  v-on:click="setIsEditing(index)"
                  v-else
                >
                  Editar
                </button>
              </td>
              <td>
                <button
                  type="button"
                  class="btn btn-danger"
                  v-on:click="eventRemove(event.id)"
                >
                  Eliminar
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data: function() {
    return {
      username: localStorage.getItem("username"),
      events: [],
      eventSelected: null,
      isEditing: [],
    };
  },
  methods: {
    eventPost: function() {
      axios.post("https://zarcos-web-be.herokuapp.com/evento/");
    },
    eventListaGet: function() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/eventoLista/")
        .then((response) => {
          this.events = response.data; //estos son los eventos
          this.isEditing = response.data.map((_x) => false); // paso de una lista de eventos a una lista de false
        });
    },
    eventGet: function(eventId) {
      fetch(`https://zarcos-web-be.herokuapp.com/evento/${eventId}`, {
        "Access-Control-Allow-Origin": "*",
      }).then((res) => {
        res.json().then((x) => (this.eventSelected = x));
      });
    },
    eventUpdate: function(evento, index) {
      axios.put(
        `https://zarcos-web-be.herokuapp.com/evento/update/${evento.id}`,
        {
          evento,
        }
      );
      this.isEditing[index] = !this.isEditing[index];
    },
    eventRemove: function(eventId) {
      fetch(`https://zarcos-web-be.herokuapp.com/evento/remove/${eventId}`, {
        method: "DELETE",
        "Access-Control-Allow-Origin": "*",
      })
        .then((res) => {
          this.eventListaGet();
        })
        .catch((e) => {
          console.log(e.message);
        });
    },
    setIsEditing: function(index) {
      this.isEditing[index] = !this.isEditing[index];
    },
  },
  created: function() {
    this.eventListaGet();
  },
};
</script>

<style>
.greetings {
  display: flex;
  justify-content: center;
  align-items: center;
}

.greetings h1 {
  font-size: 50px;
  color: #283747;
}

.greetings span {
  color: crimson;
  font-weight: bold;
}
</style>
