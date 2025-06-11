from src.models import Author, Book

def print_menu():
    print("\nMENU:")
    print("1. Dodaj autora")
    print("2. Lista autorów")
    print("3. Szukaj autora")
    print("4. Edytuj autora")
    print("5. Usuń autora")
    print("6. Dodaj książkę")
    print("7. Lista książek")
    print("8. Szukaj książki")
    print("9. Edytuj książkę")
    print("10. Usuń książkę")
    print("11. Książki autora")
    print("12. Statystyki")
    print("0. Wyjście")

def input_author():
    first_name = input("Imię: ")
    last_name = input("Nazwisko: ")

    while True:
        try:
            birth_year = int(input("Rok urodzenia: "))
            break
        except ValueError:
            print("Podaj poprawny rok (liczba całkowita).")

    nationality = input("Narodowość: ")

    return Author(
        id=0,
        first_name=first_name,
        last_name=last_name,
        birth_year=birth_year,
        nationality=nationality
    )

def input_book():
    title = input("Tytuł: ")

    while True:
        try:
            author_id = int(input("ID autora: "))
            break
        except ValueError:
            print("Podaj poprawny numer ID (liczba całkowita).")

    while True:
        try:
            publication_year = int(input("Rok wydania: "))
            break
        except ValueError:
            print("Podaj poprawny rok wydania (liczba całkowita).")

    genre = input("Gatunek: ")

    while True:
        try:
            pages = int(input("Liczba stron: "))
            break
        except ValueError:
            print("Podaj poprawną liczbę stron (liczba całkowita).")

    description = input("Opis: ")

    return Book(
        id=0,
        title=title,
        author_id=author_id,
        publication_year=publication_year,
        genre=genre,
        pages=pages,
        description=description
    )
