import os
import subprocess

# Define the model
PIPER_MODEL = "en_US-lessac-medium"
OUTPUT_FILE = "output.wav"

def text_to_speech(text):
    """
    Converts text to speech using Piper and plays the output file.
    """
    command = f'echo "{text}" | piper --model {PIPER_MODEL} --output_file {OUTPUT_FILE}'
    subprocess.run(command, shell=True)

    # Play the audio file
    play_command = "aplay output.wav" if os.name != "nt" else "powershell Start-Process output.wav"
    subprocess.run(play_command, shell=True)

if __name__ == "__main__":
    text_to_speech("Hello, Piper is now installed and working!")
