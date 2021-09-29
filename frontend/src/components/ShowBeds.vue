<template>
  <h1>Show beds</h1>
  <div class="container">
    <div v-for="(bed, index) in beds" :key="index">
      <div v-if="!bed.criticalCare" class="bed-item">
        #{{ bed.bedId }}
        <button v-if="bed.patientAssigned === null" @click="assignToBed(bed.criticalCare, bed.bedId)">Assign</button>
        <div v-if="bed.patientAssigned !== null">
          {{  bed.patientAssigned.name }}
        </div>
      </div>
      <div v-if="bed.criticalCare" class="bed-item-critical">
        #{{ bed.bedId }}
        <button v-if="bed.patientAssigned === null" @click="assignToBed(bed.criticalCare, bed.bedId)">Assign</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Show Beds",
  data() {
    return {
      loading: false,
      beds: [],
      inboundPatients: []
    };
  },
  mounted: function () {
    this.loadBeds();
  },
  methods: {
    assignToBed: async function (isCritical, bed_id) {
      try {
        this.inboundPatients = await fetch(
            "/api/inboundPatients"
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }

      if (this.inboundPatients[0].priority === 'YELLOW' && !isCritical) {
        await fetch(
            "/api/assignPatientToBed?transportId=" + this.inboundPatients[0].transportId + "&bedId=" + bed_id,
            {method: "POST"}
        ).then((response) =>  {
          console.log(response.text() );
          this.loadBeds();
        });
      } else {
        alert('not ok!');
      }

    },
    loadBeds: async function () {
      this.loading = true;
      this.beds = [];
      try {
        this.beds = await fetch(
            "/api/beds"
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
  }
}
</script>

<style>
.container {
  width: 1240px;
  text-align: center;
  position: absolute;
}

.bed-item {
  background-color: orange;
  width: 200px;
  min-height: 60px;
  margin: 2px;
}

.bed-item-critical {
  width: 200px;
  min-height: 60px;
  margin: 2px;
  background-color: rosybrown;
}
</style>