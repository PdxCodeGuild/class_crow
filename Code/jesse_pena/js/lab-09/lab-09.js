let randomQuote = () => {
    fetch("https://favqs.com/api/qotd")
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let quote = data.quote.body;
            console.log(data.quote.body);
            console.log(data.quote.author)
            document.write(`${quote} --- ${data.quote.author}`);
            
        });
    }

// reference: https://gist.github.com/prameshbajra/2196fc4071604e37d842148956b18aa9

// reference: https://forum.freecodecamp.org/t/fetch-api-with-api-key/317584

// let apiKey = process.env.API_KEY

function httpGet() {
    // let apiKey = process.env.LAB_9_API_KEY
    let anchor = document.getElementById('quotesHere')
    let query = document.getElementById('userInput').value
    console.log(query)
    // console.log(`https://favqs.com/api/quotes?page="+page_id+"&filter=${query}`)
    // let url = `https://favqs.com/api/quotes?page="+page_id+"&filter=${query}`
    let url = 'https://favqs.com/api/quotes?page="+page_id+"&filter=' + query
    console.log(url)
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="801408f938ee9a9993cb871f0fc7d934"')
            // xhttp.setRequestHeader(`'Authorization', 'Token token="${apiKey}"'`)
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            // success(data);
            console.log(data.quotes)
            let listQuotes = data.quotes
            console.log(listQuotes[1])
            // document.write(listQuotes[1].body)
            // console.log(listQuotes.length)
            for (i = 0; i < listQuotes.length; i++) {
                document.write(listQuotes[i].body)
                document.write('<br>')
                document.write(`---${listQuotes[i].author}`)
                document.write("<br>")
                document.write('*****************************************************************************')
                document.write("<br>")
                
            }


        } else if (this.readyState === 4 && this.status === 404) {
            // handle 404
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}