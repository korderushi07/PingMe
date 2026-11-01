
import winsound
from pathlib import Path


SOUND_DIR = (
    Path(__file__).resolve().parents[2]
    / "assets"
    / "sounds"
)


def play_alert_sound(alert_type):

    if alert_type == "Name Mentioned":
        sound_file = SOUND_DIR / "name_alert.wav"

    else:
        sound_file = SOUND_DIR / "keyword_alert.wav"

    if not sound_file.exists():
        print(f"Alert sound not found: {sound_file}")
        return

    winsound.PlaySound(
        str(sound_file),
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )
