<!--
<template>
    <div id="app">
        <table class="table">
            <thead>
                <th>Id</th>
                <th>Nombre Categoria</th>
            </thead>
            <tbody>
                <tr v-for="category in categories" :key="category.id">
                    <td>{{category.id}}</td>
                    <td>{{category.nombre_categoria}}</td>
                </tr>
            </tbody>
        </table>

    </div>
</template>
-->

<template>

    <div class="signUp_categoria">

        <div class="container_categoria">
            <h2> Categoria </h2>
            <form v-on:submit.prevent="categoriaPost">
                <input type="text" v-model="categoria.nombre_categoria" placeholder="Nombre Categoria">
                <br>                
                <button type="submit">POST Categoria</button>
            </form>
        </div>
    </div>

</template>

<script>
import jwt_decode from "jwt-decode";
import axios from 'axios';

export default {
    name: 'Category',

    data:function(){
        return {
            categoria:{
                nombre_categoria:"",
            },
            categories: [],
        }    
    },

    methods:{
        
        categoriaPost: function(){
            axios.post("https://zarcos-web-be.herokuapp.com/categoria/",
                        this.categoria,
                        {headers:{}}
            ).then((result) => {
                let dataCategoria = {
                    categoria : this.categoria.nombre_categoria
                }
                this.$emit('completedCategoria', dataCategoria)
                
            })
            .catch((error) => {
                  console.log(error); 
                  alert("Error en el registro");
                   
            });
        },
        created: function(){
            this.categoriaAll()
        }    
    }

}
    
</script>


<style>

    .signUp_categoria{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_categoria {
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .signUp_categoria h2{
        color: #283747;

    }

    .signUp_categoria form{
        width: 70%;
        
    }

    .signUp_categoria input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .signUp_categoria button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }

    .signUp_categoria button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }

</style>


<!--
<style>
#app{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
-->

