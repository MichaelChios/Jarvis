# Jarvis - AI Personal Assistant

A Python-based AI personal assistant with voice interaction and face recognition capabilities.

## Features

- Voice command recognition and response
- Face recognition and authentication
- Graphical user interface
- Screenshot functionality
- Custom responses and interactions

## Project Structure

```
.
├── Jarvis.py                    # Main assistant implementation
├── faceRecognition.py          # Face recognition module
├── setup.py                    # Project setup and dependencies
├── FaceRecognitionFiles/       # Face recognition resources
│   ├── haarcascade_frontalface_default.xml
│   └── trainner.yml
├── faces/                      # Face training data
│   └── me/
├── GUI/                        # Graphical interface components
│   ├── JarvisButtons.py
│   └── JarvisGUI.py
├── Resources/                  # Additional resources
└── txtFiles/                  # Configuration and response files
    ├── responses1.txt
    ├── responses2.txt
    ├── screenshotnames.txt
    └── whatIcando.txt
```

## Requirements

- Python 3.x
- OpenCV (for face recognition)
- PyQt5 (for GUI)
- Additional dependencies listed in `setup.py`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install dependencies:
```bash
python setup.py install
```

## Usage

Run the main assistant:
```bash
python Jarvis.py
```

For face recognition setup:
```bash
python faceRecognition.py
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV for face recognition capabilities
- PyQt5 for the graphical interface
- Contributors and maintainers