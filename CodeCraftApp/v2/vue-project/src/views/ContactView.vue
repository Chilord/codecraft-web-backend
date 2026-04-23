<script setup>
const phone = "2347043976670"
const message = encodeURIComponent("I want to enroll in CodeCraft")

const link = `https://wa.me/${phone}?text=${message}`
</script>

<template>
  <section class="contact">
    <div class="card">
      <h1>Contact Us</h1>
      <p>Have questions or ready to join?</p>

      <a :href="link" target="_blank" class="whatsapp-btn">
        Chat on WhatsApp →
      </a>
    </div>
  </section>
</template>

<style scoped>
.contact {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0f0f0f, #1a1a2e);
}

.card {
  background: rgba(20,20,30,0.95);
  padding: 50px;
  border-radius: 16px;
  text-align: center;
  animation: fadeUp 0.6s ease;
}

.whatsapp-btn {
  display: inline-block;
  margin-top: 20px;
  background: #25D366;
  padding: 14px 28px;
  border-radius: 8px;
  color: white;
  text-decoration: none;
  font-weight: bold;
  transition: 0.3s;
}

.whatsapp-btn:hover {
  transform: scale(1.05);
}
</style>