import io
import tempfile
import sounddevice as sd
import soundfile as sf
import whisper
from gtts import gTTS
import os

# Load Whisper model once
whisper_model = whisper.load_model("base")

def speech_to_text(audio_file_path: str):
    """
    Convert speech audio file to text using Whisper.
    """
    try:
        result = whisper_model.transcribe(audio_file_path)
        return result.get("text", "")
    except Exception as e:
        print(f"Voice Agent STT error: {e}")
        return ""

def text_to_speech(text: str, lang="en"):
    """
    Convert text to speech using gTTS and save to temp file.
    """
    try:
        tts = gTTS(text=text, lang=lang)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        print(f"Voice Agent TTS error: {e}")
        return None

if __name__ == "__main__":
    # Example TTS
    audio_path = text_to_speech("Hello, this is a test of the finance assistant voice agent.")
    print(f"Audio saved at: {audio_path}")

    # You can play audio with e.g., playsound or any player
    # And for STT, supply a path to recorded audio and call speech_to_text
