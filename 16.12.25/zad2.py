class LibraryAccount:
    def __init__(self,name :str):
        self.name=name
        self.borrowed_books=[]
    
    def borrow_book(self,book_name : str):
        self.borrowed_books.append(book_name)
        print(f"Borrowed book {book_name}.")

    def return_book(self,book_name: str):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            print(f"Removed book {book_name}.")
            return
        else:
            print(f"You havent borrowed book {book_name}.")
            return 
    
    def list_books(self):
        print("You have borrowed books: ")
        for b in self.borrowed_books:
            print(b)

a=LibraryAccount("a")
a.borrow_book("1984")
a.list_books()
a.return_book("1984")
a.list_books()