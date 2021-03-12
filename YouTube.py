from pytube import YouTube
import time
from datetime import datetime


# Banner
print("""
 █████ █████                     ███████████            █████                 ███████████           █████             █████                        
░░███ ░░███                     ░█░░░███░░░█           ░░███                 ░░███░░░░░░█          ░░███             ░░███                         
 ░░███ ███    ██████  █████ ████░   ░███  ░  █████ ████ ░███████   ██████     ░███   █ ░   ██████  ███████    ██████  ░███████    ██████  ████████ 
  ░░█████    ███░░███░░███ ░███     ░███    ░░███ ░███  ░███░░███ ███░░███    ░███████    ███░░███░░░███░    ███░░███ ░███░░███  ███░░███░░███░░███
   ░░███    ░███ ░███ ░███ ░███     ░███     ░███ ░███  ░███ ░███░███████     ░███░░░█   ░███████   ░███    ░███ ░░░  ░███ ░███ ░███████  ░███ ░░░ 
    ░███    ░███ ░███ ░███ ░███     ░███     ░███ ░███  ░███ ░███░███░░░      ░███  ░    ░███░░░    ░███ ███░███  ███ ░███ ░███ ░███░░░   ░███     
    █████   ░░██████  ░░████████    █████    ░░████████ ████████ ░░██████     █████      ░░██████   ░░█████ ░░██████  ████ █████░░██████  █████    
   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░      ░░░░░░░░ ░░░░░░░░   ░░░░░░     ░░░░░        ░░░░░░     ░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░
""")

# Spaces
print("")
print("")
print("_" * 60)

# User YouTube Link Input
inputLink = input("Enter YouTube link here: ")
try:
    youtubeLink = YouTube(inputLink)
except:
    # Spaces
    print("")

    print("[*] Enter a valid YouTube Video url!")
    time.sleep(0.5)
    exit()

# Spaces
print("")

print("[+] Fetching Data...")

# Fetch Video Information
# Spaces
print("")
print("")
try:
    print("YouTube Video Title: " + youtubeLink.title)
    print("YouTube Video Views: ", youtubeLink.views, "Views")
    print("YouTube Video Length: ", youtubeLink.length, "Seconds")
except:
    exit()

# Download YouTube Video
# Spaces
print("")
print("")

try:
    video = youtubeLink.streams.get_highest_resolution()
except:
    exit()
# User Video Path Input / Download Video
inputPath = input("Enter video path: ")
# Spaces
print("")

print("[+] Fetching Metadata...")
time.sleep(1)
# Spaces
print("")

print("[+] Saving Video...")

video.download(output_path=inputPath)

# Spaces
print("")
print("")

print("[+] Video saved on", datetime.now())
exit()

# Save in current Directory
if inputPath == "":
    video.download(output_path=inputPath)
    exit()


