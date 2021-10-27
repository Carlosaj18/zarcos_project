<template>

    <div class="signUp_lugar">

        <div class="container_lugar">
            <h2> Categoria </h2>
            <form v-on:submit.prevent="lugarPost">
                <input type="text" v-model="lugar.ciudad" placeholder="Ciudad">
                <br>     
                <input type="text" v-model="lugar.direccion" placeholder="Direccion">
                <br>
                <input type="text" v-model="lugar.nombre_lugar" placeholder="Nombre Lugar">
                <br>  
                <input type="text" v-model="lugar.complemento" placeholder="Complemento">
                <br>               
                <button type="submit">POST Lugar</button>
            </form>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: 'Place',

    data:function(){
        return{
            lugar:{
                ciudad:"",
                direccion:"",
                nombre_lugar:"",
                complemento:""
            },
        }    
    },

    methods:{
        
        lugarPost: function(){
            axios.post("https://zarcos-web-be.herokuapp.com/lugar/",
                        this.lugar,
                        {headers:{}}
            ).then((result) => {
                let dataLugar = {
                    id : this.lugar.id,
                    lugar : this.lugar.ciudad,
                    direccion : this.lugar.direccion,
                    nombreLugar : this.lugar.nombreLugar,
                    complemento : this.lugar.complemento,
                }
                this.$emit('completedLugar', dataLugar)
                
            })
            .catch((error) => {
                  console.log(error); 
                  alert("Error en el registro");
                   
            });
        },
       
    }

}
    
</script>


<style>

    .signUp_lugar{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_lugar {
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .signUp_lugar h2{
        color: #283747;

    }

    .signUp_lugar form{
        width: 70%;
        
    }

    .signUp_lugar input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .signUp_lugar button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }

    .signUp_lugar button:hover{
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

