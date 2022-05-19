<template>
<Dialog v-model:visible="modelValue" @hide="$emit('update:visible', false)"
 @show="modalShowed">
  <template #header>
      <h4>Observação</h4>
  </template>

  <Textarea v-model="obsValue" :autoResize="true" rows="5" cols="30" />

  <template #footer>
      <div class="buttons">
        <Button id="arrow-left"  icon="pi pi-arrow-left" 
        @click="() => {
          $emit('verificationClicked', true)
          }"/>

        <Button id="save"  icon="pi pi-save"
        @click="()=>{ 
          $emit('modalClicked', obsValue)
          $emit('update:visible', false)
          $emit('update:data', obsValue)
          
          }"/>
      </div>
  </template>
</Dialog> 
</template>

<script>
import Dialog from "primevue/dialog";
import Button from 'primevue/button';
import Textarea from 'primevue/textarea';
import Modal from "@/components/modal/modal.vue";

export default{
  props: ["modelValue", "data"],
  emits: ["update:modelValue", "modalClicked", "update:data", "verificationClicked"],
  data() {
    return{
      obsValue: ''
    }
  },
  components: {
    Dialog,
    Button,
    Textarea,
    Modal,
  },
  methods:{
    modalShowed: function(){
      console.log(this.$props.data)
      this.obsValue = this.$props.data;   
    }
  }
};  
</script>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
  
.buttons{
  display: flex;
  justify-content: space-between;

  #arrow-left, #save{
    width: 50px;
    height: 50px;
    background-color: $button-color-m;
  }
  
}
  
</style>
