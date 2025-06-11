from src.database_manager import DatabaseManager
from src.repositories import AuthorRepository, BookRepository
from src.ui import *

def main():
    db = DatabaseManager()
    author_repo = AuthorRepository(db)
    book_repo = BookRepository(db)

    while True:
        print_menu()
        choice = input("Wybierz opcję: ")
        if choice == "1":
            author_repo.add_author(input_author())
        elif choice == "2":
            authors = author_repo.get_all_authors()
            if not authors:
                print("Brak autorów w bazie.")
            else:
                for a in authors:
                    print(f"ID: {a[0]}, Imię: {a[1]}, Nazwisko: {a[2]}, Rok urodzenia: {a[3]}, Narodowość: {a[4]}")
        elif choice == "3":
            last_name = input("Nazwisko: ")
            authors = author_repo.find_by_last_name(last_name)
            if not authors:
                print("Nie znaleziono autora o takim nazwisku.")
            else:
                for a in authors:
                    print(f"ID: {a[0]}, Imię: {a[1]}, Nazwisko: {a[2]}, Rok urodzenia: {a[3]}, Narodowość: {a[4]}")
        elif choice == "4":
            id = int(input("ID autora: "))
            author_repo.update_author(id, *input_author().__dict__.values())
        elif choice == "5":
            id = int(input("ID autora do usunięcia: "))
            if author_repo.delete_author(id):
                print("Usunięto autora.")
            else:
                print("Nie można usunąć - autor ma przypisane książki.")
        elif choice == "6":
            book_repo.add_book(input_book())
        elif choice == "7":
            books = book_repo.get_all_books()
            if not books:
                print("Brak książek w bibliotece.")
            else:
                for b in books:
                    # b: (id, title, author_id, publication_year, genre, pages, description, "Imię Nazwisko")
                    print(f"ID: {b[0]}, Tytuł: {b[1]}, Autor: {b[7]}, Rok wydania: {b[3]}, Gatunek: {b[4]}, Strony: {b[5]}, Opis: {b[6]}")
        elif choice == "8":
            keyword = input("Szukaj: ")
            books = book_repo.search_books(keyword)
            if not books:
                print("Nie znaleziono książek.")
            else:
                for b in books:
                    print(f"ID: {b[0]}, Tytuł: {b[1]}, Autor: {b[7]}, Rok wydania: {b[3]}, Gatunek: {b[4]}, Strony: {b[5]}, Opis: {b[6]}")
        elif choice == "9":
            id = int(input("ID książki: "))
            book_repo.update_book(id, *input_book().__dict__.values())
        elif choice == "10":
            id = int(input("ID książki do usunięcia: "))
            book_repo.delete_book(id)
        elif choice == "11":
            author_id = int(input("ID autora: "))
            books = book_repo.get_books_by_author(author_id)
            if not books:
                print("Autor nie ma książek.")
            else:
                for b in books:
                    print(f"ID: {b[0]}, Tytuł: {b[1]}, Rok wydania: {b[3]}, Gatunek: {b[4]}, Strony: {b[5]}, Opis: {b[6]}")
        elif choice == "12":
            stats = book_repo.statistics()
            print(f"Liczba książek: {stats['book_count']}")
            print(f"Liczba autorów: {stats['author_count']}")
            print(f"Najstarsza książka: {stats['oldest']}")
            print(f"Najnowsza książka: {stats['newest']}")
            print(f"Autor z największą liczbą książek: {stats['most_books']}")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
