this project is about managing books and members using POOP (Python Orientated Object Programming)

Book Class: keps track of book info (title, author, copies)
Member Class: stores member details and what they’ve borrowed
Library Class: manages everything — adding books, lending, returning, showing info

Book Class
    What it does: Represents a single book
    Attributes: id, title, author, total copies, available copies
    actions:
    Borrow a book → decreases available copies
    Return a book → increases available copies

Member Class
    what it does: Represents a library member
    Attributes: id, name, email, borrowed books list

Library Class
    What it does: Connects books and members; manages all operations: Collections of books and members
    actions:
    Add books / add members
    Borrow / return books