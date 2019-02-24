% rebase('base.tpl')

<h1>Edit Book</h1>

<form action='/books/{{book.id}}/edit' method='post'>

    Title: <input type='text' name='title' value='{{book.title}}' required /><br/>

    Author: <select name='author'>
                    %for a in authors:
                        <option value='{{a.id}}'>{{a.first_name}} {{a.last_name}}</option>
                    %end
    </select><br/>

    Publisher: <select name='publisher'>
                        %for p in publishers:
                            <option value='{{p.id}}'>{{p.name}}</option>
                        %end
    </select><br/>

    Genre: <select name='genre'>
                            %for g in genres:
                                <option value='{{g.id}}'>{{g.name}}</option>
                            %end
    </select><br/>

    Year: <input type='date' name='year' value='{{book.year}}' required /><br/>

    Price: <input type='number' step='0.01' name='price' value='{{book.price}}' min="0" required /><br/><br/>

    <input type='submit' value='Save' />

</form>
