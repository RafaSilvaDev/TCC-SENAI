<template>
    <div :class="classes">
        <div class="a-activity-indicator__top-box" />
        <div class="a-activity-indicator__bottom-box" />
    </div>
</template>

<script>
export default {
    name: 'ActivityIndicator',
    props: ['size'],
    computed: {
        classes: function() {
            return [ 
                'a-activity-indicator', {[ `-${this.size}` ]: this.size}
            ]
        }
    }
}
</script>

<style src="./activityIndicator.scss" lang="scss"></style>