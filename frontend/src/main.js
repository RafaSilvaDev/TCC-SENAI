import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import PrimeVue from 'primevue/config'
import DefaultLayout from './components/layouts/default/Default';
import LoginLayout from './components/layouts/login/Login';



let app = createApp(App)
  app.component('default-layout', DefaultLayout)
  app.component('login-layout', LoginLayout)
  app.use(store)
  app.use(router)
  app.use(PrimeVue)
  app.config.globalProperties.apiURL = 'http://127.0.0.1:8000/apiv1'
  app.mount('#app');
