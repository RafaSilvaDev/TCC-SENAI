<template>
    <div id="layout" :class="classes">

        <div class="background_full -primary">
            <MinimalHeader />
          
            <div class="background-wrapper" :class="[ 'sgi', {'-side-open': sideOpen} ]">
              <div class="background-internal">
                <slot></slot>
              </div>
            </div>
        </div>

    </div>
</template>

<script>
import { mapState } from 'vuex';
import MinimalHeader from '@/components/minimalHeader/MinimalHeader.vue';

export default {
  computed: {
    classes: function(){
      return [
        this.darkMode ? '-dark-mode' : '-light-mode'
      ]
    },
    ...mapState({
      darkMode: state => state.darkMode,
      sideOpen: state => state.sideNavigationOpen,
    }),
  },
  components: {
    MinimalHeader,
  }
};
</script>

<style src="./default.scss" lang="scss"></style>