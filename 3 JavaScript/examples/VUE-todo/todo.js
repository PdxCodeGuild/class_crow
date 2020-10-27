var app = new Vue({
    el: '#app',
    data: {
        todo: '',
        todos: []
    },
    methods: {
        addNewTodo: function() {
            let todo = {
                title: this.todo,
                completed: false,
                editable: false
            }
            this.todos.push(todo);
        },
        removeTodo: function(index) {
            this.todos.splice(index, 1);
        },
    }
});