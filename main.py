import tkinter as tk
from Classes.LibraryCatalog import LibraryCatalog, Book

class BookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Catalog")

        # Create an instance of the LibraryCatalog
        self.library = LibraryCatalog("ExcelFiles/books.xlsx")

        # Create and configure GUI components
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(padx=10, pady=10)

        self.load_books_button = tk.Button(self.root, text="Load Books", command=self.load_books)
        self.load_books_button.pack(pady=10)

        self.add_book_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_book_button.pack(pady=10)

        # Entry widgets and labels for adding book information
        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self.root, width=30)
        self.title_entry.insert(0, "Title")
        self.title_entry.pack()

        self.genre_label = tk.Label(self.root, text="Genre:")
        self.genre_label.pack()

        self.genre_entry = tk.Entry(self.root, width=30)
        self.genre_entry.insert(0, "Genre")
        self.genre_entry.pack()

        self.volumes_label = tk.Label(self.root, text="Volumes:")
        self.volumes_label.pack()

        self.volumes_entry = tk.Entry(self.root, width=30)
        self.volumes_entry.insert(0, "Volumes")
        self.volumes_entry.pack()

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

        if title and genre and volumes:
            new_book = Book(title, genre, volumes)
            self.library.add_book_to_catalog(new_book)
            self.load_books()
            self.clear_entry_fields()

    def clear_entry_fields(self):
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.volumes_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookGUI(root)
    root.mainloop()
