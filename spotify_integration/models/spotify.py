from odoo import api, fields, models
import requests, base64

CLIENT_ID = "c53cb5f354854445a8fbe49703e906bd"
CLIENT_SECRET = "b85fc7a1af4f4683bbc64c452396ae3c"


class Spotify(models.Model):
    _name = 'spotify'
    _description = 'Spotify'

    name = fields.Char('Name')
    musical_genre_ids = fields.Many2many('spotify.musical.genres', 'spotify_id', string='Musical Genres')
    line_ids = fields.One2many('spotify.line', 'spotify_id')

    def get_data(self):
        data = {
            'grant_type': 'client_credentials'
        }
        return data

    def get_headers(self):
        client_credential = f"{CLIENT_ID}:{CLIENT_SECRET}"

        client_b64 = base64.b64encode(client_credential.encode())

        headers = {
            'Authorization': f"Basic {client_b64.decode()}"
        }
        return headers

    def _get_token(self):
        token_url = "https://accounts.spotify.com/api/token"
        data = self.get_data()
        headers = self.get_headers()

        response = requests.post(url=token_url, headers=headers, data=data)
        data = response.json()
        token = data['access_token']
        return token

    def get_resource_header(self):
        access_token = self._get_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers

    def get_recommend_songs(self, genres=False):
        endpoint = f"https://api.spotify.com/v1/recommendations?limit=1&market=ES&seed_genres={genres}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    @api.model
    def create(self, values):

        spotify_id = super(Spotify, self).create(values)
        for line in spotify_id.musical_genre_ids:
            genres = f"{line.name.lower()}"

            songs = self.get_recommend_songs(genres=genres)

            for song in songs['tracks']:
                name = song['name']
                url = song.get('external_urls').get('spotify')

                vals = {
                    'spotify_id': spotify_id.id,
                    'song_name': name,
                    'song_url': url,
                }

                spotify_id.line_ids.create(vals)

        return spotify_id


class SpotifyMusicalGenres(models.Model):
    _name = 'spotify.musical.genres'
    _description = 'Spotify Musical Genres'

    spotify_id = fields.Many2one('spotify')
    name = fields.Char('Musical Genre')


class SpotifyMusicLines(models.Model):
    _name = 'spotify.line'
    _description = 'Spotify Music Lines'

    spotify_id = fields.Many2one('spotify')
    song_name = fields.Char('Song Name')
    song_url = fields.Char('Url')
