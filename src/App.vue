<template>
  <RouterView />
  <div v-if="showModal" class="modal">
    <p>Пожалуйста, авторизуйтесь для продолжения.</p>
    <button @click="handleAuth" :disabled="loading">
      {{ loading ? 'Загрузка...' : 'Авторизоваться' }}
    </button>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      loading: false,
      errorMessage: '', // Сообщение об ошибке
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
        this.errorMessage = 'Ошибка при проверке авторизации. Попробуйте снова.';
      }
    } else {
      // Если кода нет, показываем модальное окно
      this.showModal = true;
    }
  },
  methods: {
    async handleAuth() {
      this.loading = true;
      this.errorMessage = ''; // Сбрасываем сообщение об ошибке

      try {
        // Запрашиваем уникальный код у бэкенда
        const response = await this.$http.get('https://api-maker-ai.vercel.app/generate-code');
        const {uniqueKey} = response.data;

        // Сохраняем уникальный код в localStorage
        localStorage.setItem('uniqueKey', uniqueKey);

        // Перенаправляем пользователя в Telegram-бота
        window.location.href = `https://t.me/Maker_AI_Official_bot?start=${uniqueKey}`;
      } catch (error) {
        console.error('Ошибка при генерации кода:', error);
        if (error.response) {
          // Ошибка от сервера (например, 404 или 500)
          this.errorMessage = `Ошибка сервера: ${error.response.status} - ${error.response.data.message}`;
        } else if (error.request) {
          // Запрос был сделан, но ответ не получен
          this.errorMessage = 'Сервер не отвечает. Проверьте подключение к интернету.';
        } else {
          // Ошибка при настройке запроса
          this.errorMessage = 'Ошибка при отправке запроса: ' + error.message;
        }
      } finally {
        this.loading = false;
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

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}

.error {
  color: #ff6b6b;
  margin-top: 10px;
  font-size: 16px;
}
</style>
