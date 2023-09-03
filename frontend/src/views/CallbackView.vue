<template>
  <div class="flex justify-center my-44">
    <h1 class="text-3xl">CALLBACK</h1>
    <p>{{error}}</p>
  </div>
</template>

<script setup>
import { useAuth0 } from "@auth0/auth0-vue"
const { error } = useAuth0();
</script>

<style scoped>

</style>