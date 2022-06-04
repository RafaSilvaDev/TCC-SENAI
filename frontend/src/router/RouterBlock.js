import axios from 'axios'
import router from './index';
import store from '../store';

const baseURL = "https://etsweberp.azurewebsites.net/"


// export async function checkSuper(user){
//     await axios.get(baseURL + 'apiv1/checkuser/' + user).then(response =>{
//         console.log(response.data.data)
//         localStorage.super = response.data.data
//     })
// }

export async function setLogin(login){
    await axios.post(baseURL + 'auth/jwt/create/',login).then(async (response) => (
        // store.commit('setToken', [response.data.access, response.data.refresh]),
        localStorage.aToken = response.data.access,
        localStorage.rToken = response.data.refresh,
        localStorage.user = login.username,
        // await checkSuper(login.username),
        
        router.push('/home')
    )).catch(error => {
        router.push({ name: 'Login', params: { error: true }})
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

export async function Logout(){
    localStorage.removeItem('aToken')
    localStorage.removeItem('rToken')
    localStorage.removeItem('user')
    localStorage.removeItem('rToken')
    localStorage.removeItem('super')
    router.go("Login")
}