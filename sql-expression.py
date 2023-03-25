from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaDate
)

# connect our Python file to Chinook DB
db = create_engine("postgresql:///chinook")

meta = MetaDate(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create variable for "Artist" Table
album_table = Table(
    
)

# Making the connection
with db.connect() as connection:
