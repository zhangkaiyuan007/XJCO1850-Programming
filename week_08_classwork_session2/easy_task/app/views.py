from flask import flash, redirect, render_template, request, url_for
from app import app
import os, csv


# To store your collection, you can simply store the ids in a global list
# you can use collection anywhere in the code now
global collection
collection = []


def read_movies(header=False):
    ''' Reads and returns the list of movies - returns without the header row by default, or use read_moves(True) if you want to include the header e.g. for writing to file '''
    movies = []
    with  open(os.path.join(app.root_path, 'static', 'imbd_movies.csv')) as f:
        prod_reader = csv.reader(f)
        for each in prod_reader:
            movies.append(each)
    # if you need to check what index is which, you can print here!
    #print(movies[0:1])
    # this will appear in the terminal, not on the website.

    return movies if header else movies[1:]

@app.route('/')
def index():
    ''' The homepage '''
    return render_template("home.html", title="Movie Database - Home")

@app.route('/all_movies')
def all_movies():
    ''' Task 1 - you should edit this to render the correct template. '''
    movies = read_movies()
    return render_template("view_all.html", title="Movie Database - All Movies", movies=movies)

@app.route('/my_collection')
def my_collection():
    movies = read_movies()
    collected = []
    for movie in movies:
        try:
            movie_id = int(movie[0])
        except (ValueError, IndexError):
            continue
        if movie_id in collection:
            collected.append(movie)
    return render_template("collection.html", title="Movie Database - My Collection", movies=collected)

@app.route("/movie/<int:id>")
def movie(id):
    movies = read_movies()
    selected = None
    for movie in movies:
        try:
            movie_id = int(movie[0])
        except (ValueError, IndexError):
            continue
        if movie_id == id:
            selected = movie
            break
    if not selected:
        return f"Movie id {id} not found."
    in_collection = id in collection
    return render_template("movie.html", title=f"Movie Database - {selected[1]}", movie=selected, in_collection=in_collection)


@app.route('/add/<int:id>')
def add(id):
    if id not in collection:
        collection.append(id)
    return redirect(url_for("movie", id=id))
