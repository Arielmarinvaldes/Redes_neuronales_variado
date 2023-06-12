import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurar las credenciales de la API de Spotify
client_id = 'TU_CLIENT_ID'
client_secret = 'TU_CLIENT_SECRET'
redirect_uri = 'TU_REDIRECT_URI'

# Inicializar el objeto de autenticación de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-modify-playback-state'))

# Buscar una canción específica
song_name = 'Nombre de la canción'
artist_name = 'Nombre del artista'
results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track', limit=1)

if results['tracks']['items']:
    # Obtener el URI de la canción encontrada
    track_uri = results['tracks']['items'][0]['uri']
    
    # Reproducir la canción en Spotify
    sp.start_playback(uris=[track_uri])
    print(f'Reproduciendo la canción: {song_name} - {artist_name}')
else:
    print('No se encontró la canción en Spotify')
