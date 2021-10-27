import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Category from './components/create/Category.vue'
import Lugar from './components/create/Lugar.vue'
import TipoEvento from './components/create/TipoEvento.vue'
import ListaCategory from './components/elements/ListaCategory.vue'
import ListaLugar from './components/elements/ListaLugar.vue'
import ListaTipoEvento from './components/elements/ListaTipoEvento.vue'
import ListaPersonas from './components/elements/ListaPersonas.vue'
import ListaEventos from './components/elements/ListaEventos.vue'
import ListaInscripciones from './components/elements/ListaInscripciones.vue'
import vistaEventos from './components/evento/vistaEventos.vue'
import eventoDetails from './components/evento/eventoDetails.vue'

/** Seran los endpoints del app */
const routes = [{
        path: '/',
        name: 'root',
        component: App
    }, 
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/signUp',
        name: "signUp",
        component: SignUp
    },
    {        
        path: '/user/home',
        name: "home",
        component: Home
    },
    { 
        path: '/create/category',
        name: "Category",
        component: Category
    },
    {
        path: '/create/lugar',
        name: "Lugar",
        component: Lugar
    },
    {
        path: '/create/tipoEvento',
        name: "TipoEvento",
        component: TipoEvento
    }, 
    {
        path: '/listacategory',
        name: "ListaCategory",
        component: ListaCategory
    },
    {
        path: '/listalugar',
        name: "ListaLugar",
        component: ListaLugar
    },
    {
        path: '/listatipoevento',
        name: "ListaTipoEvento",
        component: ListaTipoEvento
    },
    {
        path: '/listapersonas',
        name: "ListaPersonas",
        component: ListaPersonas
    },
    {
        path: '/listaeventos',
        name: "ListaEventos",
        component: ListaEventos
    },
    {
        path: '/listainscripciones',
        name: "listaInscripciones",
        component: ListaInscripciones
    },
    {
        path: '/home/eventos',
        name: "vistaEventos",
        component: vistaEventos
    },
    {
        path: '/eventos/details',
        name: "eventoDetails",
        component: eventoDetails
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router