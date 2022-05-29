import requests
import shutil # - - This module helps to transfer information from 1 file to another 
from bs4 import BeautifulSoup # - - We could honestly do this without soup

## TODO: hacerlo andar para Platzi con login y descargar los videos

# download video from url
def download_video(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=VTt9YJgL6B8'
    download_video(url, 'video.mp4')
    # NOTE no anda, baja el video pero no se puede visualizar    


