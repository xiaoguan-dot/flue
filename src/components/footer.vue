<!-- 页脚 -->
<script setup>
import { ref } from 'vue'

defineProps({
  name: String,
  timefirst: String,
  timeafter: String,
  after: String
})
</script>
<template>
	<footer>
		&copy; {{ timefirst }} - {{ timeafter }} {{ name }}  Powered by Flue
		{{ after }}
		</footer>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
