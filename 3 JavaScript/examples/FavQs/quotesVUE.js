let app = new Vue({
    el:'#app',
    data: {
        quotes: [],
        filter: ''
    },
    methods: {
        async getQuotes(){
            const api_key = 'd055d363712be70f2cd35ec5f360a528'
            let url = 'https://favqs.com/api/quotes'
        if (this.filter){
            url += `?page="+page_id+"&filter=${this.filter}`
        } else {
            url +=``
        }
        let header_info = {
                headers: {
                    'Authorization': `Token token="${api_key}"`
            }
        }  
        let response = await axios.get(url, header_info)
        this.quotes = response.data.quotes
        }

    }

})






// let quote_btn = document.getElementById('get_quotes');

// function getQuotes(){
//   let user_input = document.getElementById('user_input').value
//   console.log(user_input)
//   user_url = `https://favqs.com/api/quotes?page="+page_id+"&filter=${user_input}`
//   axios.get(user_url, {
//     headers: {
//         'Authorization': `Token token="${myKey}"`
//     }
// })
// .then(response => {
//   quoteContainer = document.getElementById('user-quote-container')
//   quoteContainer.innerHTML = ''
//   data = response.data.quotes
//   console.log(data)
//   newTitle = document.createElement('h1')
//   newTitle.innerText = `${user_input} Quotes`
//   quoteContainer.appendChild(newTitle)
  
//   data.forEach(element => {
//   newDiv1 = document.createElement('div')
//   newDiv1.classList.add('item')
//   newDiv1.innerText = element.body

//   newDiv2 = document.createElement('div')
//   newDiv2.classList.add('item')
//   newDiv2.innerText = element.author

//   quoteContainer.appendChild(newDiv1)
//   quoteContainer.appendChild(newDiv2)  
// })
// })
// };

// quote_btn.addEventListener("click", getQuotes);

// url = 'https://favqs.com/api/quotes'

// axios.get(url, {
//         headers: {
//             'Authorization': `Token token="${myKey}"`
//         }
//   })
//   .then(response => {
//       console.log(response)
//       data = response.data.quotes
//       data.forEach(element => {
//       newDiv1 = document.createElement('div')
//       newDiv1.classList.add('item')
//       newDiv1.innerText = element.body

//       newDiv2 = document.createElement('div')
//       newDiv2.classList.add('item')
//       newDiv2.innerText = element.author

//       quoteContainer = document.getElementById('quote-container')
//       quoteContainer.appendChild(newDiv1)
//       quoteContainer.appendChild(newDiv2)
//       }
//   )})
//   .catch(error => {
//     console.log(error)
//   })

