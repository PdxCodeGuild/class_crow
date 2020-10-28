let calculator = new Vue({
    el: '.calculator',
    data:{
        numberString: '',
        formula: '',
        displayValue: ''
        

    },
    methods: {
        displayNumber: function(num){
            this.numberString += num
            // alert(this.numberString)
            this.displayValue += num
            
        },
        addDecimal: function(){
            this.numberString += '.'
            this.displayValue += '.'

        },
        sum: function(numberString){
            this.formula += `${numberString} +`
            // alert(this.formula)
            this.numberString = ''
            this.displayValue = ''
        },
        subtract: function(numberString){
            this.formula += `${numberString} -`
            this.numberString = ''
            this.displayValue = ''
        },
        divide: function(numberString){
            this.formula += `${numberString} /`
            this.numberString = ''
            this.displayValue = ''
        },
        multiply: function(numberString){
            this.formula += `${numberString} *`
            this.numberString = ''
            this.displayValue = ''
        },
        execute: function(formula){
            let answer = eval(formula + this.numberString)
            this.formula = ''
            this.displayValue = answer
            this.numberString = this.displayValue
            
            // alert(answer)
        },
        allClear: function(){
            this.numberString = ''
            this.formula = ''
            this.displayValue = ''
            // alert(numberString, formula)
        }
    }
})