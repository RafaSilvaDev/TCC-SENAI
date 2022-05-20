<template>
<component :is="layout">
  <div class="home">
  <div class="app">
    <div class="banner">
      <div class="text-banner">
        
        <h1>ETS - Escola Técnica de Engenharia</h1>
        <button type="button" class="a-button a-button--primary -without-icon" href="#history">
          <a class="a-button__label" href="#history">Leia mais...</a>
        </button>

      </div>
    </div>
    <div class="cards">
      <div v-for="x in colors" :key="x" :class="['card-content', `${x}`]">
        <div class="card-icon">
          <Icon iconName="home" />
        </div>
        <div class="card-text">
          <h6 class="card-title">Wiki ETS</h6>
          <p class="card-box">
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book.
          </p>
        </div>
      </div>
    </div>
    <div id="history" class="history">
      <div class="content-history">
        <div class="title-history">
        <h3>Sobre nós</h3>
        </div>
        <div class="text-history">
          <p>
            A ETS (Engeneering Technical School) é fruto de uma parceria Bosch e Senai onde treinamos aprendizes em diversas áreas de formação visando transformá-los na base sólida e no futuro de nossa empresa. Com mais de 60 anos de tradição e 1550 profissionais treinados, formamos aprendizes dos cursos Técnicos em Mecatrônica, Smart Automation and Software Development, Administração e Manufatura Digital. Contamos atualmente com quase 200 colaboradores que atuam nas mais diversas áreas da organização, contribuindo com o desenvolvimento de projetos de digitalização, automação, administrativos e de indústria 4.0 alinhados com as metas estratégicas de nossa corporação.
                
            Visão: Consolidar a ETS como referência em treinamentos de áreas técnicas e administrativas contribuindo assim de forma sustentável para desenvolvimento do Grupo Bosch.
                
             Missão: Treinar profissionais nas áreas técnicas e administrativas alinhados com os valores e visão Bosch, tornando-os capacitados para atuarem nas diversas áreas da organização em conjunto com o desenvolvimento de projetos que possuam a sinergia de nosso grupo e de instituições parceiras.

          </p>
        </div>
      </div>
    </div>
  </div>
</div>
</component>
</template>

<script>
import Message from 'primevue/message';
import { mapState } from 'vuex';
import Icon from "@/components/icon/Icon.vue";
import Button from "@/components/button/Button.vue";
import axios from 'axios'
import checkLogin from '../../router/RouterBlock'

export default {
  data() {
    return {
      colors: ["red", "purple", "blue", "green"],
      messages: [
			{severity: 'info', content: 'Dynamic Info Message'},
			{severity: 'success', content: 'Dynamic Success Message'},
			{severity: 'warn', content: 'Dynamic Warning Message'},
            {severity: 'error', content: 'Dynamic Error Message'}
		]
    };
  },
  computed: mapState({
    sideOpen: state => state.sideNavigationOpen,
  }),
  components: {
    Icon,
    Message,
    Button
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
