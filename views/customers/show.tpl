% rebase('base.tpl')

<h1>Customer: {{customer.id}}</h1>

First Name: {{customer.first_name}}<br />
Last Name: {{customer.last_name}}<br />
Phone Number: {{customer.phone_number}}<br />
Address: {{customer.address}}<br />
City: {{customer.city}}<br />
Country: {{customer.country}}<br /><br />

<a href='/customers'>[Back]</a>
