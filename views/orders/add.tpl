% rebase('base.tpl')

<h1>Add Order</h1>

<form action='/orders/add' method='post'>

    Customer: <select name='customer'>
                %for c in customers:
                    <option value='{{c.id}}'>{{c.first_name}} {{c.last_name}}</option>
                %end
    </select><br/>

    Books: <br/>
        %for b in books:
            &emsp;<input type='checkbox' name='books' value='{{b.id}}'>{{b.title}}<br/>
        %end
    <br/><br/>

    <input type='submit' value='Add' />

</form>
