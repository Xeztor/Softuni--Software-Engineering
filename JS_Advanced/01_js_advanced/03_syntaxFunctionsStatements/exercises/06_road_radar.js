function radar(speed, area){
    let mapper = {
        'residential': 20,
        'city': 50,
        'interstate': 90,
        'motorway': 130,
    };

    let speedLim = mapper[area];

    if (speed > speedLim){
        let [exceedingSpeed, status] = getSpeedInfo(speed, speedLim)
        console.log(`The speed is ${exceedingSpeed} km/h faster than the allowed speed of ${speedLim} - ${status}`);
        return
    }

    console.log(`Driving ${speed} km/h in a ${speedLim} zone`);

    function getSpeedInfo(speed, speedLimit){
        let exceedingSpeed = speed - speedLimit;
        let status;
        if (exceedingSpeed <= 20){
            status = 'speeding';
        } else if (exceedingSpeed <= 40) {
            status = 'excessive speeding';
        } else {
            status = 'reckless driving';
        }
        return [exceedingSpeed, status];
    }
}

// radar(40, 'city')
// radar(21, 'residential')
// radar(120, 'interstate')
// radar(200, 'motorway')