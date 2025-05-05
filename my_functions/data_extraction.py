import pandas as pd
import lyricsgenius

# Functions used and documentation

## Data extraction


# Refined version of get_lyrics_with_api
def get_lyrics_with_api(access_token, artist, max_songs=1):
    """
    Retrieve song lyrics and metadata for a given artist using the Genius API.

    Parameters
    ----------
    access_token : str
        The Genius API access token for authentication.
    artist : str
        The name of the artist whose songs are to be retrieved.
    max_songs : int, optional
        The maximum number of songs to retrieve (default is 1).

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the following columns:
        - 'artist': The name of the artist.
        - 'title': The title of the song.
        - 'release_date': The release date of the song.
        - 'pageviews': The number of page views for the song on Genius.
        - 'album': The name of the album the song belongs to.
        - 'lyrics': The lyrics of the song.

    Notes
    -----
    - If the artist is not found, an empty DataFrame is returned.
    - If a song's metadata is missing, default values are used:
        - 'Unknown' for artist names.
        - 'Untitled' for song titles.
        - 'No date' for release dates.
        - 0 for page views.
        - 'No album' for album names.
        - 'No lyrics available' for lyrics.
    """

    genius = lyricsgenius.Genius(
        access_token, verbose=False, remove_section_headers=True, timeout=15
    )

    artist = genius.search_artist(artist, max_songs=max_songs)

    # Convert songs to dicts. Returns an empty list if artist is None, that's equivalent to False
    result = [song.to_dict() for song in artist.songs] if artist else []

    data = []
    # Slicing never creates 'empty' spaces, so the len of result remains
    # For instance: len(result) = 3 and max_songs = 4 -> result[:4] will have 3 elements
    for song in result[:max_songs]:
        data.append(
            {
                "artist": (song.get("primary_artist", {}) or {}).get("name", "Unknown"),
                "title": song.get("title", "Untitled"),
                "release_date": song.get("release_date", "No date"),
                # Nested safe access if the first key contains a None.
                "pageviews": (song.get("stats", {}) or {}).get("pageviews", 0),
                "album": (song.get("album", {}) or {}).get("name", "No album"),
                "lyrics": song.get("lyrics", "No lyrics available"),
            }
        )

    return pd.DataFrame(data)
