from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "3sdf343sdfksdfhkkjsdfh"
# Sample data (for demonstration purposes)
todos = []


# Route to display all Todos
@app.route('/')
def index():
    return render_template('index.html', todos=todos)


# Route to add a new Todo
@app.route('/add', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        # Generate a unique ID (for demonstration purposes)
        new_id = len(todos) + 1

        # Create a new Todo
        new_todo = {"id": new_id, "name": name, "description": description}

        # Add the new Todo to the list
        todos.append(new_todo)

    return redirect(url_for('index'))


# Route to update a Todo
@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    global todos

    # Find the Todo with the specified id
    todo_to_update = next((todo for todo in todos if todo['id'] == todo_id), None)

    if todo_to_update is None:
        flash('Todo not found', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Update the Todo with the new values
        todo_to_update['name'] = request.form['name']
        todo_to_update['description'] = request.form['description']

        flash('Todo updated successfully', 'success')
        return redirect(url_for('index'))

    return render_template('update.html', todo=todo_to_update)


# Route to delete a Todo
@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos

    # Filter out the Todo with the specified id
    todos = [todo for todo in todos if todo['id'] != todo_id]

    flash('Todo deleted successfully', 'success')
    return redirect(url_for('index'))