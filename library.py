class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_book = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_book = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully")

    def add_member(self, member):
        self.members.append(member)
        print("Member Added Successfully")

    def show_books(self):
        if not self.books:
            print("No books available")
        for book in self.books:
            status = "Issued" if book.issued_book else "Available"
            print(f"{book.book_id} | {book.title} | {book.author} | {status}")

    def issue_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member:
            if not book.issued_book:
                book.issued_book = True
                member.borrowed_book.append(book.title)
                print("Book issued successfully")
            else:
                print("Book already issued")
        else:
            print("Book or Member not found")

    def return_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member:
            if book.title in member.borrowed_book:
                book.issued_book = False
                member.borrowed_book.remove(book.title)
                print("Book returned successfully")
            else:
                print("This member didn't borrow this book")
        else:
            print("Book or Member not found")


library = Library()

while True:
    print("\n1.Add Book\n2.Add Member\n3.Show Books\n4.Issue Book\n5.Return Book\n6.Exit")
    choice = input("Enter choice: ")

    match choice:
        case "1":
            bid = int(input("Book ID: "))
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(Book(bid, title, author))

        case "2":
            mid = int(input("Member ID: "))
            name = input("Name: ")
            library.add_member(Member(mid, name))

        case "3":
            library.show_books()

        case "4":
            bid = int(input("Book ID: "))
            mid = int(input("Member ID: "))
            library.issue_book(bid, mid)

        case "5":
            bid = int(input("Book ID: "))
            mid = int(input("Member ID: "))
            library.return_book(bid, mid)

        case "6":
            print("Exiting Library System...")
            break

        case _:
            print("Invalid choice")
