import requests, time, json

bearer = ''
UIRs = []

fpath = input("please paste the file path to your text file -> ")
f = open(r"{}".format(fpath), "r")
lines = f.readlines()
song_names = []
for line in lines:
    a = line.split('		')
    song_names.append(a[0])


choice = input("please type 1 to make a playlist with these songs!\nOR\nplease type 2 to close the program\n->")
if choice == '1':
    user_id = input("please enter user ID -> ")
    playlist_name = input("please enter playlist name -> ")
    print('making playlist...')
    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    request_body = json.dumps({
            "name": playlist_name,
            "description": "made wit code",
            "public": False 
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            'authorization': bearer})
    if response.status_code == 201:
        print("playlist created!")
        playlist_id = response.json()['id']

    for name in song_names:
        try:
            r = name.replace('&', 'and')
            search_q = r
            url = f"https://api-partner.spotify.com/pathfinder/v1/query?operationName=searchDesktop&variables=%7B%22searchTerm%22%3A%22{search_q}%3F%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22numberOfTopResults%22%3A5%2C%22includeAudiobooks%22%3Afalse%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22977d09e29d2e5befe6dc29cff9e0458b6a0cbfa8facaf60b7c1cf53b10971c95%22%7D%7D"

            response = requests.post(url = url, headers={"Content-Type":"application/json", 
                                'authorization': bearer})
            obj = response.json()

            print('song found: ', obj['data']['searchV2']['tracksV2']['items'][0]['item']['data']['uri'], '-' , obj['data']['searchV2']['tracksV2']['items'][0]['item']['data']['name'])
            song = obj['data']['searchV2']['tracksV2']['items'][0]['item']['data']['uri']
            UIRs.append(song)
        except KeyError or IndexError:
                print("error finding ", name)
                continue
    endpoint_url2 = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request_body2 = json.dumps({
            "uris" : UIRs
            })
    response = requests.post(url = endpoint_url2, data = request_body2, headers={"Content-Type":"application/json", 
                            'authorization': bearer})
    if response.status_code == 201:
        print('added your songs to the playlist!')
else:
    print("closing terminal...")
    print("exit()")