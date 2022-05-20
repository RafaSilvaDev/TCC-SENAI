<template>
    <form className="m-search-form" action="javascript:void(0);" autoComplete="off">
        <TextField
            type="search"
            :id="`search-${name ? name.toLowerCase().replace(/\s/g, '-') : null}`"
            placeholder="Search"
            :withReset="withReset"
            @searchClick="setSearchValue"
        />
    </form>
</template>

<script>
import TextField from '@/components/textField/TextField.vue';

export default {
    data: function() {
        return {
            searchValue: '',
        }
    },
    emits: ['getSearchValue'],
    props: [
        'withReset',
        'id',
        'name',
    ],
    components: {
        TextField
    },
    methods: {
        setSearchValue: function(n) {
            this.searchValue = n
        }
    },
    watch: {
        searchValue(newVal, oldVal) {
            this.$emit('getSearchValue', newVal)
        }
    }

}
</script>

<style src="./searchForm.scss" lang="scss"></style>