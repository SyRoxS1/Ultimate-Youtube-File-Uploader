from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

def split(name,file):
    input_video = name
    output_directory = "videos/"
    segment_duration = 58
    video = VideoFileClip(input_video)
    total_duration = video.duration

    
    start_time = 0
    end_time = min(segment_duration, total_duration)

    i = 1
    while start_time < total_duration:
        output_file = f"{output_directory}{file}_segment_{i}.mp4"
        ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_file)
        i += 1
        start_time = end_time
        end_time = min(start_time + segment_duration, total_duration)

    video.reader.close()
    
#split("videos/output_vertical.mp4",'output_vertical')
