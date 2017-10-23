'''This code is based on that from
Programming Foundations with Python course'''

import fresh_tomatoes
import media

# Cteate objects of the class Movie
la_la_land = media.Movie("La La Land",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # noqa
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

gladiator = media.Movie("Gladiator",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=owK1qxDselE")

spider_man = media.Movie("Spider-Man",
                         "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=O7zvehDxttM")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

a_beautiful_mind = media.Movie("A Beautiful Mind",
                               "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=YWwAOutgWBQ")

wall_e = media.Movie("WALL-E",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",  # noqa
                     "https://www.youtube.com/watch?v=alIq_wG9FNk")

# Define movies variable as a list of objects of the class Movie
movies = [la_la_land, gladiator, spider_man,
          inception, a_beautiful_mind, wall_e]

# Generate an HTML file, producing a website to showcase movies
fresh_tomatoes.open_movies_page(movies)
