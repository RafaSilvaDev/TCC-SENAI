<template>
    <button
        :type="type"
        :class="classes"
    >
      <Icon v-if="icon" :iconName="icon" className="a-button__icon" :isUiIcon="isUiIcon" />
      <div v-if="label" class="a-button__label">{{label}}</div>
    </button>
</template>

<script>
import Icon from '@/components/icon/Icon.vue';

export default {
  props:{
    'type': { default:'button' },
    'mode': { default:'primary' },
    'label': null,
    'icon': null,
    'additionalClasses': [],
    'isUiIcon': false
  },
  computed: {
    classes: function() {
      return [
        'a-button',
        {
          [`a-button--${this.mode}`]: this.mode,
        '-without-icon': this.label && !this.icon,
        '-without-label': this.icon && !this.label
        },
        this.additionalClasses
      ]
    }
  },
  components: {
    Icon
  }
};
</script>

<style src="./button.scss" lang="scss"></style>