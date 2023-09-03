<template>
  <div>
    <button @click="login">Login</button>
  </div>
</template>

<script setup>
import { useAuth0 } from "@auth0/auth0-vue";

const { loginWithRedirect } = useAuth0();

const login = () => {
  loginWithRedirect(
    {
      appState: {
        target: "/",
      },
      authorizationParams: {
        prompt: "login",
      }
    }
  )
}
</script>

<style scoped>

</style>