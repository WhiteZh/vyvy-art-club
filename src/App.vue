<script setup>
import CoverPage from "./pages/CoverPage.vue";
import {computed, ref} from "vue";
import {pagemode} from "./glob.js";
import InfoPage from "./pages/InfoPage.vue";
import CompletionPage from "./pages/CompletionPage.vue";

let pages = {
  cover: CoverPage,
  info: InfoPage,
  completion: CompletionPage,
};
let CurrentPage = computed(() => pages[pagemode.value]);
</script>

<template>
  <div class="min-h-screen flex flex-col justify-start relative text-center max-w-[800px] mx-auto">
    <div class="mt-5">
      <h4 class="font-['Orbitron'] text-4xl text-white font-bold">A.A.</h4>
      <h1 class="text-white text-xl">Action Archive</h1>
    </div>
    <component :is="CurrentPage"/>
  </div>
</template>

<style scoped>

</style>
