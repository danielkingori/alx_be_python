# # Import the VideoFileClip module from the moviepy.editor library
# from moviepy.editor import VideoFileClip
# def print_video_metadata(video_path):
#  # Create a VideoFileClip object
#     clip = VideoFileClip(video_path)
#  # Print video metadata
# print('Duration: ', clip.duration) # Video duration in seconds
# print('FPS: ', clip.fps) # Frames per second
# print('Size: ', clip.size) # Video size in pixels [width, height]
# # Replace with the actual path to your video file
# print_video_metadata('path_to_your_video_file')


from tinytag import TinyTag
def print_audio_metadata(audio_path):
 # Get the audio file's metadata
 tag = TinyTag.get(audio_path)
 # Print the metadata
 print(tag)
# Replace with the actual path to your audio file
print_audio_metadata('/content/welcome.mp3')




# Import the subprocess library, which allows you to spawn new processes
import subprocess
# Define the path to the image
imgPath = "path/sample.png"
# Define the process to be executed, in this case "hachoir-metadata"
exeProcess = "hachoir-metadata"
# Start the subprocess, passing in the process name and image path
# subprocess.PIPE allows you to redirect the standard output and standard error
# universal_newlines=True allows the output to be in text mode
process = subprocess.Popen([exeProcess,imgPath],
 stdout=subprocess.PIPE,
stderr=subprocess.STDOUT,
universal_newlines=True)
# Initialize an empty dictionary to store the metadata tags
Dic={}
# Loop through each line of the process's standard output
for tag in process.stdout:
 # Strip leading/trailing whitespace and split the line at the colon
 line = tag.strip().split(':')
 # The key is the first part of the split, the value is the last part
 Dic[line[0].strip()] = line[-1].strip()
# Loop through the items in the dictionary
for k,v in Dic.items():
# Print the key and value, separated by a colon
print(k,':', v)