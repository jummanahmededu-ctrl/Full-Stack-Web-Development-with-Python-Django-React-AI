class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


class Member(Person):
    total_members = 0

    def __init__(self, member_id, name, age):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = []
        Member.total_members += 1

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def display_info(self):
        print(f"Member ID : {self.member_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Borrowed Books : {len(self.borrowed_books)}")
        print("-"*35)

    @classmethod
    def show_total_members(cls):
        print("Total Members:", cls.total_members)


class Book:
    total_books = 0

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True
        Book.total_books += 1

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value

    def display_book(self):
        print(f"ISBN : {self.isbn}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print("Status :", "Available" if self.available else "Borrowed")
        print("-"*35)

    @classmethod
    def show_total_books(cls):
        print("Total Books:", cls.total_books)

    @staticmethod
    def library_message():
        print("Welcome to the Library!")


class Library:
    def __init__(self):
        self.books=[]
        self.members=[]

    def add_book(self,title,author,isbn):
        if any(b.isbn==isbn for b in self.books):
            print("Error: ISBN already exists."); return
        self.books.append(Book(title,author,isbn))
        print("Book added successfully!")

    def register_member(self,member_id,name,age):
        if any(m.member_id==member_id for m in self.members):
            print("Error: Member ID already exists."); return
        if age<=0:
            print("Error: Age must be greater than 0."); return
        self.members.append(Member(member_id,name,age))
        print("Member registered successfully!")

    def find_member(self,mid):
        return next((m for m in self.members if m.member_id==mid),None)

    def find_book(self,isbn):
        return next((b for b in self.books if b.isbn==isbn),None)

    def borrow_book(self,mid,isbn):
        m=self.find_member(mid); b=self.find_book(isbn)
        if not m: print("Member not found."); return
        if not b: print("Book not found."); return
        if not b.available: print("Book unavailable."); return
        m.borrow_book(b); b.available=False
        print("Book borrowed successfully.")

    def return_book(self,mid,isbn):
        m=self.find_member(mid); b=self.find_book(isbn)
        if not m: print("Member not found."); return
        if not b: print("Book not found."); return
        if b not in m.borrowed_books:
            print("This member didn't borrow this book."); return
        m.return_book(b); b.available=True
        print("Book returned successfully.")

    def show_books(self):
        if not self.books:
            print("No books available."); return
        for b in self.books: b.display_book()

    def show_members(self):
        if not self.members:
            print("No members found."); return
        for m in self.members: m.display_info()

    def search_book(self,title):
        for b in self.books:
            if title.lower() in b.title.lower():
                b.display_book(); return
        print("Book not found.")


def menu():
    print("\n"+"="*40)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Book\n2. Register Member\n3. Borrow Book\n4. Return Book")
    print("5. Show All Books\n6. Show All Members\n7. Search Book\n8. Exit")

Book.library_message()
library=Library()

while True:
    menu()
    c=input("Enter your choice: ").strip()
    if c=="1":
        library.add_book(input("Title: "),input("Author: "),input("ISBN: "))
    elif c=="2":
        library.register_member(input("Member ID: "),input("Name: "),int(input("Age: ")))
    elif c=="3":
        library.borrow_book(input("Member ID: "),input("ISBN: "))
    elif c=="4":
        library.return_book(input("Member ID: "),input("ISBN: "))
    elif c=="5":
        library.show_books()
    elif c=="6":
        library.show_members()
    elif c=="7":
        library.search_book(input("Title: "))
    elif c=="8":
        print("\nThank you for using Library Management System.\nGoodbye!"); break
    else:
        print("Invalid choice.")

