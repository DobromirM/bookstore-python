% rebase('base.tpl')

<h1>List of Books</h1>

<ul>
    %for b in books:
        <li>
            <a href='/books/{{b.id}}/'>{{b.title}}</a>
            <a href='/books/{{b.id}}/edit'>[Edit]</a>
            <a href='/books/{{b.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/books/add'>[Add Book]</a> <br />
<a href='/books/search'>[Search Books]</a> <br />
<a href='/'>[Home]</a><br />
