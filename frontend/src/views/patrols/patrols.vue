<template>
  <component :is="layout">
    <div :class="['patrols', { '-side-open': sideOpen }]">
      <div class="app">
        <div class="box">
          <div class="table-header">
            <h4>Patrulheiros</h4>
          </div>
          <div class="container">
            <Modal
              v-model="isModalVisible"
              @modalClicked="modalSelected($event)"
            />
            <Observation
              v-model:visible="isObservationVisible"
              v-model:data="
                observationResponse[buttonPosition[1]][buttonPosition[0]]
              "
              @modalClicked="obsSelected($event)"
              @verificationClicked="
                (status) => {
                  if (status) returnOptions(status);
                }
              "
              v-if="observationResponse.length > 0"
            />

            <table class="table-patrols" v-if="mounted">
              <tbody class="table-content">
                <tr id="calendar">
                  <th rowspan="2" id="header-question" style="padding: 5px">
                    Questões
                  </th>
                  <th colspan="7" id="mouth" style="flex">#</th>
                </tr>

                <tr id="week">
                  <th>{{ weekDates[0] }} Segunda</th>
                  <th>{{ weekDates[1] }} Terça</th>
                  <th>{{ weekDates[2] }} Quarta</th>
                  <th>{{ weekDates[3] }} Quinta</th>
                  <th>{{ weekDates[4] }} Sexta</th>
                  <th>{{ weekDates[5] }} Sábado</th>
                  <th>{{ weekDates[6] }} Domingo</th>
                </tr>

                <tr
                  class="row-question"
                  v-for="(q, index) in questions"
                  :key="index"
                >
                  <td id="question" style="padding: 5px">
                    {{ q.question }}
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
import moment from "moment";

export default {
  data() {
    return {
      currentDate: "",
      weekDates: [],
      buttonPosition: [0, 0],
      isModalVisible: false,
      isObservationVisible: false,
      mounted: false,
      questionResponse: [],
      observationResponse: [],
      questions: [],
    };
  },
  methods: {
    returnOptions: function (status) {
      console.log("teste ", status);
      this.isObservationVisible = false;
      this.isModalVisible = true;
    },
    returnQuestions: function () {
      axios.get(this.apiURL + "/patrolquests/").then((response) => {
        let data = response.data;
        this.questions = data.results;
        this.next = data.next;
        this.previous = data.previous;
        this.count = data.count;

        console.log(data.results);
      });
    },

    dates: function () {
      let weekDates = [];

      function getThisWeekDates() {
        var weekDates = [];

        for (var i = 1; i <= 7; i++) {
          weekDates.push(moment().day(i));
        }
        return weekDates;
      }

      var thisWeekDates = getThisWeekDates();
      thisWeekDates.forEach(function (date) {
        let cDate = date.format("DD/MM");
        weekDates.push(cDate);
      });
      this.weekDates = weekDates;
      console.log(this.weekDates);
    },

    modalSelected: function (status) {
      if (status === false) this.isObservationVisible = true;
      else
        this.observationResponse[this.buttonPosition[1]][
          this.buttonPosition[0]
        ] = null;
      console.log("clicou no evnto: " + status);
      this.questionResponse[this.buttonPosition[1]][this.buttonPosition[0]] =
        status;
      console.log(this.questionResponse);
    },
    obsSelected: function (obs) {
      console.log("obs");
      console.log(obs);
      // this.observationResponse[this.buttonPosition[1]][this.buttonPosition[0]] = obs;
      console.log("this.observationResponse");
      console.log(this.observationResponse);
    },
    fillResponseQuestion: function () {
      for (let x = 0; x < 7; x++) {
        this.questionResponse.push(this.questions.map(() => null));
        this.observationResponse.push(this.questions.map(() => null));
      }
    },

    showModal() {
      if (
        this.observationResponse[this.buttonPosition[1]][this.buttonPosition[0]]
      )
        this.isObservationVisible = true;
      else this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
  },
  mounted() {
    for (let row = 0; row < 16; row++) {}

    this.returnQuestions();
    this.fillResponseQuestion();
    this.dates();
    this.mounted = true;
    console.log(this.questionResponse);
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

  setup: function () {
    const layout = "default-layout";

    return {
      layout,
    };
  },
};
</script>

<style src="./patrols.scss" lang="scss"></style>
