<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import footer1 from './components/footer.vue'
import main from './components/main.vue'
import comments from './components/comments.vue'
import all_articles from './components/all_articles.vue'
import header1 from './components/header.vue'

</script>

<template>
	<header1>
	<footer1 name="Xiaogaun" timefirst="2021" timeafter="2022"/>
</template> 

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
