
# Spotify-data-analysis
Analyzing the JSON data provided by Spotify

## Features

- Converts the JSON files to a readable Excel file with analyzed data
- Get your top 100 tracks with audio_features the spotify api provides


## Getting Spotify data
you can get your Spotify data from Privacy Settings in [Spotify accounts](https://www.spotify.com/us/account/privacy/)

Select Extended Streaming History and Request data, you'll get your data in around a month
## Creating a Spotify Developer App
Head to the Spotify [developer website]( https://developer.spotify.com/dashboard)

Login and create a new app

- Give it a name 

- Set Redirect to http://localhost:7777/callback

- You now should be able to get your client id and secret from settings

  ![image](https://github.com/Izor12/Spotify-data-analysis/assets/77780623/36f76e15-6539-44f7-bb28-6d1083997eb7)

  ![image](https://github.com/Izor12/Spotify-data-analysis/assets/77780623/844ef4c9-63c0-4ecc-a8f5-8a92d9357644)




## Installing Required Packages

To install Spotipy wiht pip

```bash
  pip install Spotipy
```




To install pandas

```bash
  pip install pandas
```


## Using the Code

- After extracting the data received from Spotify, get the folder path containing the JSON files and paste it into the folder_path variable.
![image](https://github.com/Izor12/Spotify-data-analysis/assets/77780623/e8034deb-5823-4d8d-9e93-558d3dd9d580)

- Paste the client id and client secret from above-created developer app
![image](https://github.com/Izor12/Spotify-data-analysis/assets/77780623/d1fa7a9a-cb56-4368-b8e7-0b39ad3a3544)

- Running the code should output a Excel file called "Spotify-data-analysis.xlsx" containing the raw JSON data and track data with audio features

# Example Excel file
![Sheet1](https://github.com/Izor12/Spotify-data-analysis/assets/77780623/d9a71d4d-d740-4e3b-b398-507135b7f641)
![Sheet2](https://github.com/Izor12/Spotify-data-analysis/assets/77780623/2772ac32-63fa-44cc-b220-0f0baaeec470)


