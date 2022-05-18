import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import DefaultLayout from './components/layouts/default/Default';
import LoginLayout from './components/layouts/login/Login';



createApp(App)
  .component('default-layout', DefaultLayout)
  .component('login-layout', LoginLayout)
  .use(store)
  .use(router)
  .mount('#app');
