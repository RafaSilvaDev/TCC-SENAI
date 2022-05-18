<template>
    <div id="layout">
      <header class="header-login">
        <div class="o-minimal-header__supergraphic" />
        <Logo component="o-minimal-header" />
      </header>

      <div class="container-login">
        <div class="content">

          <h3>Login</h3>

          <form submit.prevent="">

            <div class="a-text-field">
              <label>User</label>
              <input type="text" name="user">
            </div>
            <div class="a-text-field">
              <label>Password</label>
              <input :type="type" name="pwd">
              <button type="button" class="a-text-field__icon-password" @click="showPwd=!showPwd">
                <Icon iconName="watch-on" />
              </button>
            </div>

            <Button type="submit" mode="primary" label="Login"/>

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


export default {
  data: function() {
    return {
        showPwd: false,
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
  }
};
</script>

<style src="./login.scss" lang="scss"></style>