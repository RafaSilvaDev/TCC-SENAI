<template>
    <div :class="classes">
      <label v-if="label" :for="id">{{label}}</label>
      <input
        :type="typeC"
        :id="id"
        :disabled="disabled"
        :placeholder="placeholder"
        v-model="searchValue"
      />
      
        <button v-if="isPassword" type="button" class="a-text-field__icon-password" @click="showPwd=!showPwd">
          <Icon iconName="watch-on" />
        </button>

        <button v-if="isSearch" type="submit" class="a-text-field__icon-search" @click='$emit("searchClick", searchValue)'>
            <Icon titleText="LoremIpsum" iconName="search"/>
        </button>
        <button v-if="withReset" type="button" class="a-text-field__icon-close" @click='closeSearch'>
            <Icon className="a-button__icon" iconName="close" />
        </button>

    </div>
</template>

<script>
import Icon from '@/components/icon/Icon.vue';

export default {
    emits: ["searchClick"],
    props: [
        'withReset',
        'disabled',
        'id',
        'placeholder',
        'label',
        'type'
    ],
    data: function() {
        return {
            showPwd: false,
            searchValue: '',
        }
    },
    computed: {
        typeC: function() {
            return ( this.type=='password' ? (this.showPwd ? 'text' : this.type) : this.type)
        },
        isPassword: function() {
            return this.type == 'password';
        },
        isSearch: function() {
            return this.type == 'search';
        },
        classes: function() {
            return [
                'a-text-field',
                { 'a-text-field--password': this.isPassword },
                { 'a-text-field--search': this.isSearch },
            ]
        }
    },
    methods: {
        closeSearch: function() {
            this.searchValue = ''
            this.$emit("searchClick", "")
        }
    },
    components: {
        Icon
    }
}
</script>

<style src="./textField.scss" lang="scss"></style>