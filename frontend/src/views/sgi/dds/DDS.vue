<template>
  <component :is="layout">
    <div class="sgi">

      <div class="screen-grid">
        <div class="header">
          <div class="header__left">
            <h4 class="header__title">DDS</h4>
          </div>
          <div class="header__right">
            <div class="header__right__search">
              <SearchForm :withReset="true" name="dds" @getSearchValue="getSEARCH"/>
              <Button mode="integrated" label="Search DDS" icon="search"/>
            </div>
            <Button type="button" mode="primary" label="DDS Today" @click="getDDStoday"/>
          </div>
        </div>

        <div v-if="dataReady" class="conditional-render">
          <div class="cards-grid">
            <!-- 
            CARD PUXANDO INFOS DA API
            <CustomCard  v-for="x in results" :key="x.title" :title="x.title" :id="x.id" :havePopUp="true" dateRead="2002/03/04"/> 
            -->
            <CustomCard
              v-for="x in ddsFiltered"
              :key="x.title"
              :id="x.id"
              :title="x.title"
              :textFront="x.frontText"
              :textBack="x.backText"
              :havePopUp="true"
              :frontImg="x.frontImg"
              :backImg="x.backImg"
              :dateRead="x.readDate"
            />
            <p v-if="resultSearch===false">Nenhum dado encontrado.</p>
          </div>

          <div v-if="next" class="btn-more">
            <Button
              v-if="!moreCardsLoading"
              type="button"
              mode="secondary"
              label="More cards"
              @click="getMoreCards"
            />
            <ActivityIndicator v-if="moreCardsLoading" size="small" />
          </div>


          <Box v-if="showDDStoday" :show="showDDStoday">
            <div class="custom-card -popUp">
              <div class="content-card">
                <div>
                  <div class="card-header">
                    <div class="header__left">
                      <span>#{{ ddsToday.id }}</span>
                    </div>
                    <div class="header__right">
                      <Icon
                        iconName="refresh"
                        className="a-button__icon"
                        @click="showFrontDDStoday = !showFrontDDStoday"
                      />
                      <Icon
                        iconName="close"
                        className="a-button__icon"
                        @click="showDDStoday=false"
                      />
                      <div
                        v-if="dateRead !== 'no'"
                        class="dot-status -on"
                        :data-text="'Lido em ' + ddsToday.readDate"
                      ></div>
                    </div>
                  </div>
                  <div class="card-body">
                    <div :class="['content-body__front', [{ '-face': showFrontDDStoday }]]">
                      <div class="text">
                        <h5 class="title">{{ ddsToday.title }}</h5>
                        <p>
                          {{ddsToday.frontText}}
                        </p>
                      </div>
                    </div>
                    <div :class="['content-body__back', [{ '-face': !showFrontDDStoday }]]">
                      <div class="text">
                        <h5 class="title">BACK</h5>
                        <p>
                          {{ddsToday.backText}}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </Box>

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
import { mapState } from "vuex";

import Button from "@/components/button/Button.vue";
import CustomCard from "@/components/customCard/CustomCard.vue";
import Box from "@/components/box/Box.vue";
import Icon from "@/components/icon/Icon.vue";
import ActivityIndicator from "@/components/activityIndicator/ActivityIndicator.vue";
import SearchForm from "@/components/searchForm/SearchForm.vue";


export default {
  data: function () {
    return {
      resultsAll: null,
      next: null,
      previous: null,
      count: 0,
      dataReady: false,
      moreCardsLoading: false,

      resultSearch: null,

      showDDStoday: false,
      ddsToday: '',
      showFrontDDStoday: true
    };
  },
  computed: {
    ddsFiltered: function() {
      if ( this.resultSearch===false ) {
        return []
      } else if ( this.resultSearch ) {
        return this.resultSearch
      } else {
        return this.resultsAll
      }
    },
    ...mapState({
      sideOpen: (state) => state.sideNavigationOpen,
    }),
  },
  mounted: async function () {
    await axios
      // .get(this.defaultURL + "dds/")
      .get(this.apiURL+"/dds/")
      .then((response) => {
        let data = response.data;
        this.resultsAll = data.results;
        this.next = data.next;
        this.previous = data.previous;
        this.count = data.count;

        this.dataReady = true;
      })
      .catch((err) => {
        console.log(err);
      });

    // Caso queira visualizar a saida de dados da api:
    // console.log(this.results[0]);

    this.adjustSearchFieldWidth();
  },
  methods: {
    adjustSearchFieldWidth: function () {
      let headerSGI = document.querySelector(".screen-grid .header");
      let closeTrigger = document.querySelector(
        ".header__right__search .m-search-form .a-text-field--search .a-text-field__icon-close"
      );
      let openTrigger = document.querySelector(
        ".header__right__search button.a-button--integrated"
      );

      closeTrigger.addEventListener("click", () => {
        let headerSearch = document.querySelector(
          ".screen-grid .header .header__right .header__right__search"
        );
        headerSearch.classList.remove("-open");
      });
      openTrigger.addEventListener("click", () => {
        let headerSGI = document.querySelector(".screen-grid .header");
        let headerSearch = document.querySelector(
          ".screen-grid .header .header__right .header__right__search"
        );
        let searchForm = document.querySelector(
          ".header__right__search .m-search-form"
        );

        searchForm.style.width = `${headerSGI.clientWidth - 203.7}px`;
        headerSearch.classList.add("-open");
      });

      new ResizeObserver(function () {
        let headerSGI = document.querySelector(".screen-grid .header");
        let searchForm = document.querySelector(
          ".header__right__search .m-search-form"
        );

        searchForm.style.width = `${headerSGI.clientWidth - 203.7}px`;
      }).observe(headerSGI);
    },
    getMoreCards: async function () {
      this.moreCardsLoading = true;

      await axios
        .get(this.next)
        .then((response) => {
          let data = response.data;
          this.next = data.next;
          this.resultsAll = this.resultsAll.concat(data.resultsAll);

          this.moreCardsLoading = false;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getDDStoday: async function () {
      await axios
        .get(this.apiURL + '/randomdds/')
        .then((response) => {
          let data = response.data;
          this.ddsToday = data;
          console.log(this.ddsToday);
          this.showDDStoday = true;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getSEARCH: async function(n) {
      await axios
        .get(this.apiURL + "/search/?search=" + n)
        .then((response) => {
          let data = response.data;
          let sResult = data.results;

          if ( sResult.length <= 0 ) {
            this.resultSearch = false;
          } else {
            this.resultSearch = sResult;
          }
        })
        .catch((err) => {
          console.log(err);
        });

    }
  },
  components: {
    Button,
    CustomCard,
    Box,
    ActivityIndicator,
    SearchForm,
    Icon
  },

  setup: function() {
    const layout = 'default-layout';

    return {
      layout
    };
  },
};
</script>


<style src="./dds.scss" lang="scss"></style>
