<script setup>
import ProCoderImage from '../../maniscoding.jpg'
import { Rocket, Brain, Target } from 'lucide-vue-next'
</script>

<template>
  <div class="ajogrid">
    <!-- HERO -->
    <section 
      class="hero"
      :style="{ backgroundImage: `url(${ProCoderImage})` }"
    >
      <div class="overlay"></div>

      <div class="content left">
        <h1 data-aos="fade-right">
          Build your first web app with us
        </h1>

        <p data-aos="fade-right" data-aos-delay="200">
          Go from zero to real projects — games, apps, and tools you can actually show off.
        </p>

        <RouterLink 
          to="/register" 
          class="button glow"
          data-aos="fade-right"
          data-aos-delay="400"
        >
          Start Now →
        </RouterLink>
      </div>
    </section>

    <!-- SECTION: WHY -->
    <section class="section">
      <div class="container">
        <h2 data-aos="fade-up">Why CodeCraft?</h2>

        <div class="grid">
          <div data-aos="fade-up" class="area">
            <Rocket class="icon" />
            <h3>Build Real Projects</h3>
            <p>No theory overload. You’ll create games, apps, and tools from day one.</p>
          </div>

          <div data-aos="fade-up" data-aos-delay="100" class="area">
            <Brain class="icon" />
            <h3>Learn by Doing</h3>
            <p>Every lesson leads to something you can run, test, and improve.</p>
          </div>

          <div data-aos="fade-up" data-aos-delay="200" class="area">
            <Target class="icon" />
            <h3>Beginner Friendly</h3>
            <p>No experience needed. Just curiosity and consistency.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: WHAT YOU'LL BUILD -->
    <section class="section alt">
      <div class="container">
        <h2 data-aos="fade-up">What You’ll Build</h2>

        <ul>
          <li data-aos="fade-left">🦖 A game in Scratch</li>
          <li data-aos="fade-left" data-aos-delay="100">🖥️ A CLI tool in C</li>
          <li data-aos="fade-left" data-aos-delay="200">🚀 A space game in Python</li>
          <li data-aos="fade-left" data-aos-delay="300">🌐 A to do list web app</li>
        </ul>
      </div>
    </section>

    <!-- FINAL CTA -->
    <section class="cta">
      <h2 data-aos="zoom-in">
        Ready to build something real?
      </h2>

      <RouterLink 
        to="/register" 
        class="button glow"
        data-aos="zoom-in"
        data-aos-delay="200"
      >
        Join CodeCraft →
      </RouterLink>
    </section>
  </div>
</template>

<style scoped>

/* HERO */
.hero {
  position: relative;
  width: 100vw;
  height: 100vh;
  margin-left: 0px;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
}

/* gradient overlay */
.overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    rgba(10,10,20,0.9),
    rgba(20,20,40,0.7)
  );
}

/* LEFT alignment */
.content.left {
  position: relative;
  z-index: 1;
  max-width: 600px;
  padding-left: 60px;
}

h1 {
  font-size: 2.8rem;
  margin-bottom: 1rem;
}

p {
  opacity: 0.85;
  margin-bottom: 2rem;
}

/* SECTIONS */
.section {
  padding: 80px 20px;
  background: linear-gradient(135deg, #0f0f0f, #1a1a2e);
}

.section.alt {
  background: linear-gradient(135deg, #141414, #202040);
}

.container {
  max-width: 1000px;
  margin: auto;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

h2 {
  text-align: center;
  margin-bottom: 40px;
}

/* LIST */
ul {
  list-style: none;
  padding: 0;
  text-align: center;
}

li {
  margin: 15px 0;
  font-size: 1.2rem;
}

/* CTA */
.cta {
  text-align: center;
  padding: 100px 20px;
  background: linear-gradient(135deg, #0a0a0a, #151530);
}

/* BUTTON */
.button {
  background: #111;
  color: white;
  padding: 12px 28px;
  border-radius: 8px;
  transition: all 0.3s ease;
  display: inline-block;
}

.button:hover {
  transform: scale(1.08);
  background: #222;
}

.glow {
  box-shadow: 0 0 20px rgba(255,255,255,0.3);
}
p {
  font-size: 30px;
}
.icon {
  width: 40px;
  height: 40px;
  margin-bottom: 10px;
  opacity: 0.8;
}

.area:hover {
  cursor: pointer;
  padding: 2px;
  background-color: gray;
  animation: slideUp;
  animation-duration: 1.5s;
  border-radius: 5px;

}

@keyframes slideUp {
  0% {
    transform: translateY(50px);
    opacity: .4;
  } 
  50% {
    transform: translateY(50px);
    opacity: .6;
  }
  100% {
    transform: translateY(0px);
    opacity: 1;
  }
}
</style>