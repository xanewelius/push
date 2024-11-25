from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from gtts import gTTS
from app.generators import gpt

# Создаем маршрутизатор
router = Router()

# Класс для состояний сессии
class Generate(StatesGroup):
    text = State()

# Команда /start, приветствие
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет! Начнем общаться.')
    await state.clear()  # Очищаем состояние (если было)

# Основной обработчик сообщений
@router.message(F.text)
async def handle_message(message: Message, state: FSMContext):
    # Получаем текущий контекст (историю сообщений) из состояния
    context = await state.get_data()
    chat_history = context.get('chat_history', [])

    # Добавляем текущее сообщение в историю
    chat_history.append({"role": "user", "content": message.text})
    await state.update_data(chat_history=chat_history)

    # Отправляем весь контекст (историю) модели
    response = await gpt(chat_history)

    # Добавляем ответ модели в историю
    chat_history.append({"role": "assistant", "content": response})
    await state.update_data(chat_history=chat_history)

    voice = gTTS(response, lang='ru')
    voice.save("response.mp3")
    voice_file = FSInputFile("response.mp3")
    
    # Отправляем голосовое сообщение
    await message.reply_voice(voice_file)

# Команда /reset для сброса контекста
@router.message(Command('reset', prefix='/'))
async def reset_chat(message: Message, state: FSMContext):
    await state.clear()  # Очищаем состояние
    await message.answer("Контекст очищен. Начнем сначала!")
