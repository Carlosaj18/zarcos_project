<template>
  <div id="app" class="app">

    <div class="header">

      <img id="logo" src="./assets/imgs/logoFarmaciaGral.png" />
      <h1> Farmacia <br/> Zarcos </h1>
      <nav class="navbar navbar-green bg-green px-3">
        <button v-if="is_auth"  > Inicio </button>
        <button v-if="is_auth"  > Cuenta </button>
        <button v-if="is_auth"  > Cerrar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
        <!-- <button v-if="!is_auth" > Buscar categoria </button> -->
      </nav>  
    </div>

    <!-- Que esta haciendo los componentes del main? -->
    <div class="main-component">
      <!-- Me permite enrutar las vistas de login y signup, es un visualizador 
          y en ese espacio me puede colocar el resultado de esa redireccion del router y carga el 
          componente. Lo anterior pasa a partir de la funcion de JS que se complete-->
      <router-view 
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2> Misión TIC 2022</h2>
    </div>

  </div>
</template>

<script>
export default{
  name:'App',

  data:function(){
    /** Aqui se carga la data que necesito para correr se puede poner un valor por defecto
     * Se pueden poner todas las variables que se necesiten inicializar antes de la carga
     * Se puede usar data que se extrae de un sitio web
    */
    return{
      is_auth: false
    }
  },

  components: {

  },
  
  methods:{
    /** Todo lo que sea funcion de JS se van a poner aqui
     *  Cada funcion se separa por una coma ya que cada una es un elemento
     * Los metodos completedLogIn y completedSignUp usan el parametro de data anteriormente descrito 
     */
    verifyAuth: function(){
      if(this.is_auth == false)
        this.$router.push({name:'logIn'})
    },
    loadLogIn:function(){
      /** Accedo al router y cuando den click pongo a andar lo que este en login*/
      this.$router.push({name:'logIn'})
    },
    loadSignUp:function(){
      this.$router.push({name:'signUp'})
    },
    
    completedLogIn: function(data) {},
    completedSignUp: function(data) {},
  
  },
    
  created:function(){
    this.verifyAuth()
  }

}
</script>

<style>

body {
	margin:0 0 0 0; 
}
.header{
  margin:0 0 0 0; 
  padding:0;
  width:100%;
  height: 10vh;
  min-height: 100px;

  background-color: #063568;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h1{
  width: 20%;
  text-align: center;
}

.header nav {
    height: 100%;
    width: 20%;

    display: flex;
    justify-content: space-around;
    align-items: center;

    font-size: 20px;
  }

  .header nav button{
    color: #E5E7E9;
    background: #283747;
    border: 1px solid #E5E7E9;

    border-radius: 10px;
    padding: 10px 20px;
  }

  .header nav button:hover{
    color: #283747;
    background: #E5E7E9;
    border: 1px solid #E5E7E9;
  }

  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;
    background: #FDFEFE ;
  }

 
  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px; 

    background-color: #283747;
    color: #E5E7E9;

  }

  .footer h2{
    width: 100%;
    height: 100%;
    
    display: flex;
    justify-content: center;
    align-items: center;
  }

</style>