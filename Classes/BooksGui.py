
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
        self.listbox.bind('<<ListboxSelect>>', self.load_selected_book)  # when highlighted or clicked on it loads to the bottom text boxes

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

        # Create a Text widget for displaying messages
        self.message_text = tk.Text(self.root, height=2, wrap=tk.WORD)
        self.message_text.pack(pady=10)

        # Create a "Delete" button
        self.delete_button = tk.Button(self.root, text="Delete Book", command=self.delete_book)
        self.delete_button.pack(padx=5)

        # Create a "Save Catalog" button
        self.save_catalog_button = tk.Button(self.root, text="Save Catalog", command=self.save_catalog)
        self.save_catalog_button.pack(padx=5)

        # adding sort buttons and functions
        # Create and configure sorting buttons
        self.sort_title_button = tk.Button(self.root, text="Sort by Title", command=self.sort_by_title)
        self.sort_title_button.pack(side=tk.LEFT, padx=5)

        self.sort_genre_button = tk.Button(self.root, text="Sort by Genre", command=self.sort_by_genre)
        self.sort_genre_button.pack(side=tk.RIGHT, padx=5)

    # function that callss the save catalog
    def save_catalog(self):
        self.library.save_catalog()
        self.display_message("Catalog saved successfully.")

    def sort_by_title(self):
        self.library.sort_catalog_by_title()
        self.load_books()

    def sort_by_genre(self):
        self.library.sort_catalog_by_genre()
        self.load_books()

    def load_selected_book(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_book = self.listbox.get(selected_index[0])
            # Assuming the book title is the first part of the string in the listbox
            book_title = selected_book.split(" ")[0]
            book = self.library.catalog.get(book_title)
            if book:
                self.title_entry.delete(0, tk.END)
                self.genre_entry.delete(0, tk.END)
                self.volumes_entry.delete(0, tk.END)

                self.title_entry.insert(0, book.get_title())
                self.genre_entry.insert(0, book.get_genre())
                self.volumes_entry.insert(0, book.get_volumes())

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
                self.display_message("please enter values for title genre and volumes")
        except ValueError:
            self.display_message("volumes must be a valid integer")

    def display_message(self, message):
        # Clear previous messages
        self.message_text.delete(1.0, tk.END)
        # Display the new message
        self.message_text.insert(tk.END, message)

    # function to delete a book from catalogue
    def delete_book(self):
        title_to_delete = self.title_entry.get()

        if title_to_delete:
            if title_to_delete in self.library.catalog:
                del self.library.catalog[title_to_delete]
                self.load_books()
                self.clear_entry_fields()
                self.display_message(f"Book '{title_to_delete}' deleted.")
            else:
                self.display_message(f"Error: Book '{title_to_delete}' not found in the catalog.")
        else:
            self.display_message("Error: Please enter the title to delete.")

    def clear_entry_fields(self):
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.volumes_entry.delete(0, tk.END)
