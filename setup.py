import json
from entities import *

'''
    Setup module
    ===========

    The setup module should have all the methods that has to be executed before
    the application is started (i.e. seeding the database).
'''


#######################################################
### BEGIN setup methods
#######################################################
@db_session
def seed_database(dump_filename):

    # reading the json file
    data = json.load(open(dump_filename, 'r'))

    # going through the list of authors
    for record in data['Authors']:

        # creating a new authors object for each entry
        Author(first_name=record['first_name'],
               last_name=record['last_name'])

    # going through the list of publishers
    for record in data['Publishers']:

        # creating a new publisher object for each entry
        Publisher(name=record['name'],
                  country=record['country'])

    # going through the list of genres
    for record in data['Genres']:

        # creating a new genre object for each entry
        Genre(name=record['name'])

    # going through the list of customers
    for record in data['Customers']:

        # creating a new customer object for each entry
        Customer(first_name=record['first_name'],
                 last_name=record['last_name'],
                 phone_number=record['phone_number'],
                 address=record['address'],
                 city=record['city'],
                 country=record['country'])

    # going through the list of books
    for record in data['Books']:

        # creating a new book object for each entry
        Book(title=record['title'],
             author=Author[record['author']],
             publisher=Publisher[record['publisher']],
             genre=Genre[record['genre']],
             year=record['year'],
             price=record['price'])

    # going through the list of orders
    for record in data['Orders']:

        # creating a new order object for each entry
        Order(customer=Customer[record['customer']],
              books=[Book[id] for id in record['books']],
              purchase_date=record['purchase_date'],
              total=sum([Book[id].price for id in record['books']]))


#######################################################
### END setup methods
#######################################################


if __name__ == "__main__":
    # call your setup methods
    seed_database(config.DB_DUMP_FILE_NAME)
