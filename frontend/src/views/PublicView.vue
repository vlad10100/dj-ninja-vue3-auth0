<template>
  <div class="my-44">
    <h1 class="inline-flex w-full mx-auto justify-center text-3xl">PUBLIC VIEW</h1>
    <div>
      <code class="inline-flex w-full mx-auto justify-center">
        {{ message }}
      </code>
    </div>
  </div>
</template>

<script setup>
import { getPublicResource } from "@/services/ApiEndpointService";
import { ref } from "vue";
import { useAuth0 } from "@auth0/auth0-vue";

const message = ref("");
const getMessage = async () => {
  const { getAccessTokenSilently } = useAuth0();
  const accessToken = await getAccessTokenSilently();
  const { data, error } = await getPublicResource(accessToken);

  if (data) {
    message.value = JSON.stringify(data, null, 2);
  }

  if (error) {
    message.value = JSON.stringify(error, null, 2);
  }
};

getMessage();
</script>

<style scoped>

</style>