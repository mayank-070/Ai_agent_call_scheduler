# Ai_agent_call_scheduler


This project is a desktop application designed to interact with users through speech and text. It uses various machine learning models, APIs, and Natural Language Processing (NLP) techniques to process user inputs, recognize speech, perform sentiment analysis, schedule meetings, and respond intelligently.

## Features

- **Speech-to-Text**: Users can speak to the assistant, and the system will convert speech into text.
- **Text-to-Speech**: The AI replies through audio.
- **Sentiment Analysis**: The AI analyzes the sentiment of user inputs (positive, negative, neutral) and responds accordingly with an emoji.
- **Meeting Scheduler**: The assistant can schedule meetings based on user requests.
- **Personal Information**: The assistant stores and displays business-related information such as names, amounts paid, and business needs.
- **Calendar Integration**: A calendar widget to display events and reminders.

## Requirements

- Python 3.x
- External libraries:
  - `openai`
  - `speech_recognition`
  - `pyttsx3`
  - `PIL` (Pillow)
  - `tkinter`
  - `nltk`
  - `google-generativeai`
  - `tkcalendar`
  - `wtforms`

You can install the required libraries using `pip`:

```bash
pip install openai speech_recognition pyttsx3 pillow nltk google-generativeai tkcalendar wtforms
