# Personal Library Manager (Terminal-based)

import os

def load_library():
    library = []
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            for line in file:
                title, author, year, genre, read = line.strip().split(" | ")
                library.append({"Title": title, "Author": author, "Year": year, "Genre": genre, "Read": read == "True"})
    return library

def save_library(library):
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['Title']} | {book['Author']} | {book['Year']} | {book['Genre']} | {book['Read']}\n")

def display_menu():
    print("\n📚 Personal Library Manager")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search Books")
    print("4. Display All Books")
    print("5. Library Statistics")
    print("6. Exit")

def add_book(library):
    while True:
        title = input("Enter title: ").strip()
        if not title:
            print("Title cannot be empty. Please enter a valid title.")
            continue
        
        author = input("Enter author: ").strip()
        if not author:
            print("Author cannot be empty. Please enter a valid author.")
            continue
        
        year = input("Enter publication year: ").strip()
        if not year.isdigit():
            print("Please enter a valid numerical year.")
            continue
        
        genre = input("Enter genre: ").strip()
        if not genre:
            print("Genre cannot be empty. Please enter a valid genre.")
            continue
        
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
        if read_status not in ["yes", "no"]:
            print("Please enter 'yes' or 'no' for read status.")
            continue

        read_status = read_status == "yes"  # Convert to boolean (True if "yes", False if "no")

        break  # Exit loop once all inputs are valid

    if any(book["Title"].lower() == title.lower() for book in library):
        print("A book with this title already exists!")
        return
    
    library.append({"Title": title, "Author": author, "Year": year, "Genre": genre, "Read": read_status})
    save_library(library)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    library[:] = [book for book in library if book["Title"].lower() != title.lower()]
    save_library(library)
    print(f"Book '{title}' removed!")

def search_books(library):
    query = input("Enter title or author to search: ").lower()
    results = [book for book in library if query in book["Title"].lower() or query in book["Author"].lower()]
    if results:
        for book in results:
            print(f"- {book['Title']} by {book['Author']} ({book['Year']}) - {'Read' if book['Read'] else 'Unread'}")
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("Library is empty.")
        return
    for book in library:
        print(f"- {book['Title']} by {book['Author']} ({book['Year']}) - {'Read' if book['Read'] else 'Unread'}")
    
    mark_read = input("Would you like to mark any book as read? (yes/no): ").strip().lower()
    if mark_read == "yes":
        title = input("Enter the title of the book to mark as read: ")
        for book in library:
            if book["Title"].lower() == title.lower():
                book["Read"] = True
                save_library(library)
                print(f"Book '{title}' marked as read!")
                return
        print("Book not found.")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["Read"])
    if total_books > 0:
        print(f"Total Books: {total_books}")
        print(f"Books Read: {read_books} ({(read_books / total_books) * 100:.2f}%)")
    else:
        print("Library is empty.")

def main():
    library = load_library()
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()