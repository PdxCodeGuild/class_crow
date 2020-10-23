let randomQuote = new Vue({
    el: '#randomQuote',
    data () {
        return {
            info: null
        }
    },
    mounted () {
        axios 
            .get('https://favqs.com/api/qotd')
            .then(response => (this.info = response.data.quote.body + ' -' + response.data.quote.author)
            )}
})

let quotesHere = new Vue({
    el: '#quotesHere',
    data () {
        return {
            quotes: null,
            query: ''
        }
    },
    methods: {
        update(){
            if (this.query != ''){
                axios
                    .get('https://favqs.com/api/quotes?page="+page_id+"&filter=' + this.query , {
                        headers: {'Authorization': 'Token token="801408f938ee9a9993cb871f0fc7d934"'}
                    })
                    .then(response => (this.quotes = response.data.quotes))
            }
            
        }
    },
    mounted () {
        if (this.query != ''){
            axios
                .get('https://favqs.com/api/quotes?page="+page_id+"&filter=' + this.query , {
                    headers: {'Authorization': 'Token token="801408f938ee9a9993cb871f0fc7d934"'}
                })
                .then(response => (this.quotes = response.data.quotes))
        }
 
    }
   
                 
})