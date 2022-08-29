<script setup>
import { ref, onMounted } from "vue";

import "leaflet/dist/leaflet.css";
import L from "leaflet";

const center = $ref([31.593, 130.657]);

const tileLayers = {
  OpenStreetMap: {
    url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    attribution: "© OpenStreetMap",
  },
};

const tileLayerOptions = { zoom: 13, maxZoom: 19 };

function setupLeafletMap() {
  const mapDiv = L.map("map").setView(center, 13);
  L.tileLayer(tileLayers.OpenStreetMap.url, {
    maxZoom: tileLayerOptions.maxZoom,
    attribution: tileLayers.attribution,
  }).addTo(mapDiv);
}

onMounted(setupLeafletMap);
</script>

<template><div id="map">Map here</div></template>

<style scoped>
#map {
  width: 80vw;
  height: 80vh;
  margin: 2.5vh;
  border-radius: 0.75em;
}
</style>
