import { createStore } from 'vuex'

export default createStore({
  state: {
    sideNavigationOpen: false,
    darkMode: false,
  },
  mutations: {
    changeStateSideNavigation: (state) => {
      state.sideNavigationOpen = !state.sideNavigationOpen;
    },
    changeStateThemeMode: (state) => {
      state.darkMode = !state.darkMode;
    }
  },
  actions: {
   
  },
  modules: {
  },
})
