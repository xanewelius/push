import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
# Создаем клиента для взаимодействия с API Hugging Face
client = InferenceClient(api_key=os.getenv('AI_TOKEN'))

# Функция для общения с моделью
async def gpt(chat_history):
    # Отправляем весь диалог модели
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",  # Используйте вашу модель
        messages=chat_history,  # История сообщений
        max_tokens=500
    )

    # Возвращаем ответ модели
    return response['choices'][0]['message']['content']
