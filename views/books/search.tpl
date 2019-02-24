% rebase('base.tpl')

<h1>Search for a Book</h1>

<form action='/books/search/title' method='post'>
    Search by Title:
    <input type='text' name='title' value='' />
    <input type='submit' value='Search' /> <br />
</form>

<form action='/books/search/author' method='post'>
    Search by Author:

     <select name='author'>
                    %for a in authors:
                        <option value='{{a.id}}'>{{a.first_name}} {{a.last_name}}</option>
                    %end
    </select>

    <input type='submit' value='Search' /> <br />
</form>

<form action='/books/search/publisher' method='post'>
    Search by Publisher:

     <select name='publisher'>
                    %for p in publishers:
                        <option value='{{p.id}}'>{{p.name}}</option>
                    %end
    </select>

    <input type='submit' value='Search' /> <br />
</form>

<a href='/books'>[Back]</a>