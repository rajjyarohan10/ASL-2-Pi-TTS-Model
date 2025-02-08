#!/bin/bash

# Define colors
GREEN="\e[32m"
YELLOW="\e[33m"
RED="\e[31m"
RESET="\e[0m"

echo -e "${YELLOW}Updating system packages...${RESET}"
sudo apt update && sudo apt upgrade -y

echo -e "${YELLOW}Installing dependencies...${RESET}"
if sudo apt install -y python3-pip ffmpeg sox libsox-fmt-all wget; then
    echo -e "${GREEN}Dependencies installed successfully!${RESET}"
else
    echo -e "${RED}Failed to install dependencies. Exiting.${RESET}"
    exit 1
fi

echo -e "${YELLOW}Installing Piper TTS...${RESET}"
if pip3 install --upgrade piper-tts; then
    echo -e "${GREEN}Piper TTS installed successfully!${RESET}"
else
    echo -e "${RED}Piper installation failed. Exiting.${RESET}"
    exit 1
fi

# Define Piper model directory
PIPER_MODEL_DIR="$HOME/.local/share/piper"
mkdir -p "$PIPER_MODEL_DIR"
PIPER_MODEL="en_US-lessac-medium.onnx"
PIPER_JSON="en_US-lessac-medium.onnx.json"

# Check if the model already exists
if [ -f "$PIPER_MODEL_DIR/$PIPER_MODEL" ] && [ -f "$PIPER_MODEL_DIR/$PIPER_JSON" ]; then
    echo -e "${GREEN}Piper voice model already exists! Skipping download.${RESET}"
else
    echo -e "${YELLOW}Downloading Piper voice model...${RESET}"
    
    wget -O "$PIPER_MODEL_DIR/$PIPER_MODEL" "https://github.com/rhasspy/piper/releases/download/v1.0.0/en_US-lessac-medium.onnx"
    wget -O "$PIPER_MODEL_DIR/$PIPER_JSON" "https://github.com/rhasspy/piper/releases/download/v1.0.0/en_US-lessac-medium.onnx.json"

    if [ -f "$PIPER_MODEL_DIR/$PIPER_MODEL" ] && [ -f "$PIPER_MODEL_DIR/$PIPER_JSON" ]; then
        echo -e "${GREEN}Piper voice model downloaded successfully!${RESET}"
    else
        echo -e "${RED}Failed to download Piper voice model. Exiting.${RESET}"
        exit 1
    fi
fi

echo -e "${GREEN}Setup complete! You can now run the TTS system.${RESET}"
