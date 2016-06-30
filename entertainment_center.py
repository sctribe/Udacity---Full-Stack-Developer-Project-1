import media
import fresh_tomatoes

#media creates the movie class and fresh_tomatoes creates the html file for the website

#create 6 objects of the class "Movie". Each object has a title, description,
#poster, trailer, and rating

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4",
                        "G")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "PG-13")

warrior = media.Movie("Warrior",
                      "Two brothers work on their relationship in the octagon.",
                      "https://upload.wikimedia.org/wikipedia/en/e/e3/Warrior_Poster.jpg",
                      "https://www.youtube.com/watch?v=kY7HcUACs58",
                      "PG-13")

ex_machina = media.Movie("Ex-Machina",
                         "A young programmer performs the Turing test.",
                         "http://i.imgur.com/4loI4Qy.jpg",
                         "https://www.youtube.com/watch?v=XYGzRB4Pnq8",
                         "R")

chappie = media.Movie("Chappie",
                      "A robot learns to love.",
                      "http://www.impawards.com/2015/posters/chappie_ver4.jpg",
                      "https://www.youtube.com/watch?v=HhNshgSYF_M",
                      "R")

kingsman = media.Movie("Kingsman",
                       "A young boy joins a secret organization of spies.",
                       "http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-N4gVBmixzAXvGfZ",
                       "https://www.youtube.com/watch?v=xkX8jKeKUEA",
                       "R")


#create an array of the Movie objects
movies = [toy_story, avatar, warrior, ex_machina, chappie, kingsman]

#run freash_tomatoes file to create html file
fresh_tomatoes.open_movies_page(movies)



          
