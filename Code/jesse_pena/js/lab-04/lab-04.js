let manipulateDom = () => {
    let toDoList = document.getElementById('to-do')
    let removeBtn = document.createElement('button')
    let content = document.getElementById('userInput').value
    let listItem = document.createElement('li')
    let completeBtn = document.createElement('button')
    let completeList = document.getElementById('done')
  

    listItem.textContent = (content)

    removeBtn.appendChild(document.createTextNode('remove'))
    removeBtn.onclick = function() {
        toDoList.removeChild(removeBtn)
        toDoList.removeChild(listItem)
        toDoList.removeChild(completeBtn)
    }

    completeBtn.appendChild(document.createTextNode('complete'))
    completeBtn.onclick = function() {
        
        toDoList.removeChild(removeBtn)
        toDoList.removeChild(listItem)
        toDoList.removeChild(completeBtn)
        completeList.appendChild(listItem)
    }
    
    toDoList.appendChild(listItem)
    toDoList.appendChild(removeBtn)
    toDoList.appendChild(completeBtn)

}

let clearList = () => {
    let list = document.getElementById('done')
    let child = list.lastElementChild
    while (child) {
        list.removeChild(child)
        child = list.lastElementChild
    }
}
