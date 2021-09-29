import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../components/HomePage.vue";
import InboundPatients from "../components/InboundPatients";
import ShowBeds from "../components/ShowBeds"

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/inbound",
    name: "Inbound Patients",
    component: InboundPatients,
  },
  {
    path: "/beds",
    name: "ShowBeds",
    component: ShowBeds,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
