% rebase('base.tpl')

% if not publishers:
    <h1>No Publishers Found!</h1>
% else:
    <h1>Publishers Found:</h1>
% end

<ul>
    %for p in publishers:
        <li>
            <a href='/publishers/{{p.id}}/'>{{p.name}}</a>
            <a href='/publishers/{{p.id}}/edit'>[Edit]</a>
            <a href='/publishers/{{p.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/publishers'>[Back]</a>