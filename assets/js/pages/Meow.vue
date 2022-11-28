<script setup>
import { ref } from "vue";
const meow = ref("meow");
const props = defineProps({
    purr: String,
});
</script>


<template>
    <input type="text" v-model="meow" />
    <p>{{ meow }}</p>
    <p>{{ purr }}</p>
</template>


<style scoped>
</style>