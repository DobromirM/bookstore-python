% rebase('base.tpl')

<h1>Search for a Publishers</h1>

<form action='/publishers/search/name' method='post'>
    Search by Name:
    <input type='text' name='name' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<form action='/publishers/search/country' method='post'>
    Search by Country:
    <input type='text' name='country' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<a href='/publishers'>[Back]</a>