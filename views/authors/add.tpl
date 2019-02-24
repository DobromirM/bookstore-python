% rebase('base.tpl')

<h1>Add Author</h1>

<form action='/authors/add' method='post'>

    First Name: <input type='text' name='first_name' value='' required /><br/>
    Last Name: <input type='text' name='last_name' value='' required /><br/><br/>

    <input type='submit' value='Add' />

</form>
