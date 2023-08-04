from pydub.utils import mediainfo


class Clip:
    def __init__(self, image, audio):
        self.image = image
        self.audio = audio

    @property
    def duration(self):
        audio_info = mediainfo(self.audio)
        duration = float(audio_info['duration'])
        return duration

    def __repr__(self):
        return f'image: {self.image}\naudio: {self.audio}\nduration: {self.duration}\n'
