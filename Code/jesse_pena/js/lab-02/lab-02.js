function eightBall () {
    question = ''
    while (question != 'end') {
        alert('welcome to the magic 8 ball!');
        choices = ['It is certain', 'It is decidedly so', 'Reply hazy try again', 'Concentrate and ask again', 'My sources say no', 'Very doubtful'];
        question = prompt('What is your question? Type end to terminate');
        let index = Math.floor(Math.random() * choices.length);
        alert(choices[index]);
        
    };
    return choices[index]
    
};

alert(eightBall());