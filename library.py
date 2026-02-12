class Book:
    def __init__(self , title, author):
        self.title = title
        self.author = author
        self.issued_book = False


class memebet():
    def __init__(self, memeber_id , book_name):
        self.member_id = memeber_id
        self.book_name = book_name
        self.borrowed_book = []

class library():
    def __init__(self ):
        self.book = []        
        self.memeber = []



    def add_book(self , book):
        self.book.append = book
        print("Book Added Sucessfully") 

    def add_member(self , member):
        self.member.append = member
        print("Member Added Sucessfully") 
