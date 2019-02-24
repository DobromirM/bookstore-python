% rebase('base.tpl')

<h1>List of Customers</h1>

<ul>
    %for c in customers:
        <li>
            <a href='/customers/{{c.id}}/'>{{c.first_name}} {{c.last_name}}</a>
            <a href='/customers/{{c.id}}/edit'>[Edit]</a>
            <a href='/customers/{{c.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/customers/add'>[Add Customer]</a> <br />
<a href='/customers/search'>[Search Customers]</a> <br />
<a href='/'>[Home]</a><br />
