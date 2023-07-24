import pytube
import os

# Get the song URL from the user
#song_url = input("Enter the YouTube song URL: ")
#print(os.getcwd() + )
#listOfURLs = ["https://www.youtube.com/watch?v=cxoGE3RJwho", "https://www.youtube.com/watch?v=cZRzf9eD_RU"]
Artist = "Sia"
for i in listOfURLs:
    # Create a YouTube object
    youtube = pytube.YouTube(i)

    # Get the audio stream
    audio_stream = youtube.streams.filter(only_audio=True).first()

    # Get the song title
    song_title = youtube.title

    # Set the output path
    output_path = os.path.join(os.getcwd(), Artist + "\\" + song_title + ".mp3")

    # Download the song
    audio_stream.download(output_path)

    # Print a success message
    print("Song downloaded successfully!")
