from bottle import *
from entities import *
from pony.orm.integration.bottle_plugin import PonyPlugin

install(PonyPlugin())

'''
    Server module
    =============
    This module provides all the basic functionalities of the application.
    The module is a standard Bottle application and runs on port 8080.
'''

#######################################################
### Begin route declaration
#######################################################


'''
    Index page of the application.
'''


@route('/')
@view('index')
def index():
    return


#############
### Books ###
#############


'''
    Show all the books in the system.
'''


@route('/books')
@view('books/index')
def book_all():
    # select all the books from the db
    books = select(b for b in Book)

    # set the books for the template
    return dict(books=books)


'''
    Show information for specific book.
'''


@route('/books/<id>/')
@view('books/show')
def book_show(id):
    # get the book by id
    book = Book[id]

    # set the book for the template
    return dict(book=book)


'''
    Add new books to the system.
'''


@route('/books/add')
@view('books/add')
def book_add():
    # retrieve the list of authors
    authors = Author.select()

    # retrieve the list of publishers
    publishers = Publisher.select()

    # retrieve the list of genres
    genres = Genre.select()

    # set the data for the screen
    return dict(authors=authors, publishers=publishers, genres=genres)


'''
    Take in as input the create form for a book and
    add the the book to the database.
'''


@route('/books/add', method='POST')
def book_create():
    # obtain the data for the book
    title = request.forms.get('title')
    author = request.forms.get('author')
    publisher = request.forms.get('publisher')
    genre = request.forms.get('genre')
    year = request.forms.get('year')
    price = request.forms.get('price')

    # create the new book
    Book(title=title, author=author, publisher=publisher, genre=genre, year=year, price=price)

    # redirect the user to the books overview page
    redirect("/books")


'''
    Edit books information.
'''


@route('/books/<id>/edit')
@view('books/edit')
def book_edit(id):
    # retrieve the book by id from the database
    book = Book[id]

    # retrieve the list of authors
    authors = Author.select()

    # retrieve the list of publishers
    publishers = Publisher.select()

    # retrieve the list of genres
    genres = Genre.select()

    # set the data for the edit screen
    return dict(book=book, authors=authors, publishers=publishers, genres=genres)


'''
    Take in as input the edit form for a book and
    update the database accordingly.
'''


@route('/books/<id>/edit', method='POST')
def book_update(id):
    # retrieve the book by id from the database
    book = Book[id]

    # updating the data of the book
    book.title = request.forms.get('title')
    book.author = Author[request.forms.get('author')]
    book.publisher = Publisher[request.forms.get('publisher')]
    book.genre = Genre[request.forms.get('genre')]
    book.year = request.forms.get('year')
    book.price = request.forms.get('price')

    # redirect the user to the book info page
    redirect("/books/%s/" % id)


'''
    Delete book by id.
'''


@route('/books/<id>/delete')
def book_delete(id):
    # delete the book with the specified id from the database
    Book[id].delete()

    # redirect the user to the books overview page
    redirect("/books")


'''
    Search page for books.
'''


@route('/books/search')
@view('books/search')
def book_search():
    # retrieve the list of authors
    authors = Author.select()

    # retrieve the list of publishers
    publishers = Publisher.select()

    # set the data for the search screen
    return dict(authors=authors, publishers=publishers)


'''
    Search books by title.
'''


@route('/books/search/title', method="POST")
@view('books/found')
def book_search_title():
    # obtain the title from the form
    title = request.forms.get('title')

    # filter only the books with that title
    books = Book.select(lambda b: b.title == title)

    # set the data for the screen
    return dict(books=books)


'''
    Search books by author.
'''


@route('/books/search/author', method="POST")
@view('books/found')
def book_search_author():
    # obtain the author from the form
    author = request.forms.get('author')

    # filter only the books with that author
    books = Book.select(lambda b: b.author.id == author)

    # set the data for the screen
    return dict(books=books)


'''
    Search books by publisher.
'''


@route('/books/search/publisher', method="POST")
@view('books/found')
def book_search_publisher():
    # obtain the publisher from the form
    publisher = request.forms.get('publisher')

    # filter only the books with that publisher
    books = Book.select(lambda b: b.publisher.id == publisher)

    # set the data for the screen
    return dict(books=books)


###############
### Authors ###
###############


'''
    Show all the authors in the system.
'''


@route('/authors')
@view('authors/index')
def author_all():
    # select all the authors from the db
    authors = select(a for a in Author)

    # set the authors for the template
    return dict(authors=authors)


'''
    Show information for specific author.
'''


