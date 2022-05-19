<template>
    <component :is="layout">
        <div class="login"></div>
    </component>
</template>

<script>
export default {
    mounted(){},
    setup: function() {
        const layout = 'login-layout';

        return {
            layout
        };
    },
}
</script>

<style src="./login.scss" lang="scss"></style>