<template>
  <div>
    <div class="row">
      Detail
      <div class="row">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Nombre Categoria</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input disabled v-model="categorySelected.id" /></td>
              <td>
                <input
                  type="text"
                  v-model="categorySelected.nombre_categoria"
                />
                <!-- {{ categorySelected ? categorySelected.nombre_categoria : "" }} -->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="row">
        <div class="col-2">
          <button
            class="btn btn-success"
            v-on:click="categoryUpdate(categorySelected)"
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
            v-on:click="categoriaPost()"
          >
            Crear Categoria
          </button>
        </div>
      </div>
    </div>
    <div class="row">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Codigo</th>
            <th scope="col">Nombre Categoria</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="category in categories" :key="category.id">
            <td>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="categoryGet(category.id)"
              >
                {{ category.id }}
              </button>
            </td>
            <td>{{ category.nombre_categoria }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="categoryRemove(category.id)"
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
  name: "ListaCategory",

  data: function() {
    return {
      categories: [],
      categoriaCreate: { nombre_categoria: "" },
      categorySelected: { id: "", nombre_categoria: "" },
      categoryEdit: { nombre_categoria: "" },
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

    categoriaPost: function() {
      this.categoriaCreate.nombre_categoria = this.categorySelected.nombre_categoria;
      axios
        .post(
          "https://zarcos-web-be.herokuapp.com/categoria/",
          this.categoriaCreate,
          { headers: {} }
        )
        .then((result) => {
          this.categoriaAll();
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    categoriaAll() {
      axios
        .get("https://zarcos-web-be.herokuapp.com/categoriaLista/")
        .then((result) => {
          console.log(result.data);
          this.categories = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el registro");
        });
    },
    categoryGet(categoryId) {
      axios
        .get(`https://zarcos-web-be.herokuapp.com/categoria/${categoryId}/`)
        .then((result) => (this.categorySelected = result.data))
        .catch((error) => console.log(error));
    },
    categoryUpdate(category) {
      console.log("Editando categoria");
      this.categoryEdit.nombre_categoria = this.categorySelected.nombre_categoria; /**  */

      axios
        .put(
          `https://zarcos-web-be.herokuapp.com/categoria/update/${category.id}/`,
          this.categoryEdit
        )
        .then((result) => this.categoriaAll())
        .catch((error) => console.log(error));
    },
    categoryRemove(categoryId) {
      axios
        .delete(
          `https://zarcos-web-be.herokuapp.com/categoria/remove/${categoryId}/`
          /**{ headers: { Authorization: `Bearer ${token}` } }*/
        )
        .then((result) => this.categoriaAll())
        .catch((e) => console.log(e));
    },
    cleanEntries() {
      console.log("Seteando los datos");
      this.categorySelected = { id: "", nombre_categoria: "" };
    },
  },
  created: function() {
    this.categoriaAll();
  },
};
</script>

<style></style>
