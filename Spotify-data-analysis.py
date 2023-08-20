import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
client_id = "Id"
client_secret = "secret"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

#importing Json files and making a dataframe containing all the jsons
folder_path = r'[FILE PATH OF FOLDER CONTAINING JSON FILES]'  # specify the path to the folder containing the JSON files
df = pd.DataFrame()

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        data = pd.read_json(file_path)
        df = pd.concat([df, data], ignore_index=True)
#importing Json files and making a dataframe containing all the jsons

#editing the df and adding it to a excel file
df.drop(['username','conn_country','platform','ip_addr_decrypted','user_agent_decrypted','episode_name','episode_show_name','spotify_episode_uri','reason_start','reason_end','shuffle','skipped','offline','offline_timestamp','incognito_mode'],axis = 1,inplace = True)  # dropping columns which aren't needed
df.dropna(inplace = True)    #droping rowss in the df not containing needed information(usually are podcast episodes)
df = df.sort_values('ts')    #sorting  the df wrt to date and time 
#editing the df and adding it to a excel file

#extracting top 100 tracks
itern = 0
Top100_uri = []
a = df['spotify_track_uri'].value_counts()
#pprint(sp.track("spotify:track:4nyF5lmSziBAt7ESAUjpbx"))
for x in a.items():
    Top100_uri.append(x[0])
    if itern == 100: break
    itern +=1
#extracting top 100 tracks

# ONLY USED IF ALL THE TRACKS ARE TO BE GONE THROUGH (NOT JUST 100)
'''
uniqueValues = (df['spotify_track_uri']._append(df['spotify_track_uri'])).unique() #all unique Uri's in df
'''


#accesses the api for track data and is stored in another excel sheet 
song_feature_list = {}
n = 0
for x in Top100_uri:
    art = sp.track(x) # searching track from uri, taken from Top100_uri
    aud_any = sp.audio_features(x) # searching audio features from uris fromm Top100_uri
    song_feature_list[x] = {}  #dictionary to store everything

    song_feature_list[x]["Track_name"] = art["name"]
    song_feature_list[x]["Album"] = art["album"]["name"]
    song_feature_list[x]["Artist"] = art["artists"][0]["name"]
    song_feature_list[x]["duration_ms"] = art["duration_ms"]
    song_feature_list[x]["Popularity"] = art["popularity"]

    if aud_any == [None]: #made because not all songs have audio features 
        continue
    song_feature_list[x]['acousticness'] = aud_any[0]["acousticness"]
    song_feature_list[x]['danceability'] = aud_any[0]["danceability"]
    song_feature_list[x]['energy'] = aud_any[0]["energy"]
    song_feature_list[x]['instrumentalness'] = aud_any[0]["instrumentalness"]
    song_feature_list[x]['liveness'] = aud_any[0]["liveness"]
    song_feature_list[x]['loudness'] = aud_any[0]["loudness"]
    song_feature_list[x]['speechiness'] = aud_any[0]["speechiness"]
    song_feature_list[x]['tempo'] = aud_any[0]["tempo"]
    song_feature_list[x]['valence'] = aud_any[0]["valence"]
    n = n+1
    print(n)
#accesses the api for track data and is stored in another excel sheet 

dataframe = pd.DataFrame.from_dict(song_feature_list)
dataframe = dataframe.transpose()
dataframe["Listened_times"]= ""

dic_counted = {}
n = 0
def ms_converter(x): #used to get 60% of a songs duration
    #art = sp.track(x)
    duration = dataframe.loc[x]["duration_ms"]  #isolating a row containing the particular song which was iterated through uniquevalues
    #duration = int(ms_df["duration_ms"]) #extracting the duration value for the islolated row
    sixty_percent = (duration*0.6) 
    return int(sixty_percent)
for x in Top100_uri:
    
    hr= df.loc[(df['spotify_track_uri'] == x) & (df["ms_played"] > (ms_converter(x)))]  #creating/isolating all the tracks listened having the same uri and duration listened more than 60%
    if hr["spotify_track_uri"].count() != 0:   #checking if the track was never heard 
        dic_counted[x] = hr["spotify_track_uri"].count()




result_dic ={}
u = 1
for i in dic_counted.keys():
    print("at this point")
    dataframe.loc[i,"Listened_times"]= dic_counted[i]
    #print("{}. you've listened>> {} <by> {}> {} times".format(u,dataframe.loc[i]["Track_name"],dataframe.loc[i]["Artist"],sorted_d[i]))
    u+=1
    #print(i)
    #print(sorted_d[i])

with pd.ExcelWriter('Spotify-data-analysis.xlsx') as writer:
    df.to_excel(writer, index = False, sheet_name="Sheet1")   #adding to sheet1 in the workbook
    dataframe.to_excel(writer, sheet_name='Sheet2', index=False)
