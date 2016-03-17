class Movie:
    '''
    This class stores all information about a movie.
    '''
    title = ''
    poster_image_url = ''
    trailer_youtube_url = ''
    details = 'No Details Available'

    # Constructors
    def __init__(self, title, poster_image_url, trailer_youtube_url, details):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        if len(details) > 0:
            self.details = details