let clock = () => {
    let htmlAnchor = document.getElementById('anchor')
    // console.log(htmlAnchor)
    date = new Date()
    hours = date.getHours()
    minutes = date.getMinutes()
    seconds = date.getSeconds()
    ms = date.getMilliseconds()
    time = hours.toString() + ' : ' + minutes.toString() + ' : ' + seconds.toString() + ' : '+ ms.toString()
    htmlAnchor.innerText = time
}

setInterval(clock, 1000)
clicked = true
let interval = 1000
let stopWatch = () => {
    
    console.log(clicked)
    let htmlAnchor = document.getElementById('stop-watch')
    // console.log(htmlAnchor)
    date = new Date()
    // console.log(date)
    zeroedTime = date.setHours(0,0,0,0)
    hours = date.getHours()
    minutes = date.getMinutes()
    seconds = date.getSeconds()
    // ms = date.getMilliseconds()
    
    
    let plsWork = () => {
        let strSeconds = seconds.toString() 
        let strHours = hours.toString()
        let strMinutes = minutes.toString()
        time = strHours + ' : ' + strMinutes + ' : ' + strSeconds
        console.log(time)
        htmlAnchor.innerText = time.toString()
        console.log('whatup')
        seconds += 1}

    let resumeButton = document.getElementById('resume')
    console.log(resumeButton)
    resumeButton.addEventListener('click', function(){
        setInterval(plsWork, 1000)
        console.log('are you alive???')
    })
    // let resumeWatch = () => {
    //      setInterval(plsWork, 1000)
    //     }

    // time = hours.toString() + ' : ' + minutes.toString() + ' : ' + seconds.toString() + ' : '+ ms.toString()

    let xyz = document.querySelector('#plsStop')
    xyz.addEventListener('click', function(){
    clicked = false
    clearInterval(plsWork)
    console.log(clicked)
})

}

// insated of having the main function inside of, use stop and resume buittons that call a fucntion that does the stopwatch thing so maybe like stopwatch is a big function and it never gets called on click. On click, when you click the start button, yo'ull use set interval, call the stopwatch function, and pass it 1000 as the interrval, stop uses clear interval, resume setinterval stopwatch back to 1000