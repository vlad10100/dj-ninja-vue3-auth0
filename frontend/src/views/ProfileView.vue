<template>
  <div class="my-44">
    <h1 class="inline-flex w-full mx-auto justify-center text-3xl">PROFILE VIEW</h1>
    <div class="flex justify-center w-full">
        <p class="w-[900px]">
          {{code}}
        </p>
    </div>
  </div>
</template>

<script setup>
import { useAuth0 } from "@auth0/auth0-vue";
const { user } = useAuth0();
const code = user ? JSON.stringify(user.value, null, 2) : "";
</script>

<style scoped>

</style>s