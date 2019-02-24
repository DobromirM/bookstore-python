% rebase('base.tpl')

<h1>Order: {{order.id}}</h1>

Customer: {{order.customer.first_name}} {{order.customer.last_name}}<br />
Purchase Date: {{order.purchase_date}}<br />
Total: {{order.total}}&pound;<br /><br />

Books:<br />
%for b in order.books:
    &emsp;{{b.title}}
    <br />
%end


<br /><a href='/orders'>[Back]</a>
