import os
import ffmpeg

in_filepath = input("Input a file: ")
in_filepath = in_filepath.replace("\"", "")
with open(in_filepath) as f:
    filename = f.name

(ffmpeg
    .input(in_filepath)
    .output(os.path.splitext(filename)[0]+'.wav')
    .run()
 )
