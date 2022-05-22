<template>
  <component :is="layout">
    <div :class="['patrols', { '-side-open': sideOpen }]">
      <div class="app">
        <div class="box">
          <div class="table-header">
            <p>Patrulheiros</p>
          </div>
          <div class="container">
            <Modal
              v-model="isModalVisible"
              @modalClicked="modalSelected($event)"
            />
            <Observation v-model:visible="isObservationVisible"
                v-model:data="observationResponse[buttonPosition[1]][buttonPosition[0]]"
                @modalClicked="obsSelected($event)" @verificationClicked="(status)=>{
                    if(status)
                      returnOptions(status)
                }"
                v-if="observationResponse.length > 0"
            />

            <table class="table-patrols" v-if="mounted">
              <tbody class="table-content">
                <tr id="calendar">
                  <th rowspan="2" id="header-question" style="padding: 5px">Questões</th>
                  <th colspan="7" id="mouth" style="flex">    
                    #
                  </th>
                </tr>
                
                <tr id="week">
                  <th># Segunda</th>
                  <th># Terça</th>
                  <th># Quarta</th>
                  <th># Quinta</th>
                  <th># Sexta</th>
                  <th># Sábado</th>
                  <th># Domingo</th>
                </tr>

                <tr

                  class="row-question"
                  style="height: 100px"
                  v-for="(q, index) in patrolData.fk_answers"
                  :key="q"
                >
                  <td id="question" style="padding: 5px">
                    {{ q.fk_patrolquest.question }} 
                    <!-- index + " - " + -->
                  </td>
                  
                  <td
                    id="check"
                    v-for="(b, b_index) in questionResponse.length"
                    :key="b_index"
                  >
                    <Button
                      :class="'btn' + questionResponse[b_index][index]"
                      @click="
                        () => {
                          buttonPosition[0] = index;
                          buttonPosition[1] = b_index;
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
    </div>
  </component>
</template>

<script>
import { mapState } from "vuex";

import Icon from "@/components/icon/Icon.vue";
import Modal from "@/components/modal/modal.vue";
import Observation from "@/components/modal/observation.vue";
import Button from "primevue/button";
import axios from "axios";
export default {
  data() {
    return {
      buttonPosition: [0, 0],
      isModalVisible: false,
      isObservationVisible: false,
      mounted: false,
      questionResponse: [],
      observationResponse: [],
      patrolData: {
    "id": 1,
    "fk_patrol": {
        "id": 1,
        "fk_team": [],
        "currentLevel": null,
        "user_img": "/media/users/default_user.png",
        "last_login": "2022-05-21T19:19:02.447910-03:00",
        "first_name": "",
        "last_name": "",
        "username": "admin",
        "email": "admin@admin.com",
        "edv": "",
        "birthDate": "2022-05-21",
        "is_staff": true,
        "is_superuser": true,
        "groups": [],
        "user_permissions": []
    },
    "fk_answers": [
        {
            "id": 30,
            "fk_patrolquest": {
                "id": 5,
                "question": "O piso está em boas condições?"
            },
            "answerDay": null,
            "answerBool": null,
            "answer": null,
            "fk_patrolweek": 1
        },
        {
            "id": 31,
            "fk_patrolquest": {
                "id": 6,
                "question": "Berços, Pallets, Caixas estão respeitando os limites dos corredores e estão organizados em seus lugares conforme demarcação?"
            },
            "answerDay": null,
            "answerBool": null,
            "answer": null,
            "fk_patrolweek": 1
        }
    ],
    "initialDate": "2022-05-21",
    "status": true
},
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
        "Os armários dos vestiários estão fechados adequadamente",
      ],
      
    };
  },
  methods: {
    returnOptions: function(status){
        console.log("teste ", status)
        this.isObservationVisible = false;
        this.isModalVisible = true;         
    },
    modalSelected: function (status) {
      if(status === false)
        this.isObservationVisible = true;
      else
        this.observationResponse[this.buttonPosition[1]][this.buttonPosition[0]] = null;
      console.log("clicou no evnto: " + status);
      this.questionResponse[this.buttonPosition[1]][this.buttonPosition[0]] =
        status;
      console.log(this.questionResponse); 
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
      
    },

    showModal() {
      if(this.observationResponse[this.buttonPosition[1]][this.buttonPosition[0]])   
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
        console.log(this.patrolData.fk_answers);
      })
      .catch((err) => {
        console.log(err);
      });
    },
  },
  created(){
    // this.getPatrolWeek()
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
    Button,
    Observation,
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