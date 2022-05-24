<template>
  <component :is="layout">
    <div class="agenda">

      <div class="calendar-container">

        <div class="header">
          
          <div class="calendar-dateinput">
            <input type="date" v-model="currentDate">
          </div>

          <div class="day">
            <h5 class="date">{{dateTitle}} {{dayName}}</h5>
            <!-- <span class="name-day">{{dayName}}</span> -->
          </div>

          <div class="buttons-adv">
            <Button type="button" icon="arrow-left" mode="secondary" @click="setCurrentDate(-1)"/>
            <Button type="button" icon="arrow-right" mode="secondary" @click="setCurrentDate(1)"/>
          </div>
          <!-- <i class="a-icon a-button__icon boschicon-bosch-ic-calendar"></i> -->
          
        </div>

        <ul class="classes">
          
          <li class="item">
            <div></div>
            <ul class="hours"><li class="h-time" v-for="idx in 10" :key="idx">{{idx+7}}h</li></ul>
          </li>
          
          <li class="item" v-for="cl in classes" :key="cl.name">
            <div class="classeName">{{cl.name}}</div>

            <div class="main">
              <div class="event-card" v-for="event in eventsFiltered.filter(el => el.fk_team===cl.id)" 
                  :style="`grid-column-start: ${setColumnGrid(event.startTime)}; grid-column-end: ${setColumnGrid(event.endTime)};background-color: ${generateColor()};`"
                  :key="event.name" 
              >
                <div class="event-card-header">
                  {{event.name}}
                  <div class="time-event">
                    {{event.startTime.substring(0, 5)}}
                    -
                    {{event.endTime.substring(0, 5)}}
                  </div>
                </div>

                <div class="event-card-body">
                  <p>Responsável: <span>{{event.event_responsible}}</span></p>
                  <p>Local: <span>{{event.location.localName}}</span></p>
                  
                </div>
              </div>
              
            </div>

          </li>
        </ul>

        

      </div>

    </div>
  </component>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Button from '@/components/button/Button.vue';

export default {
  n: 'Agenda',
  data :function() {
    return {
      addDay: 0,
      currentDate: '',
      businessStartHours: 8,
      timeslotInterval: 15,
      classes: [],
      events: []
    }
  },
  mounted: async function() {
    this.setCurrentDate();

    const getTeams = axios.get(this.apiURL+'/teams/')
    const getEvents = axios.get(this.apiURL+'/events/')

    await axios.all([getTeams, getEvents])
      .then(axios.spread((respTeam, respEvents) => {

        const teamData = respTeam.data
        this.classes = teamData.results

        const eventsData = respEvents.data
        this.events = eventsData.results
        console.log(eventsData)
      }))
      .catch(errors => {
        errors.forEach(err => {
          console.log(err)
        });
      })
    
  },
  methods: {
    setColumnGrid: function(time) {
      const h = parseInt(time.split(':')[0])
      const m = parseInt(time.split(':')[1])

      const totalMinutes = Math.abs(this.businessStartHours - h) * 60 + m;
      const rowPos = totalMinutes / this.timeslotInterval + 1;

      return rowPos;
    },
    setRowGrid: function(id) {
     const matchID = this.classes.findIndex((el) => el.id == id)
     if (matchID == -1) {
       return 'none'
     }
     return matchID+1
    },
    setCurrentDate: function(v) {
      if (v) {
        this.addDay += v
      }
      
      const date = new Date();

      date.setDate(date.getDate() + this.addDay);

      const str = date.toISOString().split('T')[0];

      this.currentDate = str
    },
    generateColor: function() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      
      return color;      
    }
  },
  computed: {
    gridRows: function() {
      return {
        gridTemplateRows: `repeat(${this.classes.length}, 1fr)`
      }
    },
    eventsFiltered: function() {
      return this.events.filter( el => el.date==this.currentDate )
    },
    dateTitle: function() {
      const date = this.currentDate.split('-').reverse()
      date.pop()
      return date.join('/')
      
    },
    dayName: function() {
      const date = new Date(this.currentDate)
      const dayName = date.toLocaleString('en-US', { weekday: 'long' });
      return dayName
    }
  },
  components: {
    Button,
  },

  setup: function() {
    const layout = 'default-layout';

    return {
      layout
    };
  },   
}
</script>

<style src="./agenda.scss" lang="scss"></style>