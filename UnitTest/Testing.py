import unittest
from main import LibraryCatalog, BookGUI
from Classes.Books import Book
import tkinter as tk

class TestBook(unittest.TestCase):

    def test_book_creation(self):
        book = Book("Title", "Genre", "3,4")
        self.assertEqual(book.get_info(), "Title (Genre) - Volumes: (3 , 4)")

    def test_library_catalog(self):
        library = LibraryCatalog("test_file")
        book1 = Book("Book1", "Sci-Fi", 5)
        book2 = Book("Book2", "Fantasy", 3)

        library.add_book_to_catalog(book1)
        library.add_book_to_catalog(book2)

        self.assertEqual(len(library.catalog), 2)

    def test_book_gui(self):
        root = tk.Tk()
        library = LibraryCatalog("ExcelFiles/test.xlsx")
        book_gui = BookGUI(root, library)

        book_gui.title_entry.insert(0, "GUI Book")
        book_gui.genre_entry.insert(0, "GUI Genre")
        book_gui.volumes_entry.insert(0, "4")

        book_gui.add_book()

        self.assertEqual(len(library.catalog), 1)
        self.assertEqual(library.catalog["GUI Book"].get_info(), "GUI Book (GUI Genre) - Volumes: (4)")

if __name__ == '__main__':
    unittest.main()
