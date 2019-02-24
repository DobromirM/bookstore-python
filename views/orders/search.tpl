% rebase('base.tpl')

<h1>Search for a Orders</h1>

<form action='/orders/search/customer' method='post'>
    Search by Customer:

    <select name='customer'>
                    %for c in customers:
                        <option value='{{c.id}}'>{{c.first_name}} {{c.last_name}}</option>
                    %end
    </select>

    <input type='submit' value='Search' /> <br />
</form>

<form action='/orders/search/id' method='post'>
    Search by Order id:
    <input type='number' name='id' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<a href='/orders'>[Back]</a>