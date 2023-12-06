
import tkinter as tk
from Classes.Books import Book
from Classes.LibraryCatalog import LibraryCatalog

class BookGUI:
    def __init__(self, root,library):
        self.root = root
        self.root.title("Book Catalog")

        self.library=library

        # Create and configure GUI components
        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)  # adjust size when  window is resized

        self.load_books_button = tk.Button(self.root, text="Load Books", command=self.load_books)
        self.load_books_button.pack(pady=10)

        self.add_book_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_book_button.pack(pady=10)

        # Entry buttons and labels for adding book information
        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self.root, width=30)
        self.title_entry.insert(0, "")
        self.title_entry.pack()

        self.genre_label = tk.Label(self.root, text="Genre:")
        self.genre_label.pack()

        self.genre_entry = tk.Entry(self.root, width=30)
        self.genre_entry.insert(0, "")
        self.genre_entry.pack()

        self.volumes_label = tk.Label(self.root, text="Volumes:")
        self.volumes_label.pack()

        self.volumes_entry = tk.Entry(self.root, width=30)
        self.volumes_entry.insert(0, "")
        self.volumes_entry.pack()

        # adding sort buttons and functions
        # Create and configure sorting buttons
        self.sort_title_button = tk.Button(self.root, text="Sort by Title", command=self.sort_by_title)
        self.sort_title_button.pack(side=tk.LEFT, padx=5)

        self.sort_genre_button = tk.Button(self.root, text="Sort by Genre", command=self.sort_by_genre)
        self.sort_genre_button.pack(side=tk.LEFT, padx=5)

    def sort_by_title(self):
        self.library.sort_catalog_by_title()
        self.load_books()

    def sort_by_genre(self):
        self.library.sort_catalog_by_genre()
        self.load_books()

    def load_books(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Load books into the listbox
        for book in self.library.catalog.values():
            self.listbox.insert(tk.END, book.get_info())

    def add_book(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        volumes = self.volumes_entry.get()
        try:
            if title and genre and volumes:
                new_book = Book(title, genre, volumes)
                self.library.add_book_to_catalog(new_book)
                self.load_books()
                self.clear_entry_fields()
            else:
                print("please enter values for title genre and volumes")
        except ValueError:
            print("volumes must be a valid integer")

    def clear_entry_fields(self):
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.volumes_entry.delete(0, tk.END)
