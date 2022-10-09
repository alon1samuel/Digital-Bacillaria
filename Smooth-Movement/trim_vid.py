from pathlib import Path
import moviepy.editor as mpy
from typing import List

SOURCE_PATH = Path("Smooth-Movement/data/40x_100fps_b5.avi")
TARGET_PATH = Path("Smooth-Movement/data/40x_100fps_b5_trimmed_1.avi")

CUTS = [('00:00:02.30', '00:00:03.10')]
CODEC = 'libx264'


def main(
    source_path: Path,
    target_path: Path,
    cuts: List[str],
):
    video = mpy.VideoFileClip(str(source_path))

    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips)
    final_clip.write_videofile(str(target_path), fps=video.fps, codec='libx264')

if __name__ == '__main__':
    main(SOURCE_PATH, TARGET_PATH, CUTS)