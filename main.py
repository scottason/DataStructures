import tkinter as tk
from Classes.LibraryCatalog import LibraryCatalog
from Classes.BooksGui import BookGUI

def main():
    # Create an instance of the LibraryCatalog with a relative path
    library = LibraryCatalog("ExcelFiles/books.xlsx")

    # Create main window
    root = tk.Tk()

    # Create an instance of BookGUI
    book_gui = BookGUI(root, library)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
