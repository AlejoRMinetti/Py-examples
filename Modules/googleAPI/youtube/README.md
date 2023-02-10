# YouTube download list
using an API, you will need to use the YouTube Data API. Here are the general steps you will need to follow:

## Create a project in the Google Developers Console and enable the YouTube Data API.

- Go to the Google Developers Console (https://console.developers.google.com/) and sign in with your Google account.

- Click on the project drop-down and create a new project.

- Give your project a name, and click "Create."

- Click on the "Enable APIs and Services" button, and search for "YouTube Data API."

- Click on the "YouTube Data API" and then click on the "Enable" button.

- In the sidebar, go to "Credentials" and click on "Create credentials" then select "API Key".

- A pop-up window will appear with your API key. You can use this key to authenticate your requests to the YouTube Data API.

- You can also restrict the key so it only works for specific IPs, or for your own application and prevent other people from using it.


## Generate an API key for your project.

Use the API key to authenticate your requests to the YouTube Data API.

Use the API's "playlistItems.list" method to retrieve a list of all the videos in your download list.

Iterate through the list of videos and use the "playlistItems.delete" method to delete the videos that have been watched.