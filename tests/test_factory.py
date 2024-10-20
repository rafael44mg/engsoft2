import unittest
from library.factory import ConcreteLibraryFactory
from library.loan import Loan

class TestLibraryFactory(unittest.TestCase):

    def setUp(self):
        self.factory = ConcreteLibraryFactory()

    def test_create_book(self):
        book = self.factory.create_book("The Hobbit", "J.R.R. Tolkien", 3)
        self.assertEqual(book.title, "The Hobbit")
        self.assertEqual(book.author, "J.R.R. Tolkien")
        self.assertEqual(book.copies, 3)

    def test_create_loan(self):
        book = self.factory.create_book("1984", "George Orwell", 2)
        loan = self.factory.create_loan(book)
        self.assertEqual(book.copies, 1)

        with self.assertRaises(ValueError):
            for _ in range(2):  # Vai esgotar as cópias
                self.factory.create_loan(book)

    def test_return_book(self):
        book = self.factory.create_book("Brave New World", "Aldous Huxley", 1)
        loan = self.factory.create_loan(book)
        loan.return_book()
        self.assertEqual(book.copies, 1)

if __name__ == "__main__":
    unittest.main()
