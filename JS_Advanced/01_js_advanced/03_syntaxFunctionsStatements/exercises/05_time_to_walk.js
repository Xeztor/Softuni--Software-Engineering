function calculateTime(footsteps, lengthOfSteps, speed) {
    let distance = lengthOfSteps * footsteps;
    
    let speedInMperSec = (speed * 1000) / 3600;
    let travelTimeInSec = Number((distance / speedInMperSec).toFixed(0));

    let restTime = Math.floor(distance / 500);
    restTime *= 60;

    travelTimeInSec += restTime;
    let seconds = Math.floor(travelTimeInSec % 60);
    let minutes = Math.floor(travelTimeInSec / 60);
    let hours = Math.floor(minutes / 60);
    if (minutes >= 60){
        hours = Math.ceil(minutes / 60);
        minutes = minutes % 60;
    }
    
    seconds = formatTime(seconds)
    minutes = formatTime(minutes)
    hours = formatTime(hours)

    console.log(`${hours}:${minutes}:${seconds}`)

    function formatTime(number){
        if (number < 10){
            return `0${number}`
        }

        return String(number)
    }
}

// calculateTime(13, 0.60, 5)
// calculateTime(2564, 0.70,    5.5)