<template>
  <component :is="layout">
    <div class="sgi">
      <div class="screen-grid">

        <div class="header">
          <div class="header__left">
            <h4 class="header__title">AMA</h4>
          </div>
          <div class="header__right">
            <div class="header__right__search">
              <SearchForm 
                :withReset="true"
                name="dds"
              />
              <Button mode="integrated" label="Search AMA" icon="search"/>
            </div>
          </div>
        </div>

        <div v-if="dataReady" class="conditional-render">
          <div class="cards-grid">
            <CustomCard  v-for="x in results" :key="x.name" :title="x.name" :id="x.diameter" :havePopUp="true" dateRead="no" type="pdf"/>
          </div>
          
          <div v-if="next" class="btn-more">
            <Button v-if="!moreCardsLoading" type="button" mode="secondary" label="More cards" @click="getMoreCards"/>
            <ActivityIndicator v-if="moreCardsLoading" size="small" />
          </div>
        </div>

        <div v-else class="activity-box">
          <ActivityIndicator size="small" />
        </div>


      </div>
    </div>
  </component>
</template>


<script>
import axios from "axios";
import { mapState } from 'vuex';

import Button from '@/components/button/Button.vue';
import CustomCard from '@/components/customCard/CustomCard.vue';
import Box from '@/components/box/Box.vue';
import ActivityIndicator from '@/components/activityIndicator/ActivityIndicator.vue';

import SearchForm from '@/components/searchForm/SearchForm.vue';

export default {
  data: function() {
    return {
      results: null,
      next: null,
      previous: null,
      count: 0,
      dataReady: false,
      moreCardsLoading: false
    }
  },
  computed: {
    ...mapState({
      sideOpen: state => state.sideNavigationOpen,
    })
  },
  mounted: async function() {
    await axios
      .get('https://swapi.dev/api/planets')
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

    this.adjustSearchFieldWidth();
  },
  methods: {
    adjustSearchFieldWidth: function() {
      let headerSGI = document.querySelector('.screen-grid .header');
      let closeTrigger = document.querySelector('.header__right__search .m-search-form .a-text-field--search .a-text-field__icon-close');
      let openTrigger = document.querySelector('.header__right__search button.a-button--integrated');
      

      closeTrigger.addEventListener('click', () => {
        let headerSearch = document.querySelector('.screen-grid .header .header__right .header__right__search');
        headerSearch.classList.remove('-open');
      })
      openTrigger.addEventListener('click', () => {
        let headerSGI = document.querySelector('.screen-grid .header');
        let headerSearch = document.querySelector('.screen-grid .header .header__right .header__right__search');
        let searchForm = document.querySelector('.header__right__search .m-search-form');

        searchForm.style.width = `${headerSGI.clientWidth-64}px`;
        headerSearch.classList.add('-open');
      })

      new ResizeObserver(function(){
        let headerSGI = document.querySelector('.screen-grid .header');
        let searchForm = document.querySelector('.header__right__search .m-search-form');

        searchForm.style.width = `${headerSGI.clientWidth-64}px`;
      }).observe(headerSGI)
    
    },
    getMoreCards: async function() {
      this.moreCardsLoading = true;
      await axios
      .get(this.next)
      .then(response => {
        let data = response.data;
        this.next = data.next;
        this.results = this.results.concat(data.results);
        this.moreCardsLoading = false;
      })
      .catch((err) => {
        console.log(err);
      });
    },
  },
  components: {
    Button,
    CustomCard,
    Box,
    ActivityIndicator,
    SearchForm
  },


  setup: function() {
    const layout = 'default-layout';

    return {
      layout
    };
  }, 
};
</script>


<style src="./ama.scss" lang="scss"></style>
