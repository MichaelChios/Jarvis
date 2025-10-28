import importlib

def install_library(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        import pip
        pip.main(['install', package_name])
        print(f"{package_name} has been installed.")

# List of libraries to install
libraries = [
    "SpeechRecognition",
    "aspose-words",
    "webbrowser",
    "subprocess",
    "pyautogui",
    "keyboard",
    "pywhatkit",
    "clipboard",
    "requests",
    "datetime",
    "platform",
    "random",
    "smtplib",
    "pyttsx3",
    "ctypes",
    "psutil",
    "urllib",
    "os",
    "time",
    "email.message",
    "tensorflow",
    "keras",
    "dotenv"
]

for library in libraries:
    install_library(library)

print("All libraries have been installed.")