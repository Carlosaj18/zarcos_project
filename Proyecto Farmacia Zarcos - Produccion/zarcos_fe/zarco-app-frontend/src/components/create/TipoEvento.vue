<template>

    <div class="signUp_tipoEvento">

        <div class="container_tipoEvento">
            <h2> Tipo Evento </h2>
            <form v-on:submit.prevent="tipoEventoPost">
                <input type="text" v-model="tipoEvento.tipo_evento" placeholder="Tipo Evento">
                <br>                
                <button type="submit">POST TipoEvento</button>
            </form>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: 'TipoEvento',

    data:function(){
        return {
            tipoEvento:{
                tipo_evento:"",
            }
        }    
    },

    methods:{
        
        tipoEventoPost: function(){
            axios.post("https://zarcos-web-be.herokuapp.com/tipoEvento/",
                        this.tipoEvento,
                        {headers:{}}
            ).then((result) => {
                let dataTipoEvento = {
                    tipoEvento : this.tipoEvento.tipo_evento
                }
                this.$emit('completedTipoEvento', dataTipoEvento)
                
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

    .signUp_tipoEvento{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_tipoEvento {
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .signUp_tipoEvento h2{
        color: #283747;

    }

    .signUp_tipoEvento form{
        width: 70%;
        
    }

    .signUp_tipoEvento input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .signUp_tipoEvento button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }

    .signUp_tipoEvento button:hover{
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

