<template>
  <RouterView />
  <div v-if="showModal" class="modal">
    <p>Пожалуйста, авторизуйтесь для продолжения.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
    };
  },
  async created() {
    try {
      const response = await this.$http.get('https://api-maker-ai.vercel.app/init'); // Укажите URL вашего бэкенда
      if (!response.data.authorized) {
        this.showModal = true;
      }
    } catch (error) {
      console.error('Ошибка при запросе /init:', error);
      this.showModal = true;
    }
  },
};
</script>

<style>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 24px;
  z-index: 1000;
}
</style>