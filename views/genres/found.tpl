% rebase('base.tpl')

% if not genres:
    <h1>No Genres Found!</h1>
% else:
    <h1>Genres Found:</h1>
% end

<ul>
    %for g in genres:
        <li>
            <a href='/genres/{{g.id}}/'>{{g.name}}</a>
            <a href='/genres/{{g.id}}/edit'>[Edit]</a>
            <a href='/genres/{{g.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/genres'>[Back]</a>