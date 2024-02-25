# VTT-Snap: Transcribe Videos in a Snap

This script, named Video to Text - Transcribe Videos in a Snap (VTT-Snap), is designed to take a video file and transcribe the audio of the video using Google's Speech Recognition API. The script will first extract one-minute chunks of audio from the video, convert the audio to WAV format, and then pass the audio chunks to the Google Speech Recognition API to transcribe the speech. The transcribed text will be saved in a text file named "recognized.txt".

## Dependencies

- tqdm
- moviepy
- argparse
- speech_recognition
- concurrent.futures


## Usage
``
python convert.py path/to/video.mp4

``


## Steps
1. The script takes a video file as an argument and uses the moviepy library to extract one-minute chunks of audio from the video. 
2. Then, it converts the audio chunks to WAV format using the moviepy library.
3. The script then uses the Google Speech Recognition API to transcribe the speech in the audio chunks.
4. The transcribed speech is saved in a text file called "recognized.txt"
5. Finally, the script removes the chunks and converted files.

## Note

Please note that the script is using Google Speech Recognition API so you need to have an active internet connection to run the script. Also it may take a while to transcribe a long video.


[Full Tutorial](https://tigerzplace.com/vtt-snap-a-simple-and-fast-way-to-automatically-transcribe-videos-to-text/)

VTT-Snap is a python script that allows you to automatically transcribe video to text quickly and easily. This script uses Google's Speech Recognition API to transcribe the audio of the video into text. The transcribed text will be saved in a text file named "recognized.txt". Follow the tutorial on [Tigerzplace](https://tigerzplace.com/vtt-snap-a-simple-and-fast-way-to-automatically-transcribe-videos-to-text/) to learn how to use VTT-Snap to transcribe your videos.

## Tigerzplace 
