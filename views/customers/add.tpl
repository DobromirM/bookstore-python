% rebase('base.tpl')

<h1>Add Customer</h1>

<form action='/customers/add' method='post'>

    First Name: <input type='text' name='first_name' value='' required /><br/>

    Last Name: <input type='text' name='last_name' value='' required /><br/>

    Phone Number: <input type='text' name='phone_number' value='' required /><br/>

    Address: <input type='text' name='address' value='' required /><br/>

    City: <input type='text' name='city' value='' required /><br/>

    Country: <input type='text' name='country' value='' required /><br/><br/>

    <input type='submit' value='Add' />

</form>
