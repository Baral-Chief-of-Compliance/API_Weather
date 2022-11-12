<template>
  <div> {{ weather }}</div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return{
      weather: []
    }
  },
  mounted(){
    axios.get('http://127.0.0.1:5000/weather/api/v1.0/Murmansk')
      .then(response => this.weather = response.data)
  }
}
</script>