% rebase('base.tpl')

% if not books:
    <h1>No Books Found!</h1>
% else:
    <h1>Books Found:</h1>
% end

<ul>
    %for b in books:
        <li>
            <a href='/books/{{b.id}}/'>{{b.title}}</a>
            <a href='/books/{{b.id}}/edit'>[Edit]</a>
            <a href='/books/{{b.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/books'>[Back]</a>