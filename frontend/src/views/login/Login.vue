<template>
    <component :is="layout">
        <div class="login"></div>
    </component>
</template>

<script>
export default {
    setup: function() {
        const layout = 'login-layout';
        
        return {
        layout
        };
    },
}
</script>

<style src="./login.scss" lang="scss"></style>