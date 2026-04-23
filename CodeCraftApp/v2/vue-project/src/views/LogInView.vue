<script setup>
import { ref } from 'vue'
import { User, Lock } from 'lucide-vue-next'

const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

async function login() {
  error.value = ''
  loading.value = true

  try {
    const res = await fetch(`${localStorage.getItem('BASE_URL')}/api/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include', // IMPORTANT for sessions
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    })

    const data = await res.json()
    if (!res.ok) throw new Error(data.message)

    window.location.href = '/dashboard'
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <section class="auth">
    <div class="card" data-aos="fade-up">

      <h2>Welcome Back</h2>

      <div class="input">
        <User class="icon" />
        <input v-model="username" placeholder="Username" />
      </div>

      <div class="input">
        <Lock class="icon" />
        <input v-model="password" type="password" placeholder="Password" />
      </div>

      <button @click="login" :disabled="loading">
        {{ loading ? "Logging in..." : "Login" }}
      </button>

      <p class="error" v-if="error">{{ error }}</p>

    </div>
  </section>
</template>

<style scoped>
.auth {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0f0f0f, #1a1a2e);
}

.card {
  background: rgba(20,20,30,0.9);
  padding: 40px;
  border-radius: 12px;
  width: 320px;
  box-shadow: 0 0 40px rgba(0,0,0,0.6);
  text-align: center;
}

h2 {
  margin-bottom: 20px;
}

.input {
  display: flex;
  align-items: center;
  background: #111;
  border-radius: 6px;
  margin: 10px 0;
  padding: 8px;
}

.input input {
  background: transparent;
  border: none;
  color: white;
  flex: 1;
  outline: none;
}

.icon {
  width: 18px;
  margin-right: 8px;
  opacity: 0.6;
}

button {
  width: 100%;
  margin-top: 15px;
  padding: 12px;
  background: #111;
  color: white;
  border: none;
  border-radius: 6px;
  transition: 0.3s;
}

button:hover {
  background: #222;
  transform: scale(1.03);
}

.error {
  color: #ff6b6b;
  margin-top: 10px;
}
</style>