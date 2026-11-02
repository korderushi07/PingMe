# PingMe

**Never miss when you're mentioned in an online meeting.**

PingMe is a local-first Windows desktop app built to solve a simple problem: during online meetings, it is easy to miss when someone says your name or brings up a topic you need to pay attention to—especially when you're presenting, multitasking, or focused on another task.

PingMe listens to your computer's system audio, transcribes speech locally, and alerts you when your name or configured keywords are detected. This lets you stay focused on your work without having to monitor every moment of the conversation.

## The Problem

Online meetings often require people to divide their attention between the conversation, shared screens, notes, and other work. As a result, important mentions can go unnoticed.

PingMe is designed to help with that by:
- Notifying you when your name or a configured variation is mentioned.
- Alerting you when selected keywords or topics come up.
- Providing a visible popup, desktop notification, and distinct alert sound.
- Running locally, without uploading meeting audio to a remote transcription service.

PingMe is an assistive alert tool. It does not join meetings, record them, or replace active participation.

## Features

- Captures Windows system audio through WASAPI loopback.
- Transcribes audio locally using [faster-whisper](https://github.com/SYSTRAN/faster-whisper).
- Detects your name, configured name variations, and watched keywords.
- Shows Windows notifications and floating on-screen alerts.
- Plays separate custom sounds for name and keyword alerts.
- Provides a settings window to configure detection.
- Keeps a temporary alert feed for the current session; it does not maintain persistent alert history.

## How It Works

```text
Online meeting audio
        │
        ▼
Windows system audio capture
        │
        ▼
Audio chunk processing
        │
        ▼
Local speech transcription
        │
        ▼
Name and keyword detection
        │
        ▼
Desktop notification · Popup · Alert sound
```

Audio is processed locally by the application. PingMe does not upload or save captured audio.

## Tech Stack

| Area | Technology |
|---|---|
| Desktop UI | Python, PySide6 |
| Audio capture | PyAudioWPatch, WASAPI loopback |
| Speech recognition | faster-whisper, CTranslate2 |
| Audio processing | SciPy |
| Output-device detection | pycaw, comtypes |
| Notifications | winotify |
| Packaging | PyInstaller, Inno Setup |

## Project Structure

```text
PingMe/
├── assets/
│   └── sounds/              # Custom alert sounds
├── src/
│   ├── audio/               # System audio capture and device selection
│   ├── detection/           # Name and keyword detection
│   ├── notifications/       # Toast notifications, sounds, cooldowns
│   ├── transcription/       # Whisper model and audio worker
│   └── ui/                  # Main window, settings, alert popup
├── config.py
├── main.py
├── run_pingme.py            # Application entry point
├── requirements.txt
└── PingMe.iss               # Inno Setup installer configuration
```

## Development Setup

### Requirements

- Windows
- Python
- A working audio output device

### Setup

```powershell
# Clone the repository
git clone https://github.com/korderushi07/Hearken.git
cd Hearken

# Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python run_pingme.py
```

The Whisper model may need to be downloaded the first time it is initialized.

## Configuration

Open **Settings** in PingMe to configure:

- Your name and name variations
- Watched keywords
- Name alerts on or off
- Keyword alerts on or off

In development, settings are stored in `settings.json`. In a packaged Windows build, settings are stored under `%APPDATA%\PingMe` so they remain separate from the application installation.

Custom alert audio files are stored in `assets/sounds/`:

- `name_alert.wav`
- `keyword_alert.wav`

## Build

The project uses PyInstaller to create a Windows application build.

```powershell
pyinstaller --noconfirm --clean --onedir --windowed --name PingMe --add-data "assets;assets" --collect-all faster_whisper --collect-all ctranslate2 --collect-all av --collect-all PySide6 --hidden-import pyaudiowpatch --hidden-import pycaw --hidden-import comtypes --hidden-import winotify run_pingme.py
```

The application build is generated in:

```text
dist/PingMe/
```

To create a Windows installer, open `PingMe.iss` with Inno Setup Compiler and compile it. The installer is generated in the configured output directory.

## Privacy and Data

- Audio capture and transcription are performed locally.
- Captured audio is processed in memory and is not stored by the application.
- No audio is uploaded to a remote service.
- Alert entries are temporary and are not persisted as history.
- User preferences are stored locally in `settings.json` during development or `%APPDATA%\PingMe` in the packaged build.

## Notes

- PingMe is designed for Windows system-audio capture, so it can work with audio from supported online meeting applications without a meeting-platform-specific integration.
- Audio capture depends on a supported Windows output/loopback device.
- The first run may take longer while the speech-recognition model is downloaded and initialized.
