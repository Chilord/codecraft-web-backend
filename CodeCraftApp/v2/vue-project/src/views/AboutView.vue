<script setup>
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const code = ref('')
const error = ref('')
const loading = ref(false)

async function register() {
  error.value = ''
  loading.value = true

  try {
    const res = await fetch(`${localStorage.getItem('BASE_URL')}/api/register`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
        code: code.value
      })
    })

    const data = await res.json()

    if (!res.ok) throw new Error(data.message || 'Failed')

    window.location.href = '/login'
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

      <h2>Create Account</h2>

      <p class="sub">
        Enter your access code to join CodeCraft
      </p>

      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <input v-model="code" placeholder="Access Code" />

      <button @click="register" :disabled="loading">
        {{ loading ? "Creating..." : "Register" }}
      </button>

      <p class="error" v-if="error">{{ error }}</p>

      <RouterLink to="/login" class="link">
        Already have an account? Login
      </RouterLink>

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
  text-align: center;
  box-shadow: 0 0 30px rgba(0,0,0,0.5);
}

h2 {
  margin-bottom: 10px;
}

.sub {
  opacity: 0.7;
  margin-bottom: 20px;
}

input {
  width: 100%;
  padding: 10px;
  margin: 8px 0;
  border: none;
  border-radius: 6px;
  background: #111;
  color: white;
}

button {
  width: 100%;
  padding: 12px;
  margin-top: 15px;
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

.link {
  display: block;
  margin-top: 15px;
  opacity: 0.7;
}
</style>