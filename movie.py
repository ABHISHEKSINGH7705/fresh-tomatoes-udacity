class Movie:
    '''
    This class is a data structure that
    stores all information about a movie.

    Attributes:
    title                   Title of movie
    poster_image_url        URL of poster (box art)
    trailer_youtube_url     URL of trailer of the movie on YouTube
    '''

    title = ''
    poster_image_url = ''
    trailer_youtube_url = ''
    details = 'No Details Available'

    # Constructor
    def __init__(self, title, poster_image_url, trailer_youtube_url, details):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        if len(details) > 0:
            self.details = details