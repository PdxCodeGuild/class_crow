let randomPage = () => {
    let countdown = document.getElementById('htmlDiv')
    // countdown.appendChild(document.createTextNode('remove'))
    console.log(countdown)
    let urls = ['https://www.seahawks.com/',
                'https://developer.mozilla.org/en-US/docs/Web/API/Window/location',
                'https://na.op.gg/'
    ]

    let randomUrl = Math.floor(Math.random(urls)*urls.length)
    console.log('randomUrl', urls[randomUrl])
    counter = 5
    countdown.innerText = counter;
    setInterval(function() {
        console.log('counter', counter)
        // alert(counter)
        countdown.innerText = counter;
        if (counter === 0) {
            window.location = urls[randomUrl]
        }
        counter -= 1;
    }, 1000)
    
    
    
}

