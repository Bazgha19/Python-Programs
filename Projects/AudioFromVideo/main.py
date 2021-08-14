#Extract Audio from video

import moviepy.editor

video=moviepy.editor.VideoFileClip('TKP.mp4')

audio=video.audio

audio.write_audiofile('TKP.mp3')