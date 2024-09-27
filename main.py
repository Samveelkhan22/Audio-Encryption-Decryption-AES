import sounddevice as sd
import numpy as np
import hashlib
import wave

# Settings for the audio stream
fs = 44100  # Sample rate
duration = 10  # Duration of recording in seconds

# Convert audio data to integer format
def convert_audio_to_int(audio_data):
    return np.array(audio_data * (2**15 - 1), dtype=np.int16)

# Convert audio data to float format
def convert_audio_to_float(audio_data):
    return audio_data.astype(np.float32) / (2**15 - 1)

# Encrypt the audio data using XOR encryption
def encrypt_audio(audio_data, key):
    return audio_data ^ key

# Decrypt the audio data using XOR encryption
def decrypt_audio(encrypted_data, key):
    return encrypted_data ^ key

# Record audio
def record_audio():
    print('Recording...')
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    print('Recording stopped.')
    return audio_data

# Save audio data to WAV file
def save_audio_to_wav(audio_data, filename):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(np.array(audio_data * (2**15 - 1), dtype=np.int16).tobytes())

# Generate a key based on Caesar Cipher
def generate_key(text_to_encrypt):
    key = sum(ord(char) for char in text_to_encrypt)
    return key

# Main function
def main():
    # Get the text to encrypt
    text_to_encrypt = input("Enter the text to encrypt: ")

    # Generate secret key based on Caesar Cipher
    key = generate_key(text_to_encrypt)
    print("Secret key:", key)

    # Record audio
    audio_data = record_audio()

    # Convert audio data to integer format
    audio_data_int = convert_audio_to_int(audio_data)

    # Encrypt the audio data
    encrypted_audio = encrypt_audio(audio_data_int, key)
    print('Audio data encrypted.')

    # Ask for decryption
    decrypt_option = input("Do you want to decrypt the audio? (yes/no): ").lower()

    if decrypt_option == 'yes':
        # Flag for correct decryption
        decrypted = False

        while not decrypted:
            # Get the secret key
            key_input = int(input("Enter the secret key: "))

            # Check if the entered key is correct
            if key_input != key:
                print("Please enter the correct key.")
                retry_option = input("Do you want to retry? (yes/no): ").lower()
                if retry_option != 'yes':
                    print("You are not allowed to hear this audio.")
                    return
            else:
                # Decrypt the audio data
                decrypted_audio = decrypt_audio(encrypted_audio, key_input)
                print('Audio data decrypted.')

                # Convert audio data to float format
                decrypted_audio_float = convert_audio_to_float(decrypted_audio)

                # Save decrypted audio to WAV file
                save_audio_to_wav(decrypted_audio_float, "decrypted_audio.wav")
                print("Decrypted audio saved to decrypted_audio.wav")

                # Play the decrypted audio
                print('Playing decrypted audio...')
                sd.play(decrypted_audio_float, fs)
                sd.wait()

                # Set decrypted flag to True
                decrypted = True
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
