# Fresh Tomatoes

A `python` script that generates a web page from the provided set of movies (defined in `movie.py`).

### Usage

Prepare a list of objects of type `Movie` and pass them in `open_movie_pages()` to generate `fresh_tomatoes.html`.

### Creating Movie object

Make a call for the constructor as  
```python
new_movie = movie.Movie('title', 'url_to_poster', 'url_to_youtube_trailer', 'details')
```

If no description is available, pass `details` as `''` (empty `str`).