<script setup>
import { RouterLink, RouterView } from 'vue-router'


AOS.init()
const BASE_URL = 'http://localhost:5000'
localStorage.setItem('BASE_URL', BASE_URL);
</script>

<template>
  <div class="everything">
    <header class="nav">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/register">Register</RouterLink>
        <RouterLink to="/contact">Contact Us</RouterLink>
      </nav>
    </header>

    <RouterView class="rg" />
  </div>
</template>

<style scoped>
.nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 15px 30px;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(10px);
  z-index: 10;
}
.rg {
  width: 100%;
}
nav {
  display: flex;
  gap: 20px;
}

a {
  color: white;
  text-decoration: none;
  opacity: 0.8;
}

a:hover {
  opacity: 1;
}
.button {
  background: #111;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  transition: all 0.3s ease;
  display: inline-block;
}

.button:hover {
  transform: scale(1.08);
  background: #222;
}

.glow {
  box-shadow: 0 0 15px rgba(255,255,255,0.3);
}

.everything {
  min-height: 100vh;
  width: 100vw;
  left: 0;
}
</style>
