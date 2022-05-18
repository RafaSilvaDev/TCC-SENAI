<template>
    <div :class="[ 'm-side-navigation', [sideOpen ? '-open' : '-close'] ]">

        <SideNavigationHeader appName="ERP ETS" />
        <ul class="m-side-navigation__menuItems">
          <li :class="['m-side-navigation__menuItem', {'-open': openSGI}]" role="none" @click="changeStateSGI">
            <button type="button" class="m-side-navigation__group">
              <Icon iconName="molecule" />
                <span class="m-side-navigation__label">
                  SGI
                </span>
              <Icon iconName="down" titleText="down" class="arrow" />
            </button>
            <ul className="m-side-navigation__menuSubitems" role="menu">
              <li class="m-side-navigation__menuSubitem" role="none">
                <router-link
                  to="/sgi/dds"
                  role="menuItem"
                  class="m-side-navigation__link"
                >
                  <span class="m-side-navigation__label">
                    DDS
                  </span>
                </router-link>
              </li>
              <li class="m-side-navigation__menuSubitem" role="none">
                <router-link
                  to="/sgi/ama"
                  role="menuItem"
                  class="m-side-navigation__link"
                >
                  <span class="m-side-navigation__label">
                    AMA
                  </span>
                </router-link>
              </li>
              <li class="m-side-navigation__menuSubitem" role="none">
                <router-link
                  to="/sgi/bast"
                  role="menuItem"
                  class="m-side-navigation__link"
                >
                  <span class="m-side-navigation__label">
                    BAST
                  </span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="m-side-navigation__menuItem" role="none">
            <router-link to="/agenda" role="menuitem" class="m-side-navigation__link">
              <i class="a-icon boschicon-bosch-ic-login" title="Login"></i>
              <span class="m-side-navigation__label">Agenda</span>
            </router-link>
          </li>
        </ul>

    </div>
</template>

<script>
import { mapState } from 'vuex';

import SideNavigationHeader from '@/components/sideNavigation/sideNavigationHeader.vue';
import Icon from '@/components/icon/Icon.vue';
import Button from '@/components/button/Button.vue';


export default {
  data: function() {
    return {
      openSGI: false,
    }
  },
  computed: mapState({
    sideOpen: state => state.sideNavigationOpen,
  }),
  methods: {
    changeStateSGI: function(){
      this.openSGI = !this.openSGI;
    }
  },
  components: {
    SideNavigationHeader,
    Icon,
    Button
  }
};
</script>

<style src="./sideNavigation.scss" lang="scss"></style>