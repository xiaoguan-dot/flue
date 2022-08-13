<!-- 页眉 -->
<script setup>
import { ref } from 'vue'


</script>
<template>
	<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js">
		logo=$("#logo");
		$.get("127.0.0.1:9113/logo",function(res){
			logo.src=res;
			// logo.src
		});
	</script>
	<img src="" alt="" id="logo" class="font">
</template>

<style scoped>
a {
  color: #42b983;
}
.font{
	position: absolute;
	font-family: MicrosoftYaHei-Bold;
	font-size: 100px;
	font-weight: bold;
	line-height: 100px;
	letter-spacing: 0em;
	color: rgba(0, 0, 0, 0.8);
}

</style>
