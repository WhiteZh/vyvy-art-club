<script setup>

import {pagemode} from "../glob.js";

const utilf = (x) => typeof x !== "string" ? '-' : x === '' ? '-' : x;

async function submit() {
  let res = await fetch("/api/submit", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: document.getElementById('name').value,
      grade: document.getElementById('grade').value,
      school: document.getElementById('school').value,
      email: document.getElementById('email').value,
      ig_handle: document.getElementById('ig-handle').value,
      referee: utilf(document.getElementById('referee').value),
      description: utilf(document.getElementById('description').value),
    }),
  });

  if (res.ok) {
    pagemode.value = 'completion';
  } else {
    window.alert(`${res.status}: ${res.statusText}`);
    console.log(res);
  }
}
</script>

<template>
  <form class="mt-14 flex-grow flex flex-col items-stretch justify-start text-left px-4" action="/api/submit" method="post">
    <label for="name" class="text-2xl">First, Last Name</label>
    <input type=text id="name" name="name" placeholder="John Doe"/>

    <label for="grade" class="text-2xl">Grade</label>
    <select id="grade" name="grade">
      <option>9</option>
      <option>10</option>
      <option>11</option>
      <option>12</option>
    </select>

    <label for="school" class="text-2xl">School</label>
    <input type="text" id="school" name="school" placeholder="Example High School" value="Fountain Valley High School"/>

    <label for="email" class="text-2xl">Email</label>
    <input type="email" id="email" name="email" placeholder="someone@example.com"/>

    <label for="ig-handle" class="text-2xl">IG Handle</label>
    <input type="text" id="ig-handle" name="ig-handle" placeholder="@john_doe"/>

    <label for="referee" class="text-2xl">Who referred you?</label>
    <input type="text" id="referee" name="referee" placeholder="Referrals get 4 Action points!"/>

    <label for="description" class="text-md mt-2">Write a short description on what you are passionate about</label>
    <textarea id="description" name="description" class="rounded-md flex-grow max-h-56 text-black text-lg px-1.5" placeholder="(Optional)"/>

    <button type="submit" class="text-2xl rounded-xl bg-[#ffb800] h-12 font-['Orbitron'] w-32 font-bold mt-5 mx-auto" @click.prevent="submit">Submit</button>
  </form>
</template>

<style scoped>
form>input, form>select {
  @apply text-lg text-black rounded-md h-8 px-1.5;
}
</style>