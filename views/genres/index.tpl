% rebase('base.tpl')

<h1>List of Genres</h1>

<ul>
    %for g in genres:
        <li>
            <a href='/genres/{{g.id}}/'>{{g.name}}</a>
            <a href='/genres/{{g.id}}/edit'>[Edit]</a>
            <a href='/genres/{{g.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/genres/add'>[Add Genre]</a> <br />
<a href='/genres/search'>[Search Genres]</a> <br />
<a href='/'>[Home]</a><br />