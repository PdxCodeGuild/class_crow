function randomEmoticonGenerator () {
    let eyes = [':', ';', 'B']
    let noses = ['-']
    let mouth = [')', '(', 'D']
    let randomEyes = Math.floor(Math.random() * eyes.length);
    let randomNose = Math.floor(Math.random() * noses.length);
    let randomMouth = Math.floor(Math.random() * mouth.length);
    let face = eyes[randomEyes] + noses[randomNose] + mouth[randomMouth]

    document.write(face)
    return face
}

randomEmoticonGenerator()