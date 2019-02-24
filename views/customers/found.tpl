% rebase('base.tpl')

% if not customers:
    <h1>No Customers Found!</h1>
% else:
    <h1>Customers Found:</h1>
% end

<ul>
    %for c in customers:
        <li>
            <a href='/customers/{{c.id}}/'>{{c.first_name}} {{c.last_name}}</a>
            <a href='/customers/{{c.id}}/edit'>[Edit]</a>
            <a href='/customers/{{c.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/customers'>[Back]</a>