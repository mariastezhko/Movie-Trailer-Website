class Movie():
    """ This class is used to store movie related information.

    Arguments:
        movie_title: A title of the movie
        poster_image: A link to the poster image
        trailer_youtube: A link to the movie trailer
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Inits data assosiated with a movie."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
