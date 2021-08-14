# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:21:02 2021

@author: User
"""
import moviepy.editor
from tkinter.filedialog import*

video=askopenfilename()
video=moviepy.editor.VideoFileClip(video)

audio=video.audio

audio.write_audiofile('TKP.mp3')
