% rebase('base.tpl')

<h1>Book: {{book.id}}</h1>

Title: {{book.title}}<br />
Author: {{book.author.first_name}} {{book.author.last_name}}<br />
Publisher: {{book.publisher.name}}<br />
Genre: {{book.genre.name}}<br />
Year: {{book.year}}<br />
Price: {{book.price}}&pound;<br /><br />

<a href='/books'>[Back]</a>
