let manipulateDom = () => {
    let toDoList = document.getElementById('to-do')
    let removeBtn = document.createElement('button')

    content = document.getElementById('userInput').value
    listItem = document.createElement('li')
    listItem.class = 'list-item'
    listItem.textContent = (content)

    removeBtn.appendChild(document.createTextNode('remove'))
    removeBtn.onclick = function() {
        toDoList.removeChild(listItem)
        toDoList.removeChild(removeBtn)
        
    }

    toDoList.appendChild(listItem)
    toDoList.appendChild(removeBtn)
}
