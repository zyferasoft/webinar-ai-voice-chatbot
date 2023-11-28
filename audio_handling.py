import boto3
import speech_recognition as sr
import pygame  # For playing audio


class AudioManager:
    def __init__(self):
        # Initialize audio components
        self.polly_client = boto3.client('polly') # Text-To-Speech model (TTS)
        self.recognizer = sr.Recognizer() # Speech-To-Text model (STT)
        self.microphone = sr.Microphone()

    def text_to_speech(self, text):
        # Convert text to speech using Amazon Polly
        response = self.polly_client.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')
        # Save the audio file and return its path
        filename = "response.mp3"
        with open(filename, 'wb') as file:
            file.write(response['AudioStream'].read())
        return filename

    def speech_to_text(self, audio):
        # Set up the response object
        response = {
            "success": True,
            "error": None,
            "text": None
        }

        # Convert speech to text using speech_recognition
        try:
            text = self.recognizer.recognize_google(audio)
            response["text"] = text
        except sr.UnknownValueError:
            response["error"] = "I couldn't understand the audio"
        except sr.RequestError:
            response["error"] = "Could not request results; check your internet connection"
        except Exception as ex:
            response["error"] = str(ex)
        
        return response

    def record_speech(self):
        # Set up the response object
        response = {
            "success": True,
            "error": None,
            "audi": None
        }

        try:
            # Record the audio
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                print("I am listening, please speak...")
                response["audio"] = self.recognizer.listen(source, timeout=1)

        except sr.RequestError:
            # API was unreachable or unresponsive
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # Speech was unintelligible
            response["error"] = "Unable to recognize speech"
        except sr.WaitTimeoutError:
            # Listening timed out
            response["error"] = "Listening timed out while waiting for phrase to start"

        return response

    def play_response(self):
        # Play the given audio file
        pygame.mixer.init()
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)



