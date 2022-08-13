<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
  img: String
})
</script>

<template>
	<img src="{{ img }}" alt="">
	<h1>{{ msg }}</h1>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
