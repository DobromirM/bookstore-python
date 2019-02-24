% rebase('base.tpl')

<h1>Add Publisher</h1>

<form action='/publishers/add' method='post'>

    Name: <input type='text' name='name' value='' required /><br/>

    Country: <input type='text' name='country' value='' required /><br/><br/>

    <input type='submit' value='Add' />

</form>
