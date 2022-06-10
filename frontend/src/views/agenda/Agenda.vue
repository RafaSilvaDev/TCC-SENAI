<template>
  <component :is="layout">
    <div class="agenda">
      <div class="calendar-container">
        <div class="header">
          <div class="calendar-dateinput">
            <input type="date" v-model="currentDate" />
          </div>

          <div class="day">
            <h5 class="date">{{ dateTitle }} <span>{{ dayName }}</span></h5>
            <!-- <span class="name-day">{{dayName}}</span> -->
          </div>

          <div class="buttons-adv">
            <Button
              type="button"
              icon="arrow-left"
              mode="secondary"
              @click="setCurrentDate(-1)"
            />
            <Button
              type="button"
              icon="arrow-right"
              mode="secondary"
              @click="setCurrentDate(1)"
            />
          </div>
          <!-- <i class="a-icon a-button__icon boschicon-bosch-ic-calendar"></i> -->
        </div>

        <ul class="classes">
          <div class="classes-content">
            <li class="item">
              <div class="deixa-essa-div-aqui"></div>
              <ul class="hours">
                <li class="h-time" v-for="idx in 10" :key="idx">
                  {{ idx + 7 }}h
                </li>
              </ul>
            </li>

            <li class="item" v-for="cl in classes" :key="cl.name">
              <div class="classeName">{{ cl.name }}</div>

              <div class="main">
                <div
                  class="event-card"
                  v-for="event in eventsFiltered.filter(
                    (el) => el.fk_team === cl.id
                  )"
                  :style="`grid-column-start: ${setColumnGrid(
                    event.startTime
                  )}; grid-column-end: ${setColumnGrid(
                    event.endTime
                  )};background-color: ${generateColor()};`"
                  :key="event.name"
                >
                  <div :class="{'event-card-header': true, 'display-block-event': isDisplayBlock(event.startTime.substring(0, 5), event.endTime.substring(0, 5))}">
                    <p>{{event.name}}</p>
                    <div class="time-event">
                      {{ event.startTime.substring(0, 5) }}
                      -
                      {{ event.endTime.substring(0, 5) }}
                    </div>
                  </div>

                  <div class="event-card-body">
                    <span :class="{'display-block-event': isDisplayBlock(event.startTime.substring(0, 5), event.endTime.substring(0, 5))}">
                     <p>Responsável:</p> <p>{{ event.event_responsible }}</p>
                    </span>
                    <span>
                      <p>Local:</p> <p>{{ event.location.localName }}</p>
                    </span>
                  </div>
                </div>
              </div>
            </li>
          </div>
        </ul>
      </div>
    </div>
  </component>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Button from "@/components/button/Button.vue";

export default {
  n: "Agenda",
  data: function () {
    return {
      addDay: 0,
      currentDate: "",
      businessStartHours: 8,
      timeslotInterval: 15,
      classes: [],
      events: [],
    };
  },
  mounted: async function () {
    this.setCurrentDate();

    const getTeams = axios.get(this.apiURL + "/teams/");
    const getEvents = axios.get(this.apiURL + "/events/");

    await axios
      .all([getTeams, getEvents])
      .then(
        axios.spread((respTeam, respEvents) => {
          const teamData = respTeam.data;
          this.classes = teamData.results;

          const eventsData = respEvents.data;
          this.events = eventsData.results;
          
        })
      )
      .catch((errors) => {
        errors.forEach((err) => {
          console.log(err);
        });
      });
  },
  methods: {
    setColumnGrid: function (time) {
      const h = parseInt(time.split(":")[0]);
      const m = parseInt(time.split(":")[1]);

      const totalMinutes = Math.abs(this.businessStartHours - h) * 60 + m;
      const rowPos = totalMinutes / this.timeslotInterval + 1;

      return rowPos;
    },
    setRowGrid: function (id) {
      const matchID = this.classes.findIndex((el) => el.id == id);
      if (matchID == -1) {
        return "none";
      }
      return matchID + 1;
    },
    setCurrentDate: function (v) {
      let date = new Date();

      if (v) {
        date = new Date(this.currentDate);
      } else {
        v = 0
      }

      

      date.setDate(date.getDate() + v);

      const str = date.toISOString().split("T")[0];

      this.currentDate = str;

    },
    randomNumber: function(min, max) {
      return Math.floor(Math.random() * (max - min) + min);
    },
    generateColor: function () {
      let r = this.randomNumber(50, 255)
      let g = this.randomNumber(70, 255)
      let b = this.randomNumber(70, 255)

      let color = `rgba(${r}, ${g}, ${b}, 0.7)`

      return color;
    },
    isDisplayBlock: function(start='00', end='01') {
      const startTime = parseInt(start.substring(0, 3))
      const endTime = parseInt(end.substring(0, 3))
      return (endTime-startTime > 0) && (endTime-startTime <= 2)
    }
  },
  computed: {
    gridRows: function () {
      return {
        gridTemplateRows: `repeat(${this.classes.length}, 1fr)`,
      };
    },
    eventsFiltered: function () {
      return this.events.filter((el) => el.date == this.currentDate);
    },
    dateTitle: function () {
      const date = this.currentDate.split("-").reverse();
      date.pop();
      return date.join("/");
    },
    dayName: function () {
      const date = new Date(this.currentDate);
      date.setDate(date.getDate()+1);
      const dayName = date.toLocaleString("en-US", { weekday: "long" });
      return dayName;
    },

  },
  components: {
    Button,
  },

  setup: function () {
    const layout = "default-layout";

    return {
      layout,
    };
  },
};
</script>

<style src="./agenda.scss" lang="scss"></style>