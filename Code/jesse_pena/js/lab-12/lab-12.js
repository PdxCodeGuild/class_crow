let toDoList = new Vue({
    el: '#toDoList',
    data: {
        itemList: [
            
        ],
        completedList: [
        ],
        addToList: '',
        strikeThrough: 'line-through'
        
    },
    methods: {
        addToDo: function(){
            this.itemList.push(this.addToList)
        },
        removeToDo: function(item){
            this.itemList.splice(this.itemList.indexOf(item), 1)
            // reference: https://stackoverflow.com/a/42845755/14263621
        },
        markDone: function(item){
            let completeItem = this.itemList.splice(this.itemList.indexOf(item), 1)
            this.completedList.push(completeItem[0])
        },
        removeComplete: function(item){
            this.completedList.splice(this.completedList.indexOf(item), 1)
        },
        notDone: function(item){
            let notDoneItem = this.completedList.splice(this.completedList.indexOf(item), 1)
            this.itemList.push(notDoneItem[0])
        }
    }
    
})