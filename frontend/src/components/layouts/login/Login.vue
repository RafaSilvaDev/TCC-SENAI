<template>
    <div id="layout">
      <header class="header-login">
        <div class="o-minimal-header__supergraphic" />
        <Logo component="o-minimal-header" />
      </header>

      <div class="container-login">
        <div class="content">

          <h3>Login</h3>

          <form v-on:submit.prevent="loginUser">

            <div class="a-text-field">
              <label>User</label>
              <input v-model="login.username" type="text" name="user">
            </div>
            <div class="a-text-field">
              <label>Password</label>
              <input v-model="login.password" :type="type" name="pwd">
              <button type="button" class="a-text-field__icon-password" @click="showPwd=!showPwd">
                <Icon iconName="watch-on" />
              </button>
            </div>

            <Button v-if="!inLoading" type="submit" mode="primary" label="Login"/>
            <div v-else class="load_alert">
              <img class="load_alert_img"  src="@/assets/img/loading.gif" alt="">
            </div>
            <p class="erro_alert" v-if="$route.params.error">Usuário ou senha Inválidos</p>
          </form>

        </div>
      </div>
    </div>
</template>

<script>
import Logo from '@/components/minimalHeader/parts/logo/Logo.vue';
import Icon from '@/components/icon/Icon.vue';
import TextField from '@/components/textField/TextField.vue';
import Button from "@/components/button/Button.vue";

import { setLogin } from '@/router/RouterBlock'

export default {
  
  data: function() {
    return {
        showPwd: false,
        login:{
          username: 'admin',
          password: 'admin1234567 '
        },
        error: true,
        inLoading: false
    }
  },
  computed: {
    type: function() {
      return ( this.showPwd ? 'text' : 'password' )
    },
  },
  components: {
    Logo,
    TextField,
    Icon,
    Button
  },
   methods:{
    loginUser: async function(){
      this.inLoading = true
      await setLogin(this.login)
      this.inLoading = false
    }
  },
  created(){
    // this.inLoading = !this.$route.params.error
  }
};
</script>

<style src="./login.scss" lang="scss"></style>