from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    playlist = Playlist.query.get_or_404(playlist_id)
    songs = Song.query.all()
    return render_template("playlist.html", playlist=playlist, songs=songs)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_playlist = Playlist(**data)
        db.session.add(new_playlist)
        db.session.commit()
        flash(f"{new_playlist.name} has been added!")
        return redirect(url_for('show_all_playlists'))
    
    else: 
        return render_template("new_playlist.html", form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    song = Song.query.get_or_404(song_id)
    playlists = Playlist.query.all()
    return render_template("song.html", song=song, playlists=playlists)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    form = SongForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_song = Song(**data)
        db.session.add(new_song)
        db.session.commit()
        flash(f"{new_song.title} has been added!")
        
        return redirect(url_for('show_all_songs'))
    
    else: 
        return render_template("new_song.html", form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a song to a playlist."""
    
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Populate the dropdown menu with songs not already on this playlist
    form.song.choices = [(song.id, song.title) for song in Song.query.filter(~Song.playlists.any(id=playlist_id)).all()]

    if form.validate_on_submit():
        song_id = form.song.data
        playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=song_id)
        db.session.add(playlist_song)
        db.session.commit()
        flash(f"Song added to {playlist.name}!")
        return redirect(url_for('show_playlist', playlist_id=playlist_id))

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)

##############################################################################
# DELETE routes

@app.route("/songs/<int:song_id>/delete", methods=["POST"])
def delete_song(song_id):
    """Delete a song."""

    song = Song.query.get_or_404(song_id)

    db.session.delete(song)
    db.session.commit()

    flash(f"The song '{song.title}' has been deleted.", "success")
    
    return redirect(url_for("show_all_songs"))

@app.route("/playlists/<int:playlist_id>/delete", methods=["POST"])
def delete_playlist(playlist_id):
    """Delete a playlist."""

    playlist = Playlist.query.get_or_404(playlist_id)

    db.session.delete(playlist)
    db.session.commit()

    flash(f"The playlist '{playlist.name}' has been deleted.", "success")
    
    return redirect(url_for("show_all_playlists"))