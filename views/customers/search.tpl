% rebase('base.tpl')

<h1>Search for a Customers</h1>

<form action='/customers/search/name' method='post'>
    Search by Name:
    <input type='text' name='name' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<form action='/customers/search/country' method='post'>
    Search by Country:
    <input type='text' name='country' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<a href='/customers'>[Back]</a>