<template>
  <table class="table-striped">
    <thead>
      <tr>
        <th scope="col">Codigo</th>
        <th scope="col">Nombre Evento</th>
        <th scope="col">Categoria</th>
        <th scope="col">Tipo Evento</th>
        <th scope="col">Fecha</th>
        <th scope="col">Hora</th>
        <th scope="col">Duraccion</th>
        <th scope="col">Ciudad</th>
        <th scope="col">Direccion</th>
        <th scope="col">Lugar</th>
        <th scope="col">Descripcion del lugar</th>
        <th scope="col">Precio</th>
        <th scope="col">Desccripcion Simple</th>
        <th scope="col">Descripcion Completa</th>
        <th scope="col">Cupo Maximo</th>
        <th scope="col">Evento Activo</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="evento in eventos" :key="evento.id">
        <td>{{ evento.id }}</td>
        <td>{{ evento.nombre_evento }}</td>
        <td>{{ evento.categoria_FK.nombre_categoria }}</td>
        <td>{{ evento.tipoEvento_FK.tipo_evento }}</td>
        <td>{{ evento.fecha }}</td>
        <td>{{ evento.hora }}</td>
        <td>{{ evento.duracion }}</td>
        <td>{{ evento.lugar_FK.ciudad }}</td>
        <td>{{ evento.lugar_FK.direccion }}</td>
        <td>{{ evento.lugar_FK.nombre_lugar }}</td>
        <td>{{ evento.lugar_FK.complex }}</td>
        <td>{{ evento.precio }}</td>
        <td>{{ evento.descripcionSimple }}</td>
        <td>{{ evento.descripcionCompleta }}</td>
        <td>{{ evento.cupo_maximo }}</td>
        <td>{{ evento.is_active }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  name: "ListaEventos",

  data: function() {
    return {
      eventos: [],
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
  },
  created: function() {
    this.eventosAll();
  },
};
</script>

<style>
.table-striped {
  overflow: scroll;
}
</style>
