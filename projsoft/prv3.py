from moviepy.editor import VideoFileClip
import subprocess
import numpy as np

def extract_audio(mp4_file, output_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(output_file)

# Create a list of numbers
numbers=[]
for i in range(20):
	numbers.append(i)

# Convert the list to a numpy array
arr = np.array(numbers)

# Shuffle the array in-place
np.random.shuffle(arr)

# Convert the shuffled array back to a list
shuffled_numbers = arr.tolist()
s = 'y'

#for i in shuffled_numbers:
#    print(i)
for i in shuffled_numbers:
    print("The file prvaud" +str(i)+".mp4 is being played")
    mp4_file_path = "/home/sudarshan/prv proj/prv  mov/prvaud "+str(i)+".mp4"
    output_file_path ="/home/sudarshan/prv proj/prv  mov/prvaud "+str(i)+".wav"
    extract_audio(mp4_file_path, output_file_path)
    subprocess.call(['aplay', output_file_path])
    s=str(input("Enter q if u want to stop the songs otherwise enter anything else"))
    if s=='q':
        break
    else:
        pass
