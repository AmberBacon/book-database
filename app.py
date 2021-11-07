from models import Base, session, Book, engine


# import models 
# main menu - add, search, analysis, exit, view
# add book to the database
# edit books
# delete books
# search books
# data cleaning 
# loop runs program 

if __name__ == '__main__':
    Base.metadata.create_all(engine)