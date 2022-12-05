<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md q-gutter-sm">
      <q-btn color="primary" text-color="white" label="Recalcular posición" @click="getlocation" />
    </div>

    <l-map :zoom="zoom" style="height:86vh" :center="coordinates" ref="map">
      <l-tile-layer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      layer-type="base"
      name="OpenStreetMap"
      :max-zoom="15"
    />
    <l-marker :lat-lng="coordinates" ref="marker1">
      <l-popup>
        Usted está Aquí
      </l-popup>

    </l-marker>
    </l-map>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import "leaflet/dist/leaflet.css"
import { LMap, LTileLayer,LMarker, LPopup} from "@vue-leaflet/vue-leaflet";

export default defineComponent({
  name: 'IndexPage',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  data() {

    return {
      zoom: 10,
      coordinates: [50,50]

    }
  },
  mounted(){
    this.getlocation()
  },
  methods:{
    getlocation(){
       navigator.geolocation.getCurrentPosition(this.getposition, this.onError)

    },
    getposition(position) {
      this.$refs.marker1.leafletObject.openPopup()
      this.coordinates = [position.coords.latitude,position.coords.longitude]
    },

      onError(error) {
      console.log('code: '    + error.code    + '\n' +
              'message: ' + error.message + '\n');
    }
  }
})
</script>
