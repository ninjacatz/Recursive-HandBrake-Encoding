import subprocess
import os

# ------User-Defined Variables-------
# Directory to begin process:
start_directory = r''
# Directory of HandBrakeCLI executable:
handbrakeCLI_executable_path = r''
# File extensions to encode:
video_extensions_to_encode = ('.mov', '.avi', '.mp4', '.m4v')
# Handbrake Command:
# Add any additional customization to the end of the list
# See https://handbrake.fr/docs/en/latest/cli/cli-options.html for more information
handbrake_command = [
    handbrakeCLI_executable_path,
    '-i',
    'source file path(will be known, do not change)',
    '-o',
    'destination path(will be known, do not change)'
]

def recursiveSearch(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if file.endswith(video_extensions_to_encode):
            performHandbrakeEncoding(directory, file_path, file)
        elif os.path.isdir(file_path):
            recursiveSearch(file_path)

def performHandbrakeEncoding(directory, video_path, video):
    os.chdir(directory)
    # rename original video
    os.rename(video, "renamed-" + video)
    # set renamed video as source file
    handbrake_command[2] = os.path.join(directory, 'renamed-' + video)
    # set original video name as destination
    handbrake_command[4] = video_path
    # perform encoding with HandBrakeCLI
    subprocess.run(handbrake_command, shell=True)
    # remove renamed original video
    os.remove('renamed-' + video)

recursiveSearch(start_directory)