@route('/authors/<id>/')
@view('authors/show')
def author_show(id):
    # get the author by id
    author = Author[id]

    # set the author for the template
    return dict(author=author)


'''
    Add new author to the system.
'''


@route('/authors/add')
@view('authors/add')
def author_add():
    return


'''
    Take in as input the create form for an author and
    add the the author to the database.
'''


@route('/authors/add', method='POST')
def author_create():
    # obtain the data for the author
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')

    # create the new author
    Author(first_name=first_name, last_name=last_name)

    # redirect the user to the author overview page
    redirect("/authors")


'''
    Edit authors information.
'''


@route('/authors/<id>/edit')
@view('authors/edit')
def author_edit(id):
    # retrieve the author by id from the database
    author = Author[id]

    # set the data for the edit screen
    return dict(author=author)


'''
    Take in as input the edit form for an author and
    update the database accordingly.
'''


@route('/authors/<id>/edit', method='POST')
def author_update(id):
    # retrieve the author by id from the database
    author = Author[id]

    # updating the data of the author
    author.first_name = request.forms.get('first_name')
    author.last_name = request.forms.get('last_name')

    # redirect the user to the author info page
    redirect("/authors/%s/" % id)


'''
    Delete author by id.
'''


@route('/authors/<id>/delete')
def author_delete(id):
    # delete the author with the specified id from the database
    Author[id].delete()

    # redirect the user to the authors overview page
    redirect("/authors")


'''
    Search page for authors.
'''


@route('/authors/search')
@view('authors/search')
def author_search():
    return


'''
    Search authors by first name.
'''


@route('/authors/search/first', method="POST")
@view('authors/found')
def author_search_names():
    # obtain the first name from the form
    first_name = request.forms.get('first_name')

    # filter only the authors with that first name
    authors = Author.select(lambda a: a.first_name == first_name)

    # set the data for the screen
    return dict(authors=authors)


'''
    Search authors by last name.
'''


@route('/authors/search/last', method="POST")
@view('authors/found')
def author_search_names():
    # obtain the names of the author
    last_name = request.forms.get('last_name')

    # filter only the authors with that last name
    authors = Author.select(lambda a: a.last_name == last_name)

    # set the data for the screen
    return dict(authors=authors)


##################
### Publishers ###
##################


'''
    Show all the publishers in the system.
'''


@route('/publishers')
@view('publishers/index')
def publisher_all():
    # select all the publishers from the db
    publishers = select(p for p in Publisher)

    # set the publishers for the template
    return dict(publishers=publishers)


'''
    Show information for specific publisher.
'''


@route('/publishers/<id>/')
@view('publishers/show')
def publisher_show(id):
    # get the publisher by id
    publisher = Publisher[id]

    # set the publisher for the template
    return dict(publisher=publisher)


'''
    Add new publisher to the system.
'''


@route('/publishers/add')
@view('publishers/add')
def publisher_add():
    return


'''
    Take in as input the create form for a publisher and
    add the the publisher to the database.
'''


@route('/publishers/add', method='POST')
def publisher_create():
    # obtain the data for the publisher
    name = request.forms.get('name')
    country = request.forms.get('country')

    # create the new publisher
    Publisher(name=name, country=country)

    # redirect the user to the publisher overview page
    redirect("/publishers")


'''
    Edit publisher information.
'''


@route('/publishers/<id>/edit')
@view('publishers/edit')
def publisher_edit(id):
    # retrieve the publisher by id from the database
    publisher = Publisher[id]

    # set the data for the edit screen
    return dict(publisher=publisher)


'''
    Take in as input the edit form for a publisher and
    update the database accordingly.
'''


@route('/publishers/<id>/edit', method='POST')
def publisher_update(id):
    # retrieve the publisher by id from the database
    publisher = Publisher[id]

    # updating the data of the publisher
    publisher.name = request.forms.get('name')
    publisher.country = request.forms.get('country')

    # redirect the user to the publisher info page
    redirect("/publishers/%s/" % id)


'''
    Delete publisher by id.
'''


@route('/publishers/<id>/delete')
def publisher_delete(id):
    # delete the publisher with the specified id from the database
    Publisher[id].delete()

    # redirect the user to the publisher overview page
    redirect("/publishers")


'''
    Search page for publishers.
'''


@route('/publishers/search')
@view('publishers/search')
def publisher_search():
    return


'''
    Search publisher by name.
'''


@route('/publishers/search/name', method="POST")
@view('publishers/found')
def publisher_search_name():
    # obtain the name of the publisher
    name = request.forms.get('name')

    # filter only the publishers with that name
    publishers = Publisher.select(lambda p: p.name == name)

    # set the data for the screen
    return dict(publishers=publishers)


