from dataclasses import dataclass

@dataclass
class Author:
    id: int
    first_name: str
    last_name: str
    birth_year: int
    nationality: str

@dataclass
class Book:
    id: int
    title: str
    author_id: int
    publication_year: int
    genre: str
    pages: int
    description: str
