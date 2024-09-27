# Audio Encryption & Decryption Using AES

This repository contains a Python project for recording, encrypting, and decrypting audio using the Advanced Encryption Standard (AES). The project provides secure encryption of audio data, ensuring that it can only be accessed and played with the correct secret key.

## Features
- **Record Audio**: Capture audio from the microphone.
- **AES Encryption**: Encrypt the recorded audio using AES symmetric encryption with a key derived from a user-provided passphrase.
- **Decryption**: Decrypt the encrypted audio with the correct key and play it back.
- **Save to WAV**: Save the encrypted and decrypted audio data as `.wav` files.

## Requirements

To run this project, ensure you have the following libraries installed:

- `numpy`
- `sounddevice`
- `wave`
- `cryptography`

You can install the dependencies with the following command:

```bash
pip install numpy sounddevice cryptography
