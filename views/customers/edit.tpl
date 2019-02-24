% rebase('base.tpl')

<h1>Edit Customers</h1>

<form action='/customers/{{customer.id}}/edit' method='post'>

    First Name: <input type='text' name='first_name' value='{{customer.first_name}}' required /><br/>

    Last Name: <input type='text' name='last_name' value='{{customer.last_name}}' required /><br/>

    Phone Number: <input type='text' name='phone_number' value='{{customer.phone_number}}' required /><br/>

    Address: <input type='text' name='address' value='{{customer.address}}' required /><br/>

    City: <input type='text' name='city' value='{{customer.city}}' required /><br/>

    Country: <input type='text' name='country' value='{{customer.country}}' required /><br/><br/>

    <input type='submit' value='Save' />

</form>
