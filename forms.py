"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField(
        "Playlist Name",
        validators=[InputRequired()]
    )
    
    description = TextAreaField(
        "Description",
        validators=[Optional(), Length(min=5, max=140)]
    )


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField(
        "Title",
        validators=[InputRequired()]
    )
    
    artist = StringField(
        "Artist",
        validators=[InputRequired()]
    )


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
