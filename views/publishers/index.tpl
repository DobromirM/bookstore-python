% rebase('base.tpl')

<h1>List of Publishers</h1>

<ul>
    %for p in publishers:
        <li>
            <a href='/publishers/{{p.id}}/'>{{p.name}}</a>
            <a href='/publishers/{{p.id}}/edit'>[Edit]</a>
            <a href='/publishers/{{p.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/publishers/add'>[Add Publisher]</a> <br />
<a href='/publishers/search'>[Search Publisher]</a> <br />
<a href='/'>[Home]</a><br />