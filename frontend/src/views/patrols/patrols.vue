<template>
  <component :is="layout">
    <div :class="['patrols', { '-side-open': sideOpen }]">
      <div class="app">
        <div class="box">
          <div class="table-header">
            <h4>Patrulheiros</h4>
            <Button @click="() => {
                         isDetailsVisible = true
                        }" 
                        mode="primary" label="Modal"/>

            <Details v-model:visible="isDetailsVisible" />
          </div>
          <div class="container">
            <Modal
              v-model="isModalVisible"
              @modalClicked="modalSelected($event)"
            />
            <Observation v-model:visible="isObservationVisible"
                v-model:data="this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answer"
                @modalClicked="obsSelected($event)" @verificationClicked="(status)=>{
                    if(status)
                      returnOptions(status)
                }"
                v-if="observationResponse.length > 0"
            />

            <table class="table-patrols" v-if="mounted">
              <tbody class="table-content">
                <tr id="calendar" >
                  <th rowspan="2" id="header-question" style="padding: 5px">Questões</th>
                  <th colspan="7" id="mouth" style="flex;">
                    {{patrolData.fk_days[0].cDate.slice(0, 4)}}
                  </th>
                </tr>
                
                <tr id="week">
                  <th v-for="day in patrolData.fk_days" :key="day" >{{days[patrolData.fk_days.indexOf(day)]}} - {{day.cDate.slice(8, 10)}}/{{day.cDate.slice(5, 7)}}</th>
                  
                </tr>

                <tr

                  class="row-question"
                  style="height: 100px"
                  v-for="(q, index) in patrolData.fk_days[0].fk_answers"
                  :key="q"
                >
                  <td class="side-header" id="question" style="padding: 5px; position: sticky; left:0; z-index: 2; background: var(--background)">
                    {{index + 1}} - {{ q.fk_patrolquest.question }}
                    <!-- index + " - " + -->
                  </td>
                  
                  <td
                    id="check"
                    v-for="(b, b_index) in this.patrolData.fk_days.length"
                    :key="b_index"
                  >
                    <Button
                      :class="'btn' + this.patrolData.fk_days[b_index].fk_answers[index].answerBool"
                      @click="
                        () => {
                          buttonPosition[0] = b_index;
                          buttonPosition[1] = index;
                          showModal();
                        }
                      "
                    >
                    </Button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        
      </div>
      <Button @click="sendData()" mode="primary" label="Save"/>
    </div>
  </component>
</template>

<script>
import { mapState } from "vuex";

import Icon from "@/components/icon/Icon.vue";
import Button from "@/components/button/Button.vue";
import Modal from "@/components/modal/modal.vue";
import Observation from "@/components/modal/observation.vue";
import Details from "@/components/modal/details.vue";
import ButtonPrime from "primevue/button";
import axios from "axios";


export default {
  data() {
    return {
      buttonPosition: [0, 0],
      isModalVisible: false,
      isObservationVisible: false,
      isDetailsVisible: false,
      mounted: false,
      questionResponse: [],
      observationResponse: [],
      patrolData: {},
      days: ["Segunda", "Terça", "Quarta","Quinta", "Sexta", "Sábado", "Domingo"],
      questions:[],
      answers:[],
      questions2: [
        "O piso está em boas condições?",
        "Berços, Pallets, Caixas estão respeitando os limites dos corredores e estão organizados em seus lugares conforme demarcação?",
        "Há vazamento de ar comprimido?",
        "Os extintores e portas de emergência estão desobstruidas e sinalizadas?",
        "Os painéis elétricos estão trancados e sinalizados?",
        "A fiação elétrica está em bom estado de conservação?",
        "Há vazamento de óleo/produtos químicos?",
        "Os armários de produtos químicos estão limpos, organizados e fechados?",
        "Os produtos químicos (todos) estão armazenados em recipientes adequados e identificados com norma, nome e simbologia de risco?",
        "Os produtos químicos tóxicos e explosivos estão armazenados em armários de acesso restrito e estão identificados, trancados/chaveados?",
        "Existem bandejas nos locais de armazenamento de produtos químicos (armários TPM ou tambores)?",
        "Os colaboradores estão usando os EPI's e isentos de adornos?",
        "A Coleta Seletiva esta sendo realizada de forma correta?",
        "Existem garrafas de água ou alimentos nos postos de trabalho?",
        "As ferramentas manuais estão em bom estado de conservação e sem improvisação?",
        "Os armários dos vestiários estão fechados adequadamente?",
      ],
      
    };
  },
  methods: {
    returnOptions: function(status){
        console.log("teste ", status)
        this.isDetailsVisible = true; 
        this.isObservationVisible = false;
        this.isModalVisible = true; 

    },
    sendData: async function (){
      await axios
      
      .put(this.apiURL+"/patrolweek/", this.patrolData)
      .then((response) => {
        this.patrolData = response.data;
        // this.questions = this.results.fk_answers
        console.log(this.patrolData);
        document.location.reload(true);

      })
      .catch((err) => {
        console.log(err);
      });
    },
    modalSelected: function (status) {
      if(status === false)
        this.isObservationVisible = true;
      else
        this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answer = null;
      console.log("clicou no evnto: " + status);
      //row = this.buttonPosition[1];
      // column = this.buttonPosition[0]
      this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answerBool = status
      // this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answer
      // console.log(this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answerBool)
      this.questionResponse[this.buttonPosition[0]][this.buttonPosition[1]] = status;
      
      console.log("testeeeeeeeeeeee")
      console.log(this.buttonPosition[1])
      console.log(this.buttonPosition[0])
      console.log(this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answer)
      // console.log(this.questionResponse); 
      console.log(this.patrolData)
    },
    obsSelected: function (obs){
      console.log('obs');
      console.log(obs);
      // this.observationResponse[this.buttonPosition[1]][this.buttonPosition[0]] = obs;
      console.log("this.observationResponse")
      console.log(this.observationResponse)
    },
    fillResponseQuestion: function () {
      for (let x = 0; x < 7; x++) {
        this.questionResponse.push(this.questions.map(() => null));
        this.observationResponse.push(this.questions.map(() => null))
      }
      // observationResponse[buttonPosition[1]][buttonPosition[0]]
    },

    showModal() {
      if(!this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answerBool && this.patrolData.fk_days[this.buttonPosition[0]].fk_answers[this.buttonPosition[1]].answerBool !== null)   
      this.isObservationVisible = true  
      else
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },

    getPatrolWeek: async function (){
      await axios
      .get(this.apiURL+"/patrolweek/")
      .then((response) => {
        this.patrolData = response.data;
        // this.questions = this.results.fk_answers
        console.log(this.patrolData);
      })
      .catch((err) => {
        console.log(err);
      });
    },
  },
  created(){
    this.getPatrolWeek()
  },
  mounted() {
    for (let row = 0; row < 16; row++) {}
    
    this.fillResponseQuestion();
    this.mounted = true;
    // console.log(this.questionResponse);
  },
  computed: mapState({
    sideOpen: (state) => state.sideNavigationOpen,
  }),
  components: {
    Icon,
    Modal,
    ButtonPrime,
    Button,
    Observation,
    Details,
  },

  setup: function() {
    const layout = 'default-layout'

    return {
      layout
    }
  }
};
</script>

<style src="./patrols.scss" lang="scss" >
</style>