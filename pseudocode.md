# DJANGO JAMS #

## About ##
    in this project we are utilizing DJANGO REST with our database to create a music application layout similar to spotify or apple music

## MoSCoW ##

**Must Have**

-Django Framework

-Django Rest Framework

-Relationship Diagram to show database structure

-PostgreSQL DB

-Foreign Keys

-API capabilities to display JSON

-Models for Songs, Artists, Albums, etc


**Should Have**

-CRUD capabilities to manipulate the database

**Could Have**

-Extra Fields in the tables such as Release dates, song lengths etc

**Won't Have**

-The ability to listen to music

-Literally any music at all

## Database Structure ##

Tables:
    Songs:
    - id
    - title

    Artists
    -id
    -name

    Albums
    -id
    -label

    Genres
    -id
    -label

    Song_Genres
    -id
    -song_id
    -genre_id

    Album_Songs
    -id
    -song_id
    genre_id

    Song_Artists
    -id
    -song_id
    artist_id

    Users
    -id
    -email
    -username

    User_Playlist
    -id
    -user_id
    -name

    User_Playlist_Songs
    -id
    -user_playlist_id
    -song_id
    -order