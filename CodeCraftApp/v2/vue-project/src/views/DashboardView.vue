<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { PlayCircle, LogOut } from 'lucide-vue-next'

const user = ref('')
const error = ref('')
const source = ref('')
const isVideoPlaying = ref(false);


async function handleEscape(e) {
  if (e.key == 'Escape' && isVideoPlaying.value === true) {
        isVideoPlaying.value = false;
  }
}
onMounted( async () => {
  window.addEventListener('keydown', handleEscape)
})

onUnmounted(async () => {
  window.removeEventListener('keydown', handleEscape);
})

async function loadUser() {
  try {
    const res = await fetch(`${localStorage.getItem('BASE_URL')}/api/me`, {
      credentials: 'include'
    })

    if (!res.ok) throw new Error()

    const data = await res.json()
    user.value = data.username
  } catch {
    window.location.href = '/login'
  }
}

async function logout() {
  await fetch(`${localStorage.getItem('BASE_URL')}/api/logout`, {
    method: 'POST',
    credentials: 'include'
  })

  window.location.href = '/'

}

async function play(week) {
  isVideoPlaying.value = true;
  watch(week);
}
async function watch(week) {
const response = await fetch(`${localStorage.getItem('BASE_URL')}/api/watch/${week}`, {
  method: 'POST',
  credentials: 'include',  
});
const result = await response.json();
source.value = result['video_embed'];
return result['video_embed']
}
onMounted(loadUser) 
</script>

<template>
  <section class="dashboard">
    <div class="container" v-if="!isVideoPlaying">

      <div class="top">
        <h2>Welcome, {{ user }}</h2>

        <button class="logout" @click="logout">
          <LogOut class="icon" />
        </button>
      </div>

      <div class="videos">
        <div class="card" data-aos="fade-up">
          <PlayCircle class="big-icon" />
          <h3>Intro </h3>
          <button @click="play(0)" class="button">
              Watch →
          </button>
        </div>

        <div class="card" data-aos="fade-up" data-aos-delay="100">
          <PlayCircle class="big-icon" />
          <h3>Week 1</h3>
          <button @click="play(1)" class="button">
              Watch →
          </button>
        </div>

        <div class="card" data-aos="fade-up" data-aos-delay="200">
          <PlayCircle class="big-icon" />
          <h3>Week 2</h3>
          <button @click="play(2)">
              Watch →
          </button>
        </div>
        
        <div class="card" data-aos="fade-up" data-aos-delay="300">
          <PlayCircle class="big-icon" />
          <h3>Week 3</h3>
          <button @click="play(3)" class="button">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="400">
          <PlayCircle class="big-icon" />
          <h3>Week 4</h3>
          <button @click="play(4)" class="button">
            Watch →
          </button>
        </div>

        <div class="card" data-aos="fade-up" data-aos-delay="500">
          <PlayCircle class="big-icon" />
          <h3>Week 5</h3>
          <button class="button" @click="play(5)">
            Watch → 
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="600">
          <PlayCircle class="big-icon" />
          <h3>Week 6</h3>
          <button class="button" @click="play(6)">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="700">
          <PlayCircle class="big-icon" />
          <h3>Week 7</h3>>
          <button class="button" @click="play(7)">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="800">
          <PlayCircle class="big-icon" />
          <h3>Week 8</h3>
          <button class="button" @click="play(8)">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="900">
          <PlayCircle class="big-icon" />
          <h3>Week 9</h3>
          <button class="button" @click="play(9)">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="1000">
          <PlayCircle class="big-icon" />
          <h3>Week 10</h3>
          <button class="button" @click="play(10)">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="1100">
          <PlayCircle class="big-icon" />
          <h3>Week 11</h3>
          <button class="button" @click="play(11)">
            Watch →
          </button>
        </div>
        <div class="card" data-aos="fade-up" data-aos-delay="1200">
          <PlayCircle class="big-icon" />
          <h3>Week 12</h3>
          <button class="button">
            Watch →
          </button>
        </div>
      </div>
    </div>
    <div v-else class="form-container">
      <div v-if="source" class="iframe-container">
        <iframe :src="source" class="fullscreen-iframe" allowfullscreen allow="fullscreen"></iframe>
        <div class="escape-hint">Press ESC to go back</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Form View Styles */
.form-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.form-wrapper {
  background: white;
  padding: 60px 40px;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  text-align: center;
  max-width: 400px;
  width: 90%;
  animation: slideUp 0.6s ease-out;
}

.form-title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 12px;
  font-weight: 700;
}

.form-subtitle {
  color: #888;
  margin-bottom: 30px;
  font-size: 1rem;
}

.form-input {
  width: 100%;
  padding: 14px 16px;
  font-size: 1rem;
  border: 2px solid #ddd;
  border-radius: 10px;
  outline: none;
  transition: all 0.3s ease;
  background: #f9f9f9;
}

.form-input:focus {
  border-color: #667eea;
  background: white;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-input::placeholder {
  color: #bbb;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Iframe View Styles */
.iframe-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
}

.fullscreen-iframe {
  width: 100%;
  height: 100%;
  border: none;
  display: block;
}

.escape-hint {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 0.9rem;
  z-index: 1001;
  pointer-events: none;
  animation: fadeInOut 3s ease-out;
}

@keyframes fadeInOut {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.dashboard {
  min-height: 100vh;
  padding: 80px 20px;
  background: linear-gradient(135deg, #0f0f0f, #1a1a2e);
}

.container {
  max-width: 1000px;
  margin: auto;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logout {
  background: #111;
  border: none;
  padding: 10px;
  border-radius: 6px;
  cursor: pointer;
}

.videos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-top: 40px;
}

.card {
  background: rgba(20,20,30,0.9);
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  transition: 0.3s;
}

.card:hover {
  transform: translateY(-5px);
}

.big-icon {
  width: 40px;
  margin-bottom: 10px;
  opacity: 0.7;
}

.button {
  display: inline-block;
  margin-top: 10px;
  background: #111;
  padding: 10px 20px;
  border-radius: 6px;
  text-decoration: none;
  color: white;
}

.button:hover {
  background: #222;
}
@media (max-width: 480px) {
  .dashboard {
    padding: 40px 12px;
  }

  .form-wrapper {
    padding: 40px 20px;
  }

  .videos {
    gap: 12px;
  }

  .card {
    padding: 20px;
  }

  h2 {
    font-size: 1.4rem;
  }
}
</style>