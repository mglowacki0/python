from src.database_manager import DatabaseManager
from src.models import Author, Book

class AuthorRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def add_author(self, author: Author):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO authors (first_name, last_name, birth_year, nationality) VALUES (?, ?, ?, ?)",
                (author.first_name, author.last_name, author.birth_year, author.nationality)
            )
            conn.commit()

    def get_all_authors(self):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM authors")
            return cur.fetchall()

    def find_by_last_name(self, last_name):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM authors WHERE last_name LIKE ?", ('%' + last_name + '%',))
            return cur.fetchall()

    def update_author(self, author_id, first_name, last_name, birth_year, nationality):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE authors SET first_name=?, last_name=?, birth_year=?, nationality=? WHERE id=?",
                (first_name, last_name, birth_year, nationality, author_id)
            )
            conn.commit()

    def delete_author(self, author_id):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM books WHERE author_id=?", (author_id,))
            if cur.fetchone()[0] == 0:
                cur.execute("DELETE FROM authors WHERE id=?", (author_id,))
                conn.commit()
                return True
            return False

class BookRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def add_book(self, book: Book):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO books (title, author_id, publication_year, genre, pages, description) VALUES (?, ?, ?, ?, ?, ?)",
                (book.title, book.author_id, book.publication_year, book.genre, book.pages, book.description)
            )
            conn.commit()

    def get_all_books(self):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT books.*, authors.first_name || ' ' || authors.last_name 
                FROM books 
                JOIN authors ON books.author_id = authors.id
            """)
            return cur.fetchall()

    def search_books(self, keyword):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT books.*, authors.first_name || ' ' || authors.last_name 
                FROM books 
                JOIN authors ON books.author_id = authors.id
                WHERE title LIKE ? OR authors.last_name LIKE ? OR publication_year = ?
            """, ('%' + keyword + '%', '%' + keyword + '%', keyword if keyword.isdigit() else -1))
            return cur.fetchall()

    def update_book(self, book_id, title, author_id, publication_year, genre, pages, description):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE books 
                SET title=?, author_id=?, publication_year=?, genre=?, pages=?, description=?
                WHERE id=?
            """, (title, author_id, publication_year, genre, pages, description, book_id))
            conn.commit()

    def delete_book(self, book_id):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM books WHERE id=?", (book_id,))
            conn.commit()

    def get_books_by_author(self, author_id):
        with self.db.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE author_id=?", (author_id,))
            return cur.fetchall()

    def statistics(self):
        with self.db.connect() as conn:
            cur = conn.cursor()
            stats = {}
            cur.execute("SELECT COUNT(*) FROM books")
            stats["book_count"] = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM authors")
            stats["author_count"] = cur.fetchone()[0]
            cur.execute("SELECT title, MIN(publication_year) FROM books")
            stats["oldest"] = cur.fetchone()
            cur.execute("SELECT title, MAX(publication_year) FROM books")
            stats["newest"] = cur.fetchone()
            cur.execute("""
                SELECT authors.first_name || ' ' || authors.last_name, COUNT(books.id) AS book_total 
                FROM books 
                JOIN authors ON books.author_id = authors.id 
                GROUP BY author_id ORDER BY book_total DESC LIMIT 1
            """)
            stats["most_books"] = cur.fetchone()
            return stats
