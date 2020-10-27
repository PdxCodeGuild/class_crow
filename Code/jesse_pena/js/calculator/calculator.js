let calculator = new Vue({
    el: '.calculator',
    data:{
        numberString: '',
        formula: '',

    },
    methods: {
        displayNumber: function(num){
            this.numberString += num
            // alert(this.numberString)
            
        },
        sum: function(numberString){
            this.formula += `${numberString} +`
            // alert(this.formula)
            this.numberString = ''
        },
        subtract: function(numberString){
            this.formula += `${numberString} -`
            this.numberString = ''
        },
        divide: function(numberString){
            this.formula += `${numberString} /`
            this.numberString = ''
        },
        multiply: function(numberString){
            this.formula += `${numberString} *`
            this.numberString = ''
        },
        execute: function(formula, numberString){
            let answer = eval(formula + this.numberString)
            alert(answer)
        },
        allClear: function(formula, numberString){
            this.numberString = ''
            this.formula =''
            alert(numberString, formula)
        }
    }
})