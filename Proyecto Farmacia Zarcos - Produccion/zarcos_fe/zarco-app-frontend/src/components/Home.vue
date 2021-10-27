<template>
  <div class="container">
    <div class="row">
      <div class="greetings">
        <h1>
          ¡Bienvenido <span> {{ username }} </span>!
        </h1>
      </div>
      <div class="list-group">
        <h3 class="list-group-item">Categorias</h3>
        <button
          v-on:click="loadCategory"
          type="button"
          class="btn btn-secondary"
        >
          Gestionar Categorias
        </button>
        <h3 class="list-group-item">Tipo de Evento</h3>
        <button
          v-on:click="loadEventType"
          type="button"
          class="btn btn-secondary"
        >
          Gestionar Tipos de Evento
        </button>
        <h3 class="list-group-item">Lugar</h3>
        <button v-on:click="loadPlace" type="button" class="btn btn-secondary">
          Gestionar Lugares
        </button>
        <h3 class="list-group-item">Evento</h3>
        <button v-on:click="loadEvent" type="button" class="btn btn-secondary">
          Gestionar Eventos
        </button>
        <h3 class="list-group-item">Personas</h3>
        <button v-on:click="loadPerson" type="button" class="btn btn-secondary">
          Gestionar Personas
        </button>
        <h3 class="list-group-item">Inscripciones</h3>
        <button
          v-on:click="loadInscriptions"
          type="button"
          class="btn btn-secondary"
        >
          Gestionar Inscripciones
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      username: localStorage.getItem("username") || "none",
    };
  },
  component: {},
  methods: {
    loadCategory: function() {
      /**this.$router.push({ name: "Category" });*/
      this.$router.push({ name: "ListaCategory" });
    },
    loadPlace: function() {
      /**this.$router.push({ name: "Lugar" });*/
      this.$router.push({ name: "ListaLugar" });
    },
    loadEventType: function() {
      /**this.$router.push({ name: "TipoEvento" });*/
      this.$router.push({ name: "ListaTipoEvento" });
    },
    loadEvent: function() {
      this.$router.push({ name: "ListaEventos" });
    },
    loadPerson: function() {
      this.$router.push({ name: "ListaPersonas" });
    },
    loadInscriptions: function() {
      this.$router.push({ name: "listaInscripciones" });
    },
  },
  created() {},
};
</script>

<style>
.greetings {
  margin: 0;
  padding: 0%;
  height: 20%;
  width: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.greetings h1 {
  font-size: 34px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #283747;
}
.greetings span {
  color: crimson;
  font-weight: bold;
}
</style>
