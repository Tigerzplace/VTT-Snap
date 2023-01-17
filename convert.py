import os
import tqdm
import argparse
import moviepy.editor as mp
import speech_recognition as sr 
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from concurrent.futures import ProcessPoolExecutor, as_completed


def get_args():
    parser = argparse.ArgumentParser(description='Extract audio from video and transcribe it')
    parser.add_argument('video_file', metavar='video_file', type=str, help='python convert.py path/to/video.mp4')
    return parser.parse_args()


def process_audio(r, video_file, i, l):
    ffmpeg_extract_subclip(video_file, l[i]-2*(l[i]!=0), l[i+1], targetname="parts/cut{}.mp4".format(i+1))
    clip = mp.VideoFileClip(r"parts/cut{}.mp4".format(i+1)) 
    clip.audio.write_audiofile(r"audios/audio{}.wav".format(i+1))
    with sr.AudioFile("audios/audio{}.wav".format(i+1)) as source:
        r.adjust_for_ambient_noise(source)  
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    return result

def process_video(video_file):
    try:
        clip = VideoFileClip(video_file)
        num_seconds_video = int(clip.duration)
        l=list(range(0,num_seconds_video+1,60))

        with open('recognized.txt', mode='w') as file:
            file.write("Recognized Speech:\n")
            r = sr.Recognizer()
            with ProcessPoolExecutor() as executor:
                futures = [executor.submit(process_audio, r, video_file, i, l) for i in range(len(l)-1)]
                for future in tqdm.tqdm(as_completed(futures), total=len(futures)):
                    file.write(future.result() + '\n')
    except Exception as e:
        print(e)
    finally:
        # remove
        chunk_path = "parts"
        converted_path = "audios"

        if os.path.exists(chunk_path):
            for file in os.listdir(chunk_path):
                os.remove(os.path.join(chunk_path, file))

        if os.path.exists(converted_path):
            for file in os.listdir(converted_path):
                os.remove(os.path.join(converted_path, file))

        print("Finally ready!")

#process_video("../laptop.mp4")

if __name__ == "__main__":
    args = get_args()
    process_video(args.video_file)
