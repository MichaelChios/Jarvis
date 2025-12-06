# Jarvis - Voice-Activated AI Assistant

A Python-based voice-activated personal assistant with face recognition, GUI interface, and multiple automation features.

## Overview

Jarvis is a comprehensive voice-activated assistant that combines speech recognition, text-to-speech, face recognition, and GUI controls to provide a fully interactive AI assistant experience. The system can process voice commands, perform various automation tasks, and includes facial recognition capabilities for personalized interactions.

## Features

### Core Functionality
- **Voice Recognition & Response**: Uses speech recognition to understand voice commands and responds with text-to-speech output
- **Face Recognition**: Captures and recognizes faces using OpenCV and Haar Cascade classifiers
- **GUI Interface**: User-friendly graphical interface for interaction and control
- **Web Integration**: Can search the web, fetch information, and control web browsers
- **Automation Features**: Handles tasks like taking screenshots, file management, and system control

### Capabilities
- Natural language processing and response handling
- Email integration and messaging capabilities
- Document creation and conversion (DOCX to PDF)
- System information retrieval and monitoring
- Keyboard and mouse automation
- Clipboard management

## Project Structure

```
Jarvis/
├── Jarvis.py                           # Main application entry point
├── faceRecognition.py                  # Face recognition and capture module
├── setup.py                            # Dependency installation script
├── README.md                           # This file
│
├── GUI/
│   ├── JarvisGUI.py                   # Main GUI interface
│   └── JarvisButtons.py                # GUI button components
│
├── FaceRecognitionFiles/
│   ├── haarcascade_frontalface_default.xml  # Face detection cascade
│   └── trainner.yml                   # Trained face recognition model
│
├── faces/
│   └── me/                            # Captured face images directory
│       └── readme.txt
│
├── txtFiles/
│   ├── responses1.txt                 # Response templates
│   ├── responses2.txt                 # Additional responses
│   ├── whatIcando.txt                 # Capabilities description
│   └── screenshotnames.txt            # Screenshot naming log
│
└── Resourses/                         # Resource files directory
```

## Installation

### Prerequisites
- Python 3.7 or higher
- Webcam (for face recognition features)
- Microphone (for voice recognition)
- Speakers (for text-to-speech output)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Jarvis
   ```

2. **Install dependencies** (automatic)
   ```bash
   python setup.py
   ```
   
   Or manually install key packages:
   ```bash
   pip install SpeechRecognition pyttsx3 opencv-python tensorflow keras python-dotenv pyautogui keyboard pywhatkit clipboard requests aspose-words docx2pdf
   ```

## Usage

### Starting Jarvis

**Via GUI Interface**:
```bash
python GUI/JarvisGUI.py
```

**Via Command Line**:
```bash
python Jarvis.py
```

### Voice Commands

Once running, Jarvis will:
1. Listen for voice input from your microphone
2. Recognize and process your commands
3. Respond with appropriate actions or text-to-speech replies

### Face Recognition

The system can capture and recognize faces:
- **Capture Mode**: Records 50 face samples from your webcam
- **Recognition Mode**: Identifies faces in real-time video

## Configuration

Create a `.env` file in the project root for sensitive configuration:
```
# Email configuration
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# API Keys (if needed)
API_KEY=your_api_key
```

## Key Modules

### Main Application (Jarvis.py)
- Handles speech recognition and synthesis
- Manages core AI assistant logic
- Controls automation and integration features

### Face Recognition (faceRecognition.py)
- `captureFaces()`: Captures 50 face samples from webcam
- `recognizeFaces()`: Recognizes faces in real-time

### GUI (GUI/JarvisGUI.py & GUI/JarvisButtons.py)
- Provides graphical user interface
- Manages button controls and visual feedback

## Technologies Used

- **Speech Recognition**: `SpeechRecognition` library
- **Text-to-Speech**: `pyttsx3`
- **Computer Vision**: OpenCV (cv2)
- **GUI**: Tkinter (implied from GUI structure)
- **Document Processing**: `python-docx`, `docx2pdf`
- **Automation**: `pyautogui`, `keyboard`
- **Deep Learning**: TensorFlow & Keras
- **System Interaction**: psutil, subprocess, ctypes

## Notes

- Ensure your microphone and webcam are properly configured and accessible
- Face recognition requires adequate lighting for optimal accuracy
- Some features may require additional setup (email authentication, API keys, etc.)
- The system uses custom response files for varied interaction patterns

## Future Enhancements

Potential improvements could include:
- Expanded voice command vocabulary
- Cloud integration for remote access
- Machine learning model improvements
- Multi-language support
- Advanced NLP capabilities

## Author

MichaelChios

## Support

For issues, questions, or contributions, please contact the project maintainer or open an issue in the repository.
