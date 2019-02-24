% rebase('base.tpl')

<h1>List of Authors</h1>

<ul>
    %for a in authors:
        <li>
            <a href='/authors/{{a.id}}/'>{{a.first_name}} {{a.last_name}}</a>
            <a href='/authors/{{a.id}}/edit'>[Edit]</a>
            <a href='/authors/{{a.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/authors/add'>[Add Author]</a> <br />
<a href='/authors/search'>[Search Authors]</a> <br />
<a href='/'>[Home]</a><br />
