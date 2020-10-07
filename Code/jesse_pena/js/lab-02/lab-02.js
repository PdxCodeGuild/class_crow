function eightBall () {
    alert('welcome to the magic 8 ball!')
    choices = ['It is certain', 'It is decidedly so', 'Reply hazy try again', 'Concentrate and ask again', 'My sources say no', 'Very doubtful']
    prompt('What is your question?')
    let index = Math.floor(Math.random() * choices.length);
    return choices[index];

    
}

alert(eightBall())