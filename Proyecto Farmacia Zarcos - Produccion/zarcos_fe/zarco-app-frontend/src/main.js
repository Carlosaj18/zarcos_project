import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

/** Usa el router que saco del archivo y se lo pasa como una funcionalidad a APP */
createApp(App).use(router).mount('#app')