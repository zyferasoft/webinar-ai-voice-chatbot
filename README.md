# Voice Chatbot with Speech Recognition and Audio Handling via ChatGPT, LangChain and Amazon Polly TTS

## Description
This project integrates a chatbot with speech recognition and audio handling capabilities. It consists of three main components:

1. **main.py:** The main script that orchestrates the functionality of the chatbot and audio handling. It initializes the chatbot and audio manager, records user speech, processes the speech, and manages the chatbot's responses.

2. **chatbot.py:** Implements the chatbot functionality using the LangChain library and OpenAI. It sets up a conversational AI model, tailored to act as a mathematics teacher, posing questions and interpreting user responses.

3. **audio_handling.py:** Manages audio input and output. It utilizes the Amazon Polly service for text-to-speech conversion and the SpeechRecognition library for speech-to-text conversion.

## Features
- Speech recognition to interpret user speech via google STT
- Text-to-speech capabilities for vocalizing chatbot responses via Amazon Polly TTS
- Customizable chatbot behavior, focusing on mathematics education via LangChain and ChatGPT-4
- Continuous interaction loop for a seamless user experience.

## Installation
- python 3.11 
- amazon polly and chatgpt api-key must be exported to environmental variable or you have to add in the code. 
