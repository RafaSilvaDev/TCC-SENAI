<template>
  <Dialog>
    <template #header>
      <h4>Patrulheiros</h4>
    </template>

    <div class="body">
      <Dropdown placeholder="Select a patrols"></Dropdown>
      <Calendar style="margin-top:20px;"></Calendar>
    </div>
    
    <template #footer>
      <Button id="save" icon="pi pi-save" @click="()=>{}"/>
    </template>
  </Dialog>
</template>

<script>
import Dialog from "primevue/dialog";
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import Calendar from 'primevue/calendar';

export default {
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
    Dropdown,
    Calendar
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
.body{
  display: flex;
  flex-direction: column;
}
#save{
  width: 50px;
  height: 50px;
  background-color: $button-color-m;
}
</style>
