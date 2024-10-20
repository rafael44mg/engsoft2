class Loan:
    def __init__(self, book):
        if book.copies > 0:
            self.book = book
            book.copies -= 1
        else:
            raise ValueError("No copies available for loan")

    def return_book(self):
        self.book.copies += 1
