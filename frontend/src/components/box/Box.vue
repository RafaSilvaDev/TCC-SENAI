<template>
    <div :class="['a-box--modal', {'-show':show}]">
        <div class="a-box -floating">
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Box',
    props: ['show']
}
</script>

<style src="./box.scss" lang="scss"></style>