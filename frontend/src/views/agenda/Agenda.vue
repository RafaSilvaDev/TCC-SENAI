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
              <div class="event-card" v-for="event in eventsFiltered.filter(el => el.class===cl.id)" 
                  :style="`grid-column-start: ${setColumnGrid(event.start)}; grid-column-end: ${setColumnGrid(event.end)};`"
                  :key="event.name" 
              >
                {{event.title}}
              </div>
              
            </div>

          </li>
        </ul>

        

      </div>

    </div>
  </component>
</template>

<script>
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
      timeslotInterval: 10,
      classes: [
        {id: 1, name: '1º Smart Automation'},
        {id: 2, name: '2º Smart Automation'},
        {id: 6, name: '5º Mecatrônica'},
        {id: 4, name: '7º Mecatrônica'},
      ],
      events: [
        {
          id: 1,
          title: 'Aula 1',
          class: 1,
          assignee: 'Cléber',
          date: '2022-05-02',
          start: '11:00',
          end: '12:00'
        },
        {
          id: 4,
          title: 'Aula 5',
          class: 4,
          assignee: 'Cléber',
          date: '2022-05-01',
          start: '13:00',
          end: '15:10'
        },
        {
          id: 2,
          title: 'Aula 2',
          class: 6,
          assignee: 'Cléber',
          date: '2022-05-01',
          start: '8:00',
          end: '12:00'
        },
        {
          id: 10,
          title: 'Aula 3',
          class: 6,
          assignee: 'Cléber',
          date: '2022-05-05',
          start: '8:00',
          end: '9:00'
        },
      ]
    }
  },
  mounted: async function() {
    this.setCurrentDate();

    await axios
      .get(this.apiURL+'/filter/ssm/?search=ama')
      .then(response => {
        let data = response.data;
        this.results = data.results;
        this.next = data.next;
        this.previous = data.previous;
        this.count = data.count;

        this.dataReady = true;
        
      })
      .catch((err) => {
        console.log(err);
      });
    
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