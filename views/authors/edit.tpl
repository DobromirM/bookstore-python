% rebase('base.tpl')

<h1>Edit Author</h1>

<form action='/authors/{{author.id}}/edit' method='post'>

    First Name: <input type='text' name='first_name' value='{{author.first_name}}' required /><br/>
    Last Name: <input type='text' name='last_name' value='{{author.last_name}}' required /><br/><br/>

    <input type='submit' value='Save' />

</form>
