<template>
  <Header></Header>

  <div class="content">

    <div class = 'place'>
      <input v-model="place" placeholder="Место" />
      <button @click="getWeather" class="search-button">Узнать погоду</button>
    </div>

    <div class="weather" v-if="isElVisiblePlace">
      <div class="title"> Погода {{ name_of_place }}</div>
      <div> <span>Температура:</span> {{ weather_place.temp }}°</div>
      <div> <span>Ощущается как:</span> {{ weather_place.feels_like }}°</div>
      <div> <span>Влажность воздуха:</span> {{ weather_place.humidity }}%</div>
      <div> <span>Ветер:</span> {{ weather_place.wind_dir }}</div>
      <div> <span>Скорость ветра:</span> {{ weather_place.wind_speed }} м/с</div>
    </div>

    <div class = 'place'>
      <input v-model="long" placeholder="Долгота" />
      <input v-model="lat" placeholder="Широта" />
      <button @click="getWeatherCoors">Узнать погоду</button>
    </div>

    <div class="weather" v-if="isElVisibleCoors">
      <div class="title"> Погода {{ long_of_place }} {{ lat_of_place }}</div>
      <div> <span>Температура:</span> {{ weather_coors.temp }}°</div>
      <div> <span>Ощущается как:</span> {{ weather_coors.feels_like }}°</div>
      <div> <span>Влажность воздуха:</span> {{ weather_coors.humidity }}%</div>
      <div> <span>Ветер:</span> {{ weather_coors.wind_dir }}</div>
      <div> <span>Скорость ветра:</span> {{ weather_coors.wind_speed }} м/с</div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import Header from './components/Header.vue'


export default {

  components:{
    Header
  },

  methods: {

    getWeather(){

      this.name_of_place = this.place

      axios.post('http://127.0.0.1:5000/weather/api/v1.0/place',
      {
        name: this.place
      }
      )
      .then(response => this.weather_place = response.data)

      this.isElVisiblePlace = true
    },

    getWeatherCoors(){

      this.long_of_place = this.long
      this.lat_of_place = this.lat

      axios.post('http://127.0.0.1:5000/weather/api/v1.0/long_lat',
      {
        long: this.long,
        lat: this.lat
      }
      )
      .then(response => this.weather_coors = response.data)

      this.isElVisibleCoors = true
    }

  },

  data(){
    return{
      long_of_place: '',
      lat_of_place: '',
      name_of_place: '',
      weather_place: [],
      weather_coors: [],
      isElVisiblePlace: false,
      isElVisibleCoors: false
    }
  },

  // mounted(){
  //   axios.get('http://127.0.0.1:5000/weather/api/v1.0/Murmansk')
  //     .then(response => this.weather = response.data)
  // }
}
</script>

<style>
  .place{
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    border: 2px solid #0d79de;
    border-radius: 10px;
    padding-right: 10px;
    padding-left: 10px;
    padding-top: 20px;
    padding-bottom: 20px;
    text-align: center;
    margin-right: 35%;
    margin-left: 35%;
  }

  .place input{
    border: none;
    border-bottom: 2px solid #0d79de;
    margin-bottom: 10px;
  }

  .place input:focus{
    outline: none !important;
    border-bottom: 2px solid orangered;
  }

  .place button{
    border-radius: 3px;
    border: 2px solid #0d79de;
    background-color: #0d79de;
    color: white;
    padding-top: 5px;
    padding-bottom: 5px;
  }

  .place button:hover{
    background-color: orangered;
    border: 2px solid orangered;
  }

  .content{
    padding: 2% 10% 2% 10%;
  }
  .weather{
    padding: 0% 10% 2% 36%;
  }

  .weather div{
    padding-top: 3px;
    padding-bottom: 3px;
  }

  .weather span{
    font-weight: 600;
  }

  .title{
    font-size: 20px;
    font-weight: bold;
    color: #0d79de;
    margin-bottom: 10px;
  }
</style>