<template>
  <div>
    <h1>Inbound Patients</h1>
    <h3 v-if="loading">Loading...</h3>
    <ul v-if="inboundPatients">
      <li v-for="patient in inboundPatients" v-bind:key="patient">
        {{ patient.name }}
        <span v-if="patient.transportId === 1" style="margin: 0 10px">
          приехал в скорой помощи
        </span>
        Приоритет:
        <div
          v-if="patient.priority === 'GREEN'"
          style="width: 20px; height: 20px; background: green"
        />
        <div
          v-if="patient.priority === 'YELLOW'"
          style="width: 20px; height: 20px; background: orange"
        />
        <div
          v-if="patient.priority === 'RED'"
          style="width: 20px; height: 20px; background: red"
        />
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "InboundPatients",
  data() {
    return {
      loading: false,
      inboundPatients: [],
    };
  },
  props: {
    msg: String,
  },
  mounted: function () {
    this.loadInboundPatients();
  },
  methods: {
    loadInboundPatients: async function () {
      this.loading = true;
      this.inboundPatients = [];
      try {
        this.inboundPatients = await fetch(
          "http://localhost:8000/inboundPatients"
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-flex;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
