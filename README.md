# apple-music---spotify
converts apple music playlist to spotify

needed libs - requests

this code is just a very rough and unpolished display of my thought process of how to convert playlists across streaming services
- open apple music playlist and shift click on top and bottom songs to copy all songs in playlist
- right click -> copy -> paste into text file
- this code makes a list of all song titles and uses them as a search query on spotify api 
- then creates a playlist and adds all song URIs (song ID) taken from the search results

- important note - the bearer must be manually added into the code and is found in the request headers of any request made via browser on spotify.com with a user that is logged in
    - format -> bearer = 'Bearer (bearer token here)'
