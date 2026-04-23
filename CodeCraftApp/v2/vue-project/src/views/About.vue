<script setup>
</script>

<template>
  <section class="about">
    <div class="hero">
      <h1>CodeCraft</h1>
      <p>Learn by building real projects.</p>
    </div>

    <div class="features">
      <div class="box" v-for="(item, i) in features" :key="i">
        <h3>{{ item.title }}</h3>
        <p>{{ item.desc }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
const features = [
  {
    title: "Hands-on Learning",
    desc: "Build games, apps, and real-world projects."
  },
  {
    title: "Beginner Friendly",
    desc: "No experience needed. Start from zero."
  },
  {
    title: "Fast Growth",
    desc: "Go from basics to advanced in weeks."
  }
]
</script>

<style scoped>
.about {
  min-height: 100vh;
  padding: 80px 20px;
  background: linear-gradient(135deg, #0f0f0f, #1a1a2e);
  color: white;
}

.hero {
  text-align: center;
  margin-bottom: 60px;
  animation: fadeUp 0.8s ease;
}

.hero h1 {
  font-size: 3rem;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

.box {
  background: rgba(20,20,30,0.9);
  padding: 30px;
  border-radius: 12px;
  transition: 0.3s;
  animation: fadeUp 0.6s ease;
}

.box:hover {
  transform: translateY(-8px) scale(1.02);
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>