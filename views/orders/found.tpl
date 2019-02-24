% rebase('base.tpl')

% if not orders:
    <h1>No Orders Found!</h1>
% else:
    <h1>Orders Found:</h1>
% end

<ul>
    %for o in orders:
        <li>
            <a href='/orders/{{o.id}}/'>Order: {{o.id}} - {{o.customer.first_name}} {{o.customer.last_name}}</a>
            <a href='/orders/{{o.id}}/edit'>[Edit]</a>
            <a href='/orders/{{o.id}}/delete'>[Delete]</a>
        </li>
    %end
</ul>

<a href='/orders'>[Back]</a>