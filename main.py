import atexit
import pathlib
import subprocess
import time


def setup_sound(volume_percent: int = 100):
    subprocess.run(["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "0"])
    subprocess.run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", f"{volume_percent}%"])


def play_video(video_path: pathlib.Path):
    subprocess.run(["ffplay", "-fs", str(video_path.absolute())])


def format_seconds(seconds: int):
    """
    >>> format_seconds(20)
    '00:00:20'
    >>> format_seconds(80)
    '00:01:20'
    >>> format_seconds(3680)
    '01:01:20'
    """
    return f"{seconds // 3600:02}:{(seconds % 3600) // 60:02}:{seconds % 60:02}"


def set_desktop_animation(enable: bool):
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "enable-animations", str(enable).lower()])


def get_record_path(pr: pathlib.Path) -> pathlib.Path:
    pr.mkdir(exist_ok=True)
    other_recordings = list(path_recordings.glob("record_*.mp4"))
    other_recordings.sort()
    if other_recordings:
        last_recording = other_recordings[-1]
        last_recording_number = int(last_recording.stem.split("_")[1])
    else:
        last_recording_number = 0

    return path_recordings / f"record_{last_recording_number + 1}.mp4"


path = pathlib.Path(".")
path_run_once = path / "run_once"
path_recordings = path / "recordings"

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    if path_run_once.exists():
        print("Already running")
        exit(1)

    path_run_once.touch()

    path_record = get_record_path(path_recordings)

    record_process = subprocess.Popen(
        ["ffmpeg", "-f", "pulse", "-ac", "2", "-i", "default", "-f", "v4l2", "-i", "/dev/video1", "-t",
         format_seconds(10),
         "-vcodec", "libx264", path_record.absolute()])

    time.sleep(3)

    setup_sound(5)
    set_desktop_animation(False)

    time.sleep(0.5)

    # play_video(pathlib.Path("/home/afcm/Téléchargements/Jeff_The_Killer_Jumpscare.mp4"))
    play_video(pathlib.Path("/home/afcm/Téléchargements/STORROR_BEST_OF_PARKOUR.mp4"))

    record_process.wait()


    def cleanup():
        path_run_once.unlink()
        set_desktop_animation(True)


    atexit.register(cleanup)
