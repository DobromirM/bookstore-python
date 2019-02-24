% rebase('base.tpl')

<h1>Edit Publisher</h1>

<form action='/publishers/{{publisher.id}}/edit' method='post'>

    Title: <input type='text' name='name' value='{{publisher.name}}' required /><br/>

    Country: <input type='text' name='country' value='{{publisher.country}}' required /><br/><br/>

    <input type='submit' value='Save' />

</form>
