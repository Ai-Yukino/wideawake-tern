<script setup>
// 📦 Vue imports
import { ref, onMounted } from "vue";

// 📦 Leaflet imports
import "leaflet/dist/leaflet.css";
import L from "leaflet";

// ❄ Refs
const center = $ref([31.593, 130.657]);

// 🌸 Non-ref variables
const tileLayers = {
  OpenStreetMap: {
    url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    attribution: "© OpenStreetMap",
  },
};

const tileLayerOptions = { zoom: 13, maxZoom: 19 };

const aira = { main: [31.593, 130.657] };

// ❄ Methods
function setupLeafletMap() {
  const mapDiv = L.map("map").setView(center, 13);

  L.tileLayer(tileLayers.OpenStreetMap.url, {
    maxZoom: tileLayerOptions.maxZoom,
    attribution: tileLayers.attribution,
  }).addTo(mapDiv);

  L.marker([31.593, 130.657]).addTo(mapDiv);
}

// 🌸 Lifecycle hooks
onMounted(setupLeafletMap);
</script>

<template><div id="map">Map here</div></template>

<style scoped>
#map {
  width: 80vw;
  height: 80vh;
  margin: 5vh;
  border-radius: 0.75em;
}
</style>
