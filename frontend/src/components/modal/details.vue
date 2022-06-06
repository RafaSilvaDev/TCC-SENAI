<template>
  <Dialog>

    <template #header>
      <h4>Nova Semana</h4>
    </template>

    <div class="body">
      <p v-if="fillAll" class="little_alert">Preencha todos os campos</p>
      <!-- <Dropdown placeholder="Select a patrols"></Dropdown>
      <Calendar style="margin-top:20px;"></Calendar> -->
      <select v-model="patrolsData.fk_patrol" class="select_patrol" name="" id="">
        <option v-for="x in patrols" :key="x.id" :value="x.id">{{x.username}}</option>
      </select>

      <input v-model="patrolsData.initialDate" type="date" class="date_inpt">
    </div>
    
    <template #footer>
      
      <Button id="save" icon="pi pi-save" v-if="!sended" @click="()=>{
          sendNewWeek()
        }"/>
        <img v-else src="@/assets/img/loading.gif" alt="" style="width: 30px">
      
    </template>
  </Dialog>

</template>

<script>
import Dialog from "primevue/dialog";
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import Calendar from 'primevue/calendar';
import axios from "axios";
export default {
  
  data() {
    return {
      display: true,
      patrols: [],
      lastId: null,
      sended: false,
      fillAll: false,
      patrolsData: {
        fk_days: [],
        fk_patrol: null,
        initialDate: null
      }
    };
  },
  methods:{
    getPatrols: async function(){
      await axios.get(this.apiURL + '/simpleusers/').then(response =>{
        this.patrols = response.data.results
        console.log(response.data)
      })
    },
    sendNewWeek: async function(){
      if(this.patrolsData.fk_patrol !== null && this.patrolsData.initialDate !== null){
        this.sended = true
        this.fillAll = false
        console.log(this.patrolsData)
        await axios.post(this.apiURL + '/patrolweek/',this.patrolsData).then(response =>{
          console.log(response.data)
          this.lastId = response.data.id
        }).catch(error => console.log(error))

        if(this.lastId !== null){
          await axios.post(this.apiURL + '/generate/' + this.lastId ,this.patrolsData).then(response =>{
            console.log(response.data)
          }).catch(error => console.log(error))
        }
        this.sended=false
        document.location.reload(true);
      }else{
        this.fillAll = true
      }
    }
  },
  
  components: {
    Dialog,
    Button,
    Dropdown,
    Calendar
  },
  mounted(){
    this.getPatrols()
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
.body{
  display: flex;
  flex-direction: column;
}
.little_alert{
  color: red
}
#save{
  width: 50px;
  height: 50px;
  background-color: $button-color-m;
  margin-top: 0;
}
.date_inpt{
  width: 100%;
  height: 40px;
  outline: 0;
  border: none;
  margin-top: 10px;
  border-bottom: black 1px solid;
  
}
.select_patrol{
  width: 100%;
  height: 40px;
  border:none;
  border-bottom: black 1px solid;
  outline: 0;
  

}
.blackout_patrols{
  background-color: rgba(0, 0, 0, 0.3);
  position: absolute; top: 0; left: 0;
  z-index: 200;
  width: 100vw;
  height: 100vh;
  display:flex;
  justify-content: center;
  align-items: center;
  img{
    width: 50px;
  }
}
</style>