'''
    Search publisher by country.
'''


@route('/publishers/search/country', method="POST")
@view('publishers/found')
def publisher_search_country():
    # obtain the country of the publisher
    country = request.forms.get('country')

    # filter only the publishers with the specific country
    publishers = Publisher.select(lambda p: p.country == country)

    # set the data for the screen
    return dict(publishers=publishers)


#############
### Genre ###
#############


'''
    Show all the genres in the system.
'''


@route('/genres')
@view('genres/index')
def genre_all():
    # select all the genres from the db
    genres = select(g for g in Genre)

    # set the genres for the template
    return dict(genres=genres)


'''
    Show information for specific genres.
'''


@route('/genres/<id>/')
@view('genres/show')
def genre_show(id):
    # get the genre by id
    genre = Genre[id]

    # set the genre for the template
    return dict(genre=genre)


'''
    Add new genre to the system.
'''


@route('/genres/add')
@view('genres/add')
def genre_add():
    return


'''
    Take in as input the create form for a genre and
    add the the genre to the database.
'''


@route('/genres/add', method='POST')
def genre_create():
    # obtain the data for the genre
    name = request.forms.get('name')

    # create the new genre
    Genre(name=name)

    # redirect the user to the genre overview page
    redirect("/genres")


'''
    Edit genre information.
'''


@route('/genres/<id>/edit')
@view('genres/edit')
def genre_edit(id):
    # retrieve the genre by id from the database
    genre = Genre[id]

    # set the data for the edit screen
    return dict(genre=genre)


'''
    Take in as input the edit form for a genre and
    update the database accordingly.
'''


@route('/genres/<id>/edit', method='POST')
def genre_update(id):
    # retrieve the genre by id from the database
    genre = Genre[id]

    # updating the data of the genre
    genre.name = request.forms.get('name')

    # redirect the user to the genre info page
    redirect("/genres/%s/" % id)


'''
    Delete genre by id.
'''


@route('/genres/<id>/delete')
def genre_delete(id):
    # delete the genre with the specified id from the database
    Genre[id].delete()

    # redirect the user to the genre overview page
    redirect("/genres")


'''
    Search page for genres.
'''


@route('/genres/search')
@view('genres/search')
def genre_search():
    return


'''
    Search genre by name.
'''


@route('/genres/search/name', method="POST")
@view('genres/found')
def genre_search_name():
    # obtain the name of the genre
    name = request.forms.get('name')

    # filter only the genres with that name
    genres = Genre.select(lambda g: g.name == name)

    # set the data for the screen
    return dict(genres=genres)


#################
### Customers ###
#################


'''
    Show all the customers in the system.
'''


@route('/customers')
@view('customers/index')
def customer_all():
    # select all the customers from the db
    customers = select(c for c in Customer)

    # set the customers for the template
    return dict(customers=customers)


'''
    Show information for specific customers.
'''


@route('/customers/<id>/')
@view('customers/show')
def customer_show(id):
    # get the customer by id
    customer = Customer[id]

    # set the customer for the template
    return dict(customer=customer)


'''
    Add new customer to the system.
'''


@route('/customers/add')
@view('customers/add')
def customer_add():
    return


'''
    Take in as input the create form for a customer and
    add the the customer to the database.
'''


@route('/customers/add', method='POST')
def customer_create():
    # obtain the data for the customer
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    phone_number = request.forms.get('phone_number')
    address = request.forms.get('address')
    city = request.forms.get('city')
    country = request.forms.get('country')

    # create the new customer
    Customer(first_name=first_name,
             last_name=last_name,
             phone_number=phone_number,
             address=address,
             city=city,
             country=country)

    # redirect the user to the customers overview page
    redirect("/customers")


'''
    Edit customer information.
'''


@route('/customers/<id>/edit')
@view('customers/edit')
def customer_edit(id):
    # retrieve the customer by id from the database
    customer = Customer[id]

    # set the data for the edit screen
    return dict(customer=customer)


'''
    Take in as input the edit form for a customer and
    update the database accordingly.
'''


@route('/customers/<id>/edit', method='POST')
def customer_update(id):
    # retrieve the customer by id from the database
    customer = Customer[id]

    # updating the data of the customer
    customer.first_name = request.forms.get('first_name')
    customer.last_name = request.forms.get('last_name')
    customer.phone_number = request.forms.get('phone_number')
    customer.address = request.forms.get('address')
    customer.city = request.forms.get('city')
    customer.country = request.forms.get('country')

    # redirect the user to the customer info page
    redirect("/customers/%s/" % id)


