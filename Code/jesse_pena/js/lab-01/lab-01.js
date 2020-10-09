function grading (score) {
    let grade = ''
    if (score >= 90){
        grade ='A'
    } else if (score >= 80){
        grade = 'B'
    } else if (score >= 70){
        grade = 'C'
    } else if (score >= 60){
        grade ='D'
    } else {
        grade = 'F'
    }
    return grade
}

function plusMinus (score) {
    let modulus = score % 10
    if (modulus >= 8) {
        symbol = '+'
    } else if (modulus >= 3) {
        symbol = ''
    } else if (modulus < 3) {
        symbol = '-'
    }
    return symbol
}


function totalGrade (grade, symbol) {
    if (grade != 'F') {
        console.log(grade + symbol)
        return grade + symbol
    } else {
        console.log(grade)
        return grade
    }
}

totalGrade(grading(69), plusMinus(69))