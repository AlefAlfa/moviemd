from .clip import Clip
from elevenlabs import generate, save
from moviepy.editor import concatenate_videoclips, AudioFileClip, ImageClip
import os


def make_clips(md_data, api_key):
    clips = []
    counter = 0

    for text in md_data[1]:
        audio = generate(
            api_key=api_key,
            text=text,
            voice="pXSOxxxoUAWAwm4KgTe8",
            model="eleven_monolingual_v1"
        )

        filename = f"audio_{counter}.mp3"

        save(
            audio=audio,
            filename=filename
        )

        clip = Clip(image=md_data[0][counter], audio=filename)
        clips.append(clip)
        counter += 1

    counter = 1
    for clip in clips:
        print(f'Clip {counter}')
        print(clip)
        counter += 1

    return clips


def make_output(clips):
    movie_clips = []
    # create moviepy clips
    for clip in clips:
        image_clip = ImageClip(clip.image).set_duration(clip.duration)
        audio_clip = AudioFileClip(clip.audio).set_duration(clip.duration)
        final_clip = image_clip.set_audio(audio_clip)
        movie_clips.append(final_clip)

    # concatinate moviepy clips
    if movie_clips:  # check if movie_clips is not empty
        final_video = concatenate_videoclips(movie_clips)
        final_video.fps = 24
        # fps should be provided here
        final_video.write_videofile("output.mp4", fps=24)
    else:
        print("No clips to concatenate.")

    # clean up root directory
    for clip in clips:
        os.remove(clip.audio)
