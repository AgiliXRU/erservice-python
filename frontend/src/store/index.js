import { createStore } from "vuex";

export default createStore({
  state: {
    inboundPatients: [
      {
        transportId: 1,
        name: "John Doe",
        priority: "YELLOW",
      },
    ],
  },
  mutations: {},
  actions: {},
  modules: {},
});
