# Push Bot

A conversational AI Telegram bot powered by [Hugging Face](https://huggingface.co/) and TTS (text-to-speech) technology. The bot can handle conversational inputs, maintain context, and reply with both text and voice messages.

## Features

- **AI-Powered Conversations**: Uses a GPT model from Hugging Face to generate contextual responses.
- **Voice Messages**: Converts AI-generated text replies into voice messages using `gTTS`.
- **Context Management**: Maintains chat history for better conversation flow.
- **Reset Command**: Allows users to clear the chat context.

## Setup

### Prerequisites

- Python 3.10 or higher.
- [Telegram Bot Token](https://core.telegram.org/bots#botfather).
- [Hugging Face API Token](https://huggingface.co/docs/api-inference/index).
- [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)

### Installation

~ WIP

### Running the Bot

```bash
python run.py
```

## Usage

-   **/start**: Initiates the conversation with the bot.
-   **/reset**: Clears the conversation context.
-   Send any message to chat with the bot and receive text and voice responses.

## File Structure

-   `run.py`: Entry point to start the bot.
-   `app/handlers.py`: Contains the bot's message handlers and logic.
-   `app/generators.py`: Manages communication with the Hugging Face API.
-   `lib/`: Contains additional dependencies (if any).

### Dependencies

-   `aiogram`: Telegram Bot API framework.
-   `gTTS`: Google Text-to-Speech for voice message generation.
-   `huggingface_hub`: API client for Hugging Face models.
-   `python-dotenv`: Manages environment variables.

### Acknowledgments

-   [Hugging Face](https://huggingface.co/) for AI capabilities.
-   [gTTS](https://pypi.org/project/gTTS/) for text-to-speech conversion.
-   [aiogram](https://aiogram.dev/) for simplifying Telegram bot development.
