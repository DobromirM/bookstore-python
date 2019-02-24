% rebase('base.tpl')

<h1>List of Orders</h1>

<ul>
    %for o in orders:
        <li>
            <a href='/orders/{{o.id}}/'>Order: {{o.id}} - {{o.customer.first_name}} {{o.customer.last_name}}</a>
            <a href='/orders/{{o.id}}/edit'>[Edit]</a>
            <a href='/orders/{{o.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/orders/add'>[Add Order]</a> <br />
<a href='/orders/search'>[Search Orders]</a> <br />
<a href='/'>[Home]</a><br />