'''
    Delete customer by id.
'''


@route('/customers/<id>/delete')
def customer_delete(id):
    # delete the customer with the specified id from the database
    Customer[id].delete()

    # redirect the user to the customers overview page
    redirect("/customers")


'''
    Search page for customers.
'''


@route('/customers/search')
@view('customers/search')
def customer_search():
    return


'''
    Search customer by name.
'''


@route('/customers/search/name', method="POST")
@view('customers/found')
def customer_search_name():
    # obtain the name of the customer
    name = request.forms.get('name')

    # filter only the customers with that name
    customers = Customer.select(lambda c: c.first_name == name or c.last_name == name or c.first_name + " " + c.last_name == name)

    # set the data for the screen
    return dict(customers=customers)


'''
    Search customer by country.
'''


@route('/customers/search/country', method="POST")
@view('customers/found')
def customer_search_country():
    # obtain the country of the customer
    country = request.forms.get('country')

    # filter only the customers from that country
    customers = Customer.select(lambda c: c.country == country)

    # set the data for the screen
    return dict(customers=customers)


##############
### Orders ###
##############


'''
    Show all the orders in the system.
'''


@route('/orders')
@view('orders/index')
def order_all():
    # select all the orders from the db
    orders = select(o for o in Order)

    # set the orders for the template
    return dict(orders=orders)


'''
    Show information for specific order.
'''


@route('/orders/<id>/')
@view('orders/show')
def orders_show(id):
    # get the order by id
    order = Order[id]

    # set the order for the template
    return dict(order=order)


'''
    Add new order to the system.
'''


@route('/orders/add')
@view('orders/add')
def order_add():
    # select all the customers from the db
    customers = Customer.select()

    # select all the books from the db
    books = Book.select()

    return dict(customers=customers, books=books)


'''
    Take in as input the create form for an order and
    add the the order to the database.
'''


@route('/orders/add', method='POST')
def order_create():
    # obtain the data for the order
    customer = request.forms.get('customer')
    purchase_date = datetime.now().strftime("%Y-%m-%d")
    books = request.forms.getlist('books')

    # create the new order
    Order(customer=customer,
          purchase_date=purchase_date,
          books=[Book[id] for id in books],
          total=sum([Book[id].price for id in books]))

    # redirect the user to the orders overview page
    redirect("/orders")


'''
    Edit order information.
'''


@route('/orders/<id>/edit')
@view('orders/edit')
def order_edit(id):
    # retrieve the order by id from the database
    order = Order[id]

    # select all the customers from the db
    customers = Customer.select()

    # select all the books from the db
    books = Book.select()

    # set the data for the edit screen
    return dict(order=order, customers=customers, books=books)


'''
    Take in as input the edit form for an order and
    update the database accordingly.
'''


@route('/orders/<id>/edit', method='POST')
def order_update(id):
    # retrieve the order by id from the database
    order = Order[id]

    # updating the data of the order
    order.customer = request.forms.get('customer')
    order.purchase_date = request.forms.get('date')
    order.books = [Book[id] for id in request.forms.getlist('books')]
    order.total = sum([Book[id].price for id in request.forms.getlist('books')])

    # redirect the user to the order info page
    redirect("/orders/%s/" % id)


'''
    Delete order by id.
'''


@route('/orders/<id>/delete')
def order_delete(id):
    # delete the order with the specified id from the database
    Order[id].delete()

    # redirect the user to the orders overview page
    redirect("/orders")


'''
    Search page for order.
'''


@route('/orders/search')
@view('orders/search')
def customer_search():
    # select all the customers from the db
    customers = Customer.select()

    # set the data for the screen
    return dict(customers=customers)


'''
    Search order by customer.
'''


@route('/orders/search/customer', method="POST")
@view('orders/found')
def order_search_customer():
    # obtain the the customer
    customer = Customer[request.forms.get('customer')]

    # filter only the orders for that customer
    orders = Order.select(lambda o: o.customer == customer)

    # set the data for the screen
    return dict(orders=orders)


'''
    Search orders by id.
'''


@route('/orders/search/id', method="POST")
@view('orders/found')
def order_search_id():
    # obtain the id of the order
    id = request.forms.get('id')

    # filter the order with that id
    orders = Order.select(lambda o: o.id == id)

    # set the data for the screen
    return dict(orders=orders)


#######################################################
### END route declaration
#######################################################

run(host='localhost', port=8080, debug=True, reloader=True)
