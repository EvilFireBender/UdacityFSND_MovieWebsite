import media
import fresh_tomatoes

# creating a Movie object for Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# creating a Movie object for Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# creating a Movie object for The Dark Knight Rises
tdkr = media.Movie("The Dark Knight Rises",
                   "Batman returns to save Gotham from Bane",
                   "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=g8evyE9TuYk")

# creating a Movie object for Hugo
hugo = media.Movie("Hugo",
                   "an orphan is wrapped up in a mystery involving his late father and an automaton",  # noqa
                   "https://upload.wikimedia.org/wikipedia/en/7/73/Hugo_Poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=Hv3obL9HqyY")

# creating a Movie object for Fight Club
fight_club = media.Movie("Fight Club",
                         "An insomniac office worker joins an underground fight club",  # noqa
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=BdJKm16Co6M")

# creating a Movie object for The Matrix
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns about the true nature of his reality",  # noqa
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# adding all Movie objects in one list
movies = [toy_story, avatar, tdkr, hugo, fight_club, the_matrix]

# Opening the web page with the above list of movies
fresh_tomatoes.open_movies_page(movies)
