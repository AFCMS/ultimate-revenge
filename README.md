# Ultimate Revenge

Forgot to lock your computer? Then you notice your friend's wanting to ruin it? Remotly jumpscare them! And best of all,
record their reaction!

This carefuly crafted Python script will max out the volume, play a video of you choice at full screen
after disabling desktop animations, while recording the webcam.

This software has been tested on Fedora Workstation and require the following:

- [GNOME Desktop Environment](https://www.gnome.org)
- [PipeWire](https://pipewire.org) as audio server
- [FFPLAY/FFMPEG](https://www.ffmpeg.org) installed (required for playing the video and recording webcam)

You can trigger the jumpscare with any tool allowing you to run a command on the target session.
In my case I conveniently use GSConnect + KDE Connect from my phone:

- [GSConnect](https://extensions.gnome.org/extension/1319/gsconnect)
- [KDE Connect](https://kdeconnect.kde.org)

I recommend you this very effective jumpscare (beware if you are subject to epilepsy): https://youtu.be/ToRqXvEfSCQ

## How to run

Create virtualenv:

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Run the script (with your webcam device and video file):

```bash
python main.py /dev/video1 /path/to/video.mp4
```

You can also run the convenience script `run.sh`:

```bash
main.sh /dev/video1 /path/to/video.mp4
```

See `--help` for more options.

Now you can setup a command in GSConnect for exemple to run the script. 