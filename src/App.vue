<template>
  <RouterView />
  <div v-if="showModal" class="modal">
    <p>Пожалуйста, авторизуйтесь для продолжения.</p>
    <button @click="handleAuth">Авторизоваться</button>
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
    // Проверяем, есть ли уникальный код в localStorage
    const uniqueKey = localStorage.getItem('uniqueKey');
    if (uniqueKey) {
      // Если код есть, проверяем статус авторизации
      try {
        const response = await this.$http.get(`https://api-maker-ai.vercel.app/init?uniqueKey=${uniqueKey}`);
        this.showModal = !response.data.authorized;
      } catch (error) {
        console.error('Ошибка при запросе /init:', error);
        this.showModal = true;
      }
    } else {
      // Если кода нет, показываем модальное окно
      this.showModal = true;
    }
  },
  methods: {
    async handleAuth() {
      try {
        // Запрашиваем уникальный код у бэкенда
        const response = await this.$http.get('https://api-maker-ai.vercel.app/generate-code');
        const {uniqueKey} = response.data;

        // Сохраняем уникальный код в localStorage
        localStorage.setItem('uniqueKey', uniqueKey);

        // Перенаправляем пользователя в Telegram-бота
        window.location.href = `https://t.me/Maker_AI_Official_bot?start=${uniqueKey}`; // Замените на ссылку вашего бота
      } catch (error) {
        console.error('Ошибка при генерации кода:', error);
        alert('Произошла ошибка при авторизации. Попробуйте снова.');
      }
    },
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
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 24px;
  z-index: 1000;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
}

button:hover {
  background-color: #0056b3;
}
</style>