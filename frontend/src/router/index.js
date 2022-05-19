import { createRouter, createWebHistory } from 'vue-router';

import DDS from '../views/sgi/dds/DDS.vue';
import AMA from '../views/sgi/ama/AMA.vue';
import BAST from '../views/sgi/bast/BAST.vue';
import Agenda from '../views/agenda/Agenda.vue';
import Login from '../views/login/Login.vue';
import Home from '../views/home/Home.vue';
import Patrols from '../views/patrols/patrols.vue';
import Error404 from '../views/404/404.vue';

import { checkLogin } from '@/router/RouterBlock'


const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/sgi/dds',
    name: 'DDS',
    component: DDS,
  },
  {
    path: '/sgi/ama',
    name: 'AMA',
    component: AMA
  },
  {
    path: '/sgi/bast',
    name: 'BAST',
    component: BAST
  },
  {
    path: '/agenda',
    name: 'Agenda',
    component: Agenda
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/patrols',
    name: 'Patrols',
    component: Patrols
  },
  {
    path: '/404',
    name: 'Error404',
    component: Error404
  },
  
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.afterEach((to, from) => {
  if(to.name === undefined){
    router.push("home")
  }

  if(to.name !== "Login"){    
    checkLogin()
  }
  
});

export default router
