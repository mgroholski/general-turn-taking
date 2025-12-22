import io
import os
import wave

from google.cloud import speech


class ASR:
    def __init__(self, filepath):
        """
        Initialize ASR with an audio file path.

        Args:
            filepath: Path to the audio file to monitor and transcribe
        """
        self.filepath = filepath
        self.client = speech.SpeechClient()
        self.dialogue_sequence = []
        self.last_read_size = 0

        # Audio configuration - adjust these based on your audio format
        self.sample_rate = 16000
        self.language_code = "en-US"

    def has_new_result(self):
        """
        Check if there's new audio data since the last time get_result was called.

        Returns:
            bool: True if there's new audio data, False otherwise
        """
        if not os.path.exists(self.filepath):
            return False

        current_size = os.path.getsize(self.filepath)
        return current_size > self.last_read_size

    def get_result(self):
        """
        Transcribe new audio data using Google Cloud Speech-to-Text and return
        the current dialogue sequence.

        Returns:
            list: The current dialogue sequence (all transcriptions so far)
        """
        if not self.has_new_result():
            return self.dialogue_sequence

        try:
            with open(self.filepath, "rb") as audio_file:
                # Skip to the last read position
                audio_file.seek(self.last_read_size)
                new_audio_data = audio_file.read()

            # Update the last read position
            self.last_read_size += len(new_audio_data)

            if len(new_audio_data) == 0:
                return self.dialogue_sequence

            # Transcribe the new audio
            transcription = self._transcribe_audio(new_audio_data)

            if transcription:
                self.dialogue_sequence.append(transcription)

        except Exception as e:
            print(f"Error processing audio: {e}")

        return self.dialogue_sequence

    def _transcribe_audio(self, audio_data):
        """
        Transcribe audio data using Google Cloud Speech-to-Text.

        Args:
            audio_data: Raw audio bytes to transcribe

        Returns:
            str: Transcribed text, or None if transcription failed
        """
        try:
            # Configure audio and recognition settings
            audio = speech.RecognitionAudio(content=audio_data)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=self.sample_rate,
                language_code=self.language_code,
            )

            # Perform the transcription
            response = self.client.recognize(config=config, audio=audio)

            # Extract the transcription from the response
            transcripts = []
            for result in response.results:
                if result.alternatives:
                    transcripts.append(result.alternatives[0].transcript)

            if transcripts:
                return " ".join(transcripts)

        except Exception as e:
            print(f"Error during transcription: {e}")

        return None

    def reset(self):
        """
        Reset the dialogue sequence. File position tracking continues
        so new audio is still tracked from the current position.
        """
        self.dialogue_sequence = []
