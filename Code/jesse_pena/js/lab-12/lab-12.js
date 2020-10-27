let toDoList = new Vue({
    el: '#toDoList',
    data: {
        itemList: [
            
        ],
        addToList: '',
        isComplete: true
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
            this.itemList.push(completeItem[0])
        },
    }
    
})