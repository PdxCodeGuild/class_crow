


var app = new Vue({
    el: '#app',
    data: [],
    methods: {
        getToDos: function(){
            axios.get('http://localhost:8000/api/')
            .then(function(response){
            console.log(response)
            
            });
        }
    }
})