<template>
    <i :class="classes" />
</template>

<script>
export default {
  props:{
    'iconName': null,
    'titleText': null,
    'className': '',
    'isUiIcon': false,
  },
  computed: {
    classes: function() {
      return [
        'a-icon',
        {
          [this.className]: this.className,
          [`boschicon-bosch-ic-${this.iconName}`]: this.iconName && !this.isUiIcon,
          [`ui-ic-${this.iconName}`]: this.iconName && this.isUiIcon,
        }
      ]
    }
  }
};
</script>

<style src="./icon.scss" lang="scss"></style>