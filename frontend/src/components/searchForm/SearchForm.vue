<template>
    <form className="m-search-form" action="javascript:void(0);" autoComplete="off">
        <TextField
            type="search"
            :id="`search-${name ? name.toLowerCase().replace(/\s/g, '-') : null}`"
            placeholder="Search"
            :withReset="withReset"
        />
    </form>
</template>

<script>
import TextField from '@/components/textField/TextField.vue';

export default {
    props: [
        'withReset',
        'id',
        'name',
    ],
    components: {
        TextField
    },

}
</script>

<style src="./searchForm.scss" lang="scss"></style>