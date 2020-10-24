
# Lab 12: Vue Todos

Make a todo app using Vue.js.

Use Vue to create a simple todo list in the browser.

Your Vue app will need to do a few things:
 * Store an array of objects (the todos themselves)
 * List each todo
 * Allow the user to add and remove todos
 * Allow a user to toggle if a task is complete or not
 
 Reference the Vue.js [Introduction Guide](https://vuejs.org/v2/guide/).

## How to get started

* Create a simple local HTML project with the following structure:
```
todos
├── css
│   └── site.css
├── index.html
└── js
    └── site.js`
```

## How to serve your application

* Install this plug-in for VSCode: `https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer`
* Make sure VSCode is open to the same folder as your `index.html`
* On the bottom bar in VSCode you should see an icon that says `Go Live`
* Click it and you're serving up a local version of your html file. It also auto-reloads everytime you make a change, neat right?

## How to structure your `index.html`

Example: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Todo List</title>
    <!-- Add your styles here! -->
    <link rel="stylesheet" href="/css/site.css" />    
 <!-- Include Vue from a CDN of your choice, I chose unpkg -->
    <script src="https://unpkg.com/vue"></script>
</head>
<body>
    <div id="app">
        {{ message }}
    </div>


    <!-- Include your code here... -->
    <script src="/js/site.js"></script>
</body>
</html>
```

### How to start a simple Vue app:
```js
new Vue({
    el: '#app',
    data: {
        message: 'Hello world!'
    }
})
```
Complete todos.js and todos.html to get the functionality of the in class demo.

In todos.js:
```js
addTodo: function() {
    // add todo to the front of this.todos
},
removeTodo: function(index) {
    // remove todo from this.todos
},
markDone: function(index) {
    // mark todo as completed and move todo the the end of todos
}
```
In todos.html:
- You'll need to modify your `<input>` to handle `addTodo()`.
- The bulk of your work will be on between `<li></li>`. This is your representation of each todo.
- Hint: you want to loop through your todos and represent each todo as a `<li>`
- At the end of each `<li>`, you'll want buttons/links/icons that onclick will handle `markDone()` and `removeTodo()` respectively.
- Hint: notice how in todos.js, the code stubs for `markDone(index)` and `removeTodo(index)` take **index** as an argument.
- Style completed todos with a strikethrough and different coloring.

## Version 2
Next, allow markDone to toggle. Show a markDone button/link/icon if the todo is not completed, else show an undo button/link/icon if the todo *is* completed. 

In todos.js:
```js
markDone: function(index) {
    // toggle todo.completed
    // if completed: move todo to the front of todos
    // else: move todo to the end of todos
}
```
In todos.html:
- Use Vue logic (hint: v-if, v-else) to progmatically display a button depending if the todo is marked completed.
