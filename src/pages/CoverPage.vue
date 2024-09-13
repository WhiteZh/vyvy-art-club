<script setup>
import {ref} from "vue";
import {pagemode} from "../glob.js";

let header1 = ref();

function yesButton() {
  if (header1.value.textContent === 'Want to know a secret?') {
    pagemode.value = 'info';
  } else {
    // do nothing.
  }
}

function noButton() {
  if (header1.value.textContent === 'Want to know a secret?') {
    header1.value.textContent = 'Are you sure?'
  } else {
    pagemode.value = 'info';
  }
}
</script>

<template>
   <div class="absolute w-full top-[40vh]">
      <h2 class="-top-12 text-3xl tracking-wider text-[#f8a72f] leading-none" ref="header1">Want to know a secret?</h2>
      <div class="flex flex-col justify-between items-center gap-y-6 text-white mt-4">
        <button class="text-3xl rounded-xl bg-[#ffb800] h-12 font-['Orbitron'] w-32 font-bold" @click="yesButton">YES</button>
        <button class="text-4xl rounded-xl bg-[#ffb800] h-12 font-['Orbitron'] w-32 font-bold" @click="noButton">NO</button>
      </div>
   </div>
</template>

<style scoped>

</style>