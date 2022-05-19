<template>
  <Dialog  class="" :dismissableMask="true" v-model:visible="modelValue" @hide="$emit('update:modelValue', false)">
    <template #header>
      <h4>Verificação</h4>
    </template>

    Escolha uma das opções:

    <template #footer>
      <div class="buttons">
        <Button id="no"  icon="pi pi-times" @click="()=>{
          $emit('modalClicked', false)
          $emit('update:modelValue', false)
          }"/>
        <Button id="yes" icon="pi pi-check" @click="()=>{
          $emit('modalClicked', true)
          $emit('update:modelValue', false)
          }" />
      </div>
    </template>
  </Dialog>
</template>

<script>
import Dialog from "primevue/dialog";
import Button from 'primevue/button';

export default {
  name: "Modal",
  props: ["modelValue"],
  emits: ["update:modelValue", "modalClicked"],
  data() {
    return {
      display: true,
    };
  },
  methods:{
    
  },
  components: {
    Dialog,
    Button,
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
  
  .buttons{
    width: 100%;
    display: flex;

    #yes{
    float: right;
    width: 50%;
    outline: none;
    border: none;
    background-color: $button-color-m;
    }
    #no{
    float:left;
    width: 50%;
    outline: none;
    border: none;
    background-color: $button-color-m;
    }
  }

</style>