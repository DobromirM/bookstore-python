% rebase('base.tpl')

<h1>Edit Order</h1>

<form action='/orders/{{order.id}}/edit' method='post'>

    Customer: <select name='customer' value='{{order.customer.id}}'>
                    %for c in customers:

                        % if c.id == order.customer.id:
                            <option value='{{c.id}}' selected>{{c.first_name}} {{c.last_name}}</option>
                        % else:
                            <option value='{{c.id}}'>{{c.first_name}} {{c.last_name}}</option>
                        % end

                    %end
    </select><br/>

    Purchase Date: <input type='date' name='date' value='{{order.purchase_date}}' required /><br/>

    Books: <br/>
            %for b in books:

                % if b.id in order.books.id:
                    &emsp;<input type='checkbox' name='books' value='{{b.id}}' checked>{{b.title}}<br/>
                % else:
                    &emsp;<input type='checkbox' name='books' value='{{b.id}}'>{{b.title}}<br/>
                % end

            %end
    <br/><br/>

    <input type='submit' value='Save' />

</form>
