# Playlist App

## Overview
The Playlist App is a Flask-based web application that allows users to manage playlists and songs. Users can create playlists, add songs to playlists, view all playlists, view details of individual playlists, view all songs, and view details of individual songs.

## Features
- **Playlist Management**: Users can create new playlists with a name and optional description.
- **Song Management**: Users can add new songs with a title and artist.
- **Association**: Songs can be associated with playlists, allowing users to organize their music into different playlists.
- **Viewing**: Users can view all playlists, view details of a specific playlist (including the songs it contains), view all songs, and view details of a specific song.
- **Deletion**: Users can delete playlists and songs.

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/playlist-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd playlist-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    createdb playlist-app
    ```

5. Run the application:

    ```bash
    flask run
    ```

6. Access the application in your web browser at `http://localhost:5000`.

## Usage
- Navigate to `http://localhost:5000/playlists` to view all playlists.
- Click on a playlist to view its details, including the songs it contains.
- Navigate to `http://localhost:5000/songs` to view all songs.
- Click on a song to view its details.
- To add a new playlist, click on "Add a playlist" and fill out the form.
- To add a new song, click on "Add a song" and fill out the form.
- To add a song to a playlist, go to the playlist's detail page and click "Add Song To Playlist".
- To delete a playlist or song, navigate to its detail page and click "Delete".

## Contributing
Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests to help improve this application.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.