% rebase('base.tpl')

<h1>Search for an Authors</h1>

<form action='/authors/search/first' method='post'>
    First Name: <input type='text' name='first_name' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<form action='/authors/search/last' method='post'>
    Last Name: <input type='text' name='last_name' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<a href='/authors'>[Back]</a>