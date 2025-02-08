import os
import subprocess
import random
import string
import time

# Define the Piper model
PIPER_MODEL = "en_US-lessac-medium"
OUTPUT_DIR = "tts_outputs"  # Directory to save generated files

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_random_filename():
    """Generate a short random filename for the .wav file."""
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Short, readable filename
    return os.path.join(OUTPUT_DIR, f"tts_{random_str}.wav")

def text_to_speech():
    """Asks for user input, generates speech, saves, plays, and deletes the file."""
    text = input("Enter text to speak: ").strip()
    
    if not text:
        print("❌ No text entered. Exiting...")
        return

    # Generate random filename
    output_file = generate_random_filename()

    # Test Different Speed Values
    # --length-scale 1.5 # Slight slower
    # --length-scale 2.0 # Much slower
    # --length-scale 2.5 # Very slow

    # Control Speech Ratios
    print(f"🗣️ Generating speech for: \"{text}\"")
    command = f'echo "{text}" | piper --model {PIPER_MODEL} --length-scale 1.8 --output_file "{output_file}"'
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Hide Piper output

    if not os.path.exists(output_file):
        print("❌ Failed to generate audio.")
        return

    print(f"🎵 Playing: {output_file}")
    
    # Play the audio file
    play_command = f"ffplay -nodisp -autoexit {output_file}" if os.name != "nt" else f"powershell Start-Process {output_file}"
    subprocess.run(play_command, shell=True)

    # Wait for a short moment before deleting (to prevent errors)
    time.sleep(1)

    # Delete the file
    os.remove(output_file)
    print(f"🗑️ Deleted: {output_file}")

if __name__ == "__main__":
    while True:
        text_to_speech()
        cont = input("🔄 Generate another speech? (y/n): ").strip().lower()
        if cont != 'y':
            print("👋 Exiting...")
            break
