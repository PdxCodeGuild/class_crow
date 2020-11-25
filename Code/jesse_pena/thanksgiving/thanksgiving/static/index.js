var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        foods : [],
        input_food_name: '',
        input_food_rating: '',
        newFood: ''
    },
    mounted: async function(event){
        let response = await axios.get('http://localhost:8000/api/');
        this.foods = response.data;
        this.string = 'STRING';
    },
    methods: {
        getFoods: async function(event){
            let response = await axios.get('http://localhost:8000/api/');
            this.foods = response.data;
            this.string = 'STRING';
        },
        addFood: function(){
            const newFood = {
                'name': this.input_food_name,
                'rating': this.input_food_rating
            }
            this.foods.push(newFood)
            const config = {headers: {
                'Content-Type': 'application/json',
                'xsrfHeaderName': 'X-CSRFToken'
            }}
            axios.post('http:localhost:8000/api/', newFood)
            .then(response => this.newFood = response.data)
            .catch(error => {
                this.errorMessage = error.message;
                console.log('ERROR', error)
            })
        }
    }
})

alert('REEEEE')