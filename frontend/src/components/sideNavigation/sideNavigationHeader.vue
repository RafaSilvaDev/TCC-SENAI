<template>
    <div class="m-side-navigation__header">

        <div class="m-side-navigation__header__label -size-l highlight">
            {{appName}}
        </div>

        <Button 
          type="button" 
          mode="integrated" 
          icon="list-view-mobile"
          :additionalClasses="['m-side-navigation__header__trigger -open']"
          @click="changeStateSideNavigation"
        />

        <Button 
          type="button" 
          mode="integrated" 
          icon="close"
          :additionalClasses="['m-side-navigation__header__trigger -close']"
          @click="changeStateSideNavigation"
        />

    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import Button from '@/components/button/Button.vue';

export default {
  props: ['appName'],
  components: {
    Button,
  },
  methods: {
    ...mapMutations([
      'changeStateSideNavigation',
    ]),
  }
};
</script>

<style src="./sideNavigation.scss" lang="scss"></style>