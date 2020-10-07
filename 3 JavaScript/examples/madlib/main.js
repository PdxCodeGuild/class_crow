let name = document.getElementById('name')
let adjective = document.getElementById('adjective')
let color = document.getElementById('color')
let noun = document.getElementById('noun')
let verb = document.getElementById('verb')

let btn = document.getElementById('createMadLib')
let output = document.getElementById('output')



btn.addEventListener('click', function () {
    let madlib = `
    ${name.value} had a ${adjective.value} day. 
    The sky was ${color.value}. They lost their ${noun.value}. 
    At the ended they had to ${verb.value}. Wow what a day. 

    `
    console.log(madlib)
    output.innerText = madlib
    
})