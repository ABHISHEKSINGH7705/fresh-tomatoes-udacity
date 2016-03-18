import movie
from fresh_tomatoes import open_movies_page

if __name__ == "__main__":
    # Declaring movies
    raw_movies_data = [
        (
            'Deadpool',

            'http://s3.foxfilm.com/foxmovies/production/films/103/images/poste'
            'rs/464-film-page-large.jpg',

            'https://www.youtube.com/watch?v=Xithigfg7dA',

            'Deadpool is a 2016 American superhero film based on the Marvel Co'
            'mics character of the same name. It is the eighth installment of '
            'the X-Men film series, and is directed by Tim Miller. Written by '
            'Rhett Reese and Paul Wernick, the film stars Ryan Reynolds, Moren'
            'a Baccarin, Ed Skrein, T. J. Miller, Gina Carano, Brianna Hildebr'
            'and, and Stefan Kapičić. In Deadpool, Wade Wilson hunts the man w'
            'ho gave him an accelerated healing factor, but also a scarred phy'
            'sical appearance.'
        ),
        (
            'Dark Circles',

            'http://gdj.gdj.netdna-cdn.com/wp-content/uploads/2012/03/movies-p'
            'oster-50.jpg',

            'https://www.youtube.com/watch?v=K0HVeqjqs9E',

            'Alex (Johnathon Schaech) and Penny (Pell James) have decided to u'
            'proot themselves from their hectic city lives and move out to the'
            ' country, believing that it will be better for their baby. The mo'
            've is not without hesitation, as Penny is concerned that she will'
            ' not be a fit mother for her baby while Alex can\'t help but wond'
            'er if it would have been better to remain in the city with his ba'
            'ndmates. Soon after they move, strange things begin to occur that'
            ' cause them to wonder if the move was really the best idea.'
        ),
        (
            'Avengers',

            'http://interhost.hu/stuff/pics/posters/Avengers.jpg',

            'https://www.youtube.com/watch?v=eOrNdBpGMv8',

            'Marvel\'s The Avengers[4] (classified under the name Marvel Aveng'
            'ers Assemble in the United Kingdom and Ireland),[1][5] or simply '
            'The Avengers, is a 2012 American superhero film based on the Marv'
            'el Comics superhero team of the same name, produced by Marvel Stu'
            'dios and distributed by Walt Disney Studios Motion Pictures.1 It '
            'is the sixth film in the Marvel Cinematic Universe. The film was '
            'written and directed by Joss Whedon and features an ensemble cast'
            ' that includes Robert Downey Jr., Chris Evans, Mark Ruffalo, Chri'
            's Hemsworth, Scarlett Johansson, Jeremy Renner, Tom Hiddleston, C'
            'lark Gregg, Cobie Smulders, Stellan Skarsgård, and Samuel L. Jack'
            'son. In the film, Nick Fury, director of the peacekeeping organiz'
            'ation S.H.I.E.L.D., recruits Iron Man, Captain America, the Hulk,'
            ' and Thor to form a team that must stop Thor\'s brother Loki from'
            ' subjugating Earth.'
        ),
        (
            'The Divergent Series : Allegiant',

            'http://hollywoodnewssource.com/wp-content/uploads/2016/02/shailen'
            'e-woodley-the-divergent-series-allegiant-posters_1.jpg',

            'https://www.youtube.com/watch?v=tE8LEPSTK6A',

            'After the earth-shattering revelations of Insurgent, Tris (Shaile'
            'ne Woodley) must escape with Four (Theo James) and go beyond the '
            'wall enclosing Chicago. For the first time ever, they will leave '
            'the only city and family they have ever known to find a peaceful '
            'solution for their embroiled city. Once outside, old discoveries '
            'are quickly rendered meaningless with the revelation of shocking '
            'new truths. Tris and Four must quickly decide who they can trust '
            'as a ruthless battle ignites beyond the walls of Chicago which th'
            'reatens all of humanity. To survive, Tris will be forced to make '
            'impossible choices about courage, allegiance, sacrifice.'
        )
    ]

    # Wrapping movies in a list
    movies = [
        movie.Movie(temp[0], temp[1], temp[2], temp[3])
        for temp in raw_movies_data
        ]

    # Calling to generate HTML page
    open_movies_page(movies)
