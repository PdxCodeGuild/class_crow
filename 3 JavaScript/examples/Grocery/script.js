//submit function creates new div, sets innertext to input value, appends to parent div
let submit = () => {
    let parentDiv = document.querySelector('.item-list')

    let newDiv = document.createElement('div')
    newDiv.className = "item"
    let item = newDiv.innerText = document.querySelector('.item-input').value
    document.querySelector('.item-list').append(newDiv)

    //add remove button
    let remove = document.createElement('button')
    remove.setAttribute('type', 'button');
    remove.setAttribute("value", "Remove");
    remove.setAttribute("id", "removeButton");
    remove.innerText = "X"

    
    newDiv.appendChild(remove);
    //remove items
    remove.addEventListener('click', function(event) {
        console.log('clicked')
        parentDiv.removeChild(newDiv)
    })
}

//calls the submit function on click
document.querySelector('.item-submit').addEventListener('click', () => {
    submit();
})

//allow the user to use the enter key to submit 
document.querySelector('.item-submit').addEventListener('keyup', (event) => {
    if (event.key === 13) {
        submit();
        console.log('enter hit')
    }
})
//clear all items from list 
document.querySelector('.list-clear').addEventListener('click', () => {
    let parentDiv = document.querySelector('.item-list')
    let items = document.querySelectorAll('.item')
    console.log(items)
    for (let i=0; i < items.length; i++){
        let child = items[i];
        parentDiv.removeChild(child)
    }
})