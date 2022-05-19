<template>
    <component :is="layout">

        <div class="login"></div>
        
    </component>
</template>

<script>
// import Message from "@/components/msg/error.vue"

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