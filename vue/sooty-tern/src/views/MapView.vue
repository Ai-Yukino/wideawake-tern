<!-- <script setup>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
</script> -->

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default {
  name: "Map",
  data() {
    return {
      center: [31.593, 130.657],
    };
  },
  methods: {
    setupLeafletMap: function () {
      const mapDiv = L.map("map").setView(this.center, 13);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "© OpenStreetMap",
      }).addTo(mapDiv);
    },
  },
  mounted() {
    this.setupLeafletMap();
  },
};
</script>

<template><div id="map">Map here</div></template>

<style scoped>
#map {
  width: 80vw;
  height: 80vh;
  margin: 2.5vh;
}
</style>
