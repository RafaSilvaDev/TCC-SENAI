<template>
    <header class="o-minimal-header">
        <SideNavigation />
        <div class="o-minimal-header__supergraphic" />
        <div class="o-minimal-header__top">
            <div class="o-minimal-header__burger">
                <Button
                    mode="integrated"
                    icon="menu"
                    :isUiIcon="true"
                    @click="changeStateSideNavigation"
                />
            </div>
            <div class="o-minimal-header__title">{{nameRoute}}</div>
            <ul class="o-minimal-header__actions">
              <li>
                <Button mode="integrated" icon="sun-moon" @click="changeStateThemeMode"/>
              </li>
            </ul>
            <Logo component="o-minimal-header" @click="setLogout"/>
            <div className="o-minimal-header__falafel">
              
            </div>
        </div>
    </header>
</template>

<script>
import { mapMutations } from 'vuex';

import SideNavigation from '@/components/sideNavigation/SideNavigation.vue';
import Button from '@/components/button/Button.vue';
import Logo from '@/components/minimalHeader/parts/logo/Logo.vue';
import {logout} from '@/router/RouterBlock'

export default {
  components: {
    SideNavigation,
    Button,
    Logo,

  },
  computed: {
    nameRoute: function() { 
      let path = this.$route.path
      let appName = path.split('/')[1]
      return appName.toUpperCase(); 
    }
  },
  methods: {
    ...mapMutations([
      'changeStateSideNavigation',
      'changeStateThemeMode'
  ]),
    setLogout: function(){
      logout()
    }
  }
};
</script>


<style src="./minimalHeader.scss" lang="scss"></style>