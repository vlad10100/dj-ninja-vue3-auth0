<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuth0 } from "@auth0/auth0-vue";

const { isAuthenticated } = useAuth0();

import LoginBtn from "@/components/buttons/LoginBtn.vue"
import LogoutBtn from "@/components/buttons/LogoutBtn.vue"

</script>

<template>
  <div>
    <header>
      <nav class="flex justify-between px-20 py-10 bg-purple-100">
        <div>
          <RouterLink to="/" class="text-3xl cursor-pointer">BRAND</RouterLink>
        </div>
        <div class="flex text-xl gap-10">
          <RouterLink to="/" class="cursor-pointer">Home</RouterLink>
          <RouterLink to="/public" class="cursor-pointer">Public</RouterLink>
          <RouterLink to="/protected" class="cursor-pointer">Protected</RouterLink>
          <RouterLink to="/profile" class="cursor-pointer" v-if="isAuthenticated">Profile</RouterLink>
          <RouterLink to="/admin" class="cursor-pointer" v-if="isAuthenticated">Admin</RouterLink>
          <LoginBtn v-if="!isAuthenticated"></LoginBtn>
          <LogoutBtn v-if="isAuthenticated"></LogoutBtn>
        </div>
      </nav>
    </header>
    <RouterView />
  </div>

</template>

