from pymongo import MongoClient


def connect():
    client = MongoClient(port=27017)
    db = client.bookdb
    return db


def insert(title, year, author, isbn):
    db = connect()
    record = {
        "book_title": title,
        "published_on": year,
        "author": author,
        "ISBN": isbn
    }
    db.book.insert_one(record)


def view():
    db = connect()
    book_collection = db.book.find({},{"book_title":1,"published_on":1,"author":1,"ISBN":1,"_id":0 })
    book_item = ()
    book_list = []
    for books in book_collection:
        book_item = tuple(books.values())
        book_list.append(book_item)
    return book_list

def search(title="", year="", author="", isbn=""):
    db = connect()
    book_list = []
    if (len(author) > 0 and len(title) > 0 and len(isbn) > 0 and len(year) > 0):
        result = db.book.find(
            {"author": author, "book_title": title, "published_on": year, "ISBN": isbn})
    elif (len(author) > 0 and len(title) > 0 and len(isbn) > 0 and len(year)==0):
        result = db.book.find(
            {"author": author, "book_title": title, "ISBN": isbn})
    elif (len(author) > 0 and len(title) > 0 and len(isbn)==0 and len(year) > 0):
        result = db.book.find(
            {"author": author, "book_title": title, "published_on": year})
    elif (len(author)==0 and len(title) > 0 and len(isbn) > 0 and len(year) > 0):
        result = db.book.find(
            {"ISBN": isbn, "book_title": title, "published_on": year})
    elif (len(author) > 0 and len(title)==0 and len(isbn) > 0 and len(year) > 0):
        result = db.book.find(
            {"ISBN": isbn, "author": author, "published_on": year})
    elif (len(author) > 0 and len(title)==0 and len(isbn) > 0 and len(year)==0):
        result = db.book.find({"author": author, "ISBN": isbn})
    elif (len(author) > 0 and len(title) > 0 and len(isbn)==0 and len(year)==0):
        result = db.book.find({"author": author, "book_title": title})
    elif (len(author) > 0 and len(title)==0 and len(isbn)==0 and len(year) > 0):
        result = db.book.find({"author": author, "published_on": year})
    elif (len(author)==0 and len(title) > 0 and len(isbn)==0 and len(year) > 0):
        result = db.book.find({"book_title": title, "published_on": year})
    elif (len(author)==0 and len(title) > 0 and len(isbn) > 0 and len(year)==0):
        result = db.book.find({"book_title": title, "ISBN": isbn})
    elif (len(author)==0 and len(title)==0 and len(isbn) > 0 and len(year) > 0):
        result = db.book.find({"published_on": year, "ISBN": isbn})
    elif (author):
        result = db.book.find({"author": author})
    elif (title):
        result = db.book.find({"book_title": title})
    elif (year):
        result = db.book.find({"published_on": year})
    elif (isbn):
        result = db.book.find({"ISBN": isbn})
    else:
        result = db.book.find({})

    for books in result:
        book_list.append('{0} {1} {2} {3}'.format(
            books['book_title'], books['published_on'], books['author'], books['ISBN']))
    return book_list

def delete(title="", year="", author="", isbn=""):
    db=connect()
    db.book.find({"book_title": title,
        "published_on": year,
        "author": author,
        "ISBN": isbn}).getObjectId("_id")
    print(id)

delete()