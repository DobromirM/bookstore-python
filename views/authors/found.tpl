% rebase('base.tpl')

% if not authors:
    <h1>No Authors Found!</h1>
% else:
    <h1>Authors Found:</h1>
% end

<ul>
    %for a in authors:
        <li>
            <a href='/authors/{{a.id}}/'>{{a.first_name}} {{a.last_name}}</a>
            <a href='/authors/{{a.id}}/edit'>[Edit]</a>
            <a href='/authors/{{a.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/authors'>[Back]</a>