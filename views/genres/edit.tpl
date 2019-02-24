% rebase('base.tpl')

<h1>Edit Genre</h1>

<form action='/genres/{{genre.id}}/edit' method='post'>

    Name: <input type='text' name='name' value='{{genre.name}}' required /><br/><br/>

    <input type='submit' value='Save' />

</form>
