let button_clock = document.getElementById('button_clock');
let button_stopwatch = document.getElementById('button_stopwatch');
let button_countdown = document.getElementById('button_countdown');

stopwatch_div.style.display = 'none';
clock_div.style.display = 'none';

button_clock.onclick = function() {
    clock_div.style.display = 'block';
    stopwatch_div.style.display = 'none';
    coundown_div.style.display = 'none';
    button_clock.disabled = 'disabled';
    button_countdown.removeAttribute('disabled');
    button_stopwatch.removeAttribute('disabled');
    

}

button_stopwatch.onclick = function(){
    stopwatch_div.style.display = 'block';
    clock_div.style.display = 'none';
    coundown_div.style.display = 'none';
    button_stopwatch.disabled = 'disabled';
    button_countdown.removeAttribute('disabled');
    button_clock.removeAttribute('disabled');
}

function add0(n) {
    return (n<10)? '0' + n: n;
}

function add00(n) {
    return (n < 10)? '00' +n: 
            (n < 100)? '0' + n: n;
}

function get_datetime() {
    console.log('getting date')
    let now = new Date();
    let dd = add0(now.getDate());
    let MM = add0(now.getMonth() + 1);
    let yyyy = now.getFullYear();
    let hh = add0(now.getHours());
    let mm = add0(now.getMinutes());
    let ss = add0(now.getSeconds());
    let ms = add0(now.getMilliseconds());
    let time_str = yyyy + ':' + MM + ':' + dd + ' ' + hh + ':' + mm + ':' + ss + ':' + ms 
    clock_div.innerHTML = time_str;
}

let clock_interval = setInterval(get_datetime, 1000); 

// stopwatch

bt_pause_stopwatch.style.display = 'none';
bt_resume_stopwatch.style.display = 'none';
bt_stop_stopwatch.style.display = 'none';

bt_start_stopwatch.onclick = function() {
    stopwatch_date = new Date();
    stopwatch_date.setHours(0,0,0,0);
    stopwatch_interval = setInterval(update_stopwatch, 1000);
    bt_pause_stopwatch.style.display = 'initial';
    bt_stop_stopwatch.style.display = 'initial';
}

bt_countdownh.onclick = function() {
    coundown_div.style.display = 'block';
    clock_div.style.display = 'none';
    stopwatch_div.style.display = 'none';
    button_countdown.disabled ='disabled';

}

function update_stopwatch() {
    stopwatch_date.setSeconds(stopwatch_date.getSeconds() + 1)
    view_stopwatch.innerHTML = stopwatch_date;
}

bt_stop_stopwatch.onclick = function(){
    clearInterval(stopwatch_interval);
    stopwatch_interval = null;
    stopwatch_date = new Date();
    stopwatch_date.setHours(0,0,0,0);
    view_stopwatch.innerHTML = stopwatch_date;
    bt_resume_stopwatch.style.display = 'none';
    bt_pause_stopwatch.style.display = 'none';
    bt_stop_stopwatch.style.display = 'none';
}

bt_pause_stopwatch.onclick = function(){
    clearInterval(stopwatch_interval);
    stopwatch_interval = null;
    bt_resume_stopwatch.style.display = 'initial';
    bt_pause_stopwatch.style.display = 'none';
}

br_resume_stopwatch.onclick = function(){
    console.log('resume')
    stopwatch_interval = setInterval(update_stopwatch, 1000)
}

//countdown

let view_countdown = document.getElementById('view_countdown')

bt_start_countdown.onclick = function() {
    countdown_date = new Date();
    countdown_date.setHours(0, input_countdown.value, 0, 0);
    countdown_interval = setInterval(update_countdown, 1000);
    view_countdown.innerHTML = countdown_date;
}

function update_countdown() {
    countdown_date.setSeconds(countdown_date.getSeconds() - 1);
    view_countdown.innerHTML = countdown_date;
    
    if(countdown_date){
        clearInterval(countdown_interval);
        countdown_interval = null;
        document.getElementsById('countdown_div').className = 'done';
        
    };
};
