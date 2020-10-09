let manipulateDom = () => {
    let container = document.getElementsByClassName('container')
    let toDoList = document.getElementById('to-do')
    let removeBtn = document.createElement('button')

    content = document.getElementById('userInput').value
    listItem = document.createElement('li')
    listItem.className = 'list-item'
    listItem.textContent = (content)

    removeBtn.appendChild(document.createTextNode('remove'))

    removeBtn.onclick = function() {
        toDoList.removeChild(removeBtn)
        toDoList.removeChild(listItem)
    }
    
    toDoList.appendChild(listItem)
    toDoList.appendChild(removeBtn)


    
}
