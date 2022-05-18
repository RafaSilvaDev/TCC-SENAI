<template>
<component :is="layout">
  <div :class="[ 'home', {'-side-open': sideOpen} ]">
  <div class="app">
    <div class="banner">
      <div class="text-banner">
        <p>ETS - Escola Técnica de Engenharia</p>
        <p><a href="#history" id="button-about">Leia mais</a></p>
      </div>
    </div>
    <div class="cards">
      <div v-for="x in colors" :key="x" :class="['card-content', `${x}`]">
        <div class="card-icon">
          <Icon iconName="home" />
        </div>
        <div class="card-text">
          <p class="card-title">Wiki ETS</p>
          <p class="card-box">
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book.
          </p>
        </div>
      </div>
      <br />
    </div>
    <div id="history" class="history">
      <div class="content-history">
        <div class="title-history">
        <h1>Sobre nós</h1>
        </div>
        <div class="text-history">
          <p>
            A ETS (Engeneering Technical School) é fruto de uma parceria Bosch e Senai onde treinamos aprendizes em diversas áreas de formação visando transformá-los na base sólida e no futuro de nossa empresa. Com mais de 60 anos de tradição e 1550 profissionais treinados, formamos aprendizes dos cursos Técnicos em Mecatrônica, Smart Automation and Software Development, Administração e Manufatura Digital. Contamos atualmente com quase 200 colaboradores que atuam nas mais diversas áreas da organização, contribuindo com o desenvolvimento de projetos de digitalização, automação, administrativos e de indústria 4.0 alinhados com as metas estratégicas de nossa corporação.
                
            Visão: Consolidar a ETS como referência em treinamentos de áreas técnicas e administrativas contribuindo assim de forma sustentável para desenvolvimento do Grupo Bosch.
                
             Missão: Treinar profissionais nas áreas técnicas e administrativas alinhados com os valores e visão Bosch, tornando-os capacitados para atuarem nas diversas áreas da organização em conjunto com o desenvolvimento de projetos que possuam a sinergia de nosso grupo e de instituições parceiras.

          </p>
        </div>
      </div>-
    </div>
  </div>
</div>
</component>
</template>

<script>
import { mapState } from 'vuex';
import Icon from "@/components/icon/Icon.vue";
import axios from 'axios'
import checkLogin from '../../router/RouterBlock'
export default {
  data() {
    return {
      colors: ["red", "purple", "blue", "green"],
    };
  },
  computed: mapState({
    sideOpen: state => state.sideNavigationOpen,
  }),
  components: {
    Icon,
  },
  methods:{
    
  },
  created(){
    // checkLogin()
  },
  setup: function() {
    let layout = 'default-layout'

    return {
      layout
    }
  }
  
};
</script>

<style src="./home.scss" lang="scss"></style>
