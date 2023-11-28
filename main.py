import chatbot
import audio_handling

def main():
    # Initialize the chatbot and audio handling components
    bot = chatbot.ChatBot()
    audio_manager = audio_handling.AudioManager()

    # Main application loop
    while True:
        # 1. Record user's speech
        user_speech = audio_manager.record_speech()
        # Check if recording was successful
        if user_speech["error"]:
            print(f"Error in speech recording: {user_speech['error']}")
            continue  # Skip to the next loop iteration

        # 2. Convert speech to text
        user_input = audio_manager.speech_to_text(user_speech["audio"])
        # Check if STT was successful
        if user_input["error"]:
            print(f"Error in STT: {user_input['error']}")
            continue  # Skip to the next loop iteration

        # 3. Interact with the chatbot using the converted text
        bot_response = bot.interact_with_chatgpt(user_input["text"])
        print(f"Math ChatBot: {bot_response}")

        # 4. Convert the bot response to speech
        audio_manager.text_to_speech(bot_response)

        # 5. Play the response
        audio_manager.play_response()

if __name__ == "__main__":
    main()
