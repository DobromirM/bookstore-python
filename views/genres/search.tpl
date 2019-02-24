% rebase('base.tpl')

<h1>Search for a Genres</h1>

<form action='/genres/search/name' method='post'>
    Search by Name:
    <input type='text' name='name' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<a href='/genres'>[Back]</a>