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
    <l-marker :lat-lng="coordinates" ref="marker1" v-if="mostraretiqueta">
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
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'IndexPage',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  data() {
    const $q = useQuasar()
    return {
      zoom: 10,
      coordinates: [-33.5337529, -70.7247316],
      mostraretiqueta: false

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
      this.mostraretiqueta = true
      this.coordinates = [position.coords.latitude,position.coords.longitude]

    },
    upPopUp(){
      this.$refs.marker1.leafletObject.openPopup()
    },
      onError(error) {
        this.$q.notify({
          type: 'negative',
          message: 'No se puede acceder a la geolocalización, activar GPS'
        })
    }
  }
})
</script>
