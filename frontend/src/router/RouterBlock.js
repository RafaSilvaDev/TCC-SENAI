import axios from 'axios'
import router from './index';
import store from '../store';

let baseURL = "http://localhost:8000/"

export async function setLogin(login){
    await axios.post(baseURL + 'auth/jwt/create/',login).then(response => (
        //store.commit('setToken', [response.data.access, response.data.refresh]),
        localStorage.aToken = response.data.access,
        localStorage.rToken = response.data.refresh,
        router.push('/home')
    )).catch(error => {
        router.go(router.currentRoute)
    })
}

export async function checkLogin(){
    let token = localStorage.aToken
    await axios.post(baseURL + 'auth/jwt/verify/', {"token": token}).then(response => {
        // console.log(response)
    }).catch(error => {
        console.log(error)
        router.push("/login")
    })
}

export async function logout(){
    localStorage.removeItem('aToken')
    localStorage.removeItem('rToken')
    router.go(router.currentRoute)
}