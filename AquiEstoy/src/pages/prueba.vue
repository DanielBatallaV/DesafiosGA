<template>
  <q-page class="flex flex-center">
    <l-map :zoom="zoom" style="height:50vh">
      <l-tile-layer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      layer-type="base"
      name="OpenStreetMap"
      :max-zoom="10"
    />
    <l-marker :lat-lng="coordinates"></l-marker>
    </l-map>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import "leaflet/dist/leaflet.css"
import { LMap, LTileLayer,LMarker, LIcon  } from "@vue-leaflet/vue-leaflet";

export default defineComponent({
  name: 'IndexPage',
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {

    return {
      zoom: 2,
      coordinates: [-33.5575278,-70.5987366]

    }
  },
  mounted(){

    console.log(navigator.geolocation.getCurrentPosition(this.getlat, this.onError))

  },
  methods:{
      getlat(position) {
      this.coordinates = [50,50]
    },
      getlon(position) {
      return position.coords.longitude
    },
      onError(error) {
      console.log('code: '    + error.code    + '\n' +
              'message: ' + error.message + '\n');
    }
  }
})
</script>
