import requests
import json

def get_lyrics(song_name):
  """Retrieves the lyrics of a song using its name.

  Args:
    song_name: The name of the song.

  Returns:
    The lyrics of the song as a string.

  Raises:
     requests.exceptions.HTTPError: If the request to the Lyrics.com API fails.
  """

  url = "https://api.lyrics.ovh/v1/{}".format(song_name.replace(" ", "%20"))
  response = requests.get(url)
  if response.status_code != 200:
    if response.status_code == 404:
      return None
    else:
      raise requests.exceptions.HTTPError("Error retrieving lyrics: {}".format(response.status_code))

  data = json.loads(response.content)
  return data["lyrics"]

if __name__ == "__main__":
  song_name = input("Enter the name of the song: ")
  lyrics = get_lyrics(song_name)
  if lyrics is not None:
    print(lyrics)
  else:
    print("The song was not found.")
