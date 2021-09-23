<template>
  <div class="home">
    <InboundPatients />
  </div>
</template>

<script>
// @ is an alias to /src
import InboundPatients from "@/components/InboundPatients.vue";

export default {
  name: "Home",
  components: {
    InboundPatients,
  },
};
</script>
