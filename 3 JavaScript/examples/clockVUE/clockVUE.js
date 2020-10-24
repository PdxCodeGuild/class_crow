let app = new Vue({
    el: '#app',
    data: {
        clock: true,
        stopWatch: false,
        hours: 0, 
        minutes: 0, 
				seconds: 0, 
				stopHours: 0,
				stopMinutes: 0, 
				stopSeconds: 0, 
				stopMili: 0, 
				stpInterval: null
    },
    methods: {
        showClock: function(){
            this.clock = true
            this.stopWatch = false
        },
        showStopWatch: function(){
            this.clock = false
            this.stopWatch = true
        },
        keepTime: function(){
						this.clockInterval = 1000
            setInterval(() => {						
						this.seconds ++
						if (this.seconds >= 60){
							this.seconds = 0
							this.minutes ++
						}
						if (this.minutes >= 60){
								this.minutes = 0
								this.hours ++
							}
            }, 1000)
				},
				getTime: function(){
					let date = new Date()
					this.hours = date.getHours()
					this.minutes = date.getMinutes()
					this.seconds = date.getSeconds()
					this.keepTime()
				},
				timeString: function(number){
					this.getTime()
					return number.toString()
				},
		// 		startStopWatch: function(){
		// 			if(this.stopclockInterval) return
		// 			this.stopclockInterval = keepTime()		
		// 		},
		// 		stopStopWatch: function(){
		// 			clearInterval(this.clockInterval)
		// 			this.clockInterval = null
		// 		}
				startStopWatch: function(){
					// if(this.stpInterval) return 
						setInterval(() =>{
						// this.stpInterval = true
						this.stopMili ++
						// if(this.stopMili > 999){
						// 	this.stopMili = 0
						// 	this.stopSeconds++
						// }
					}, 1)
				}

				
    }
})