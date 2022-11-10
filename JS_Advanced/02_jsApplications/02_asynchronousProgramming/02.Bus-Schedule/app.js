function solve() {

    function depart() {
        document.getElementById('depart').disabled = true;
        document.getElementById('arrive').disabled = false;

        let data = getData(getNextStop())

    }

    async function getData(stopId) {
        try {
            const response = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${stopId}`);

            if (response.ok == false) {
                onError();
            };

            const data = await response.json();
            updateInfoBox(`Next stop ${data.name}`)
            document.getElementsByClassName('info')[0].dataset.nextstopid = data.next;

        } catch (err) {
            onError();
        };
    };



    function arrive() {
        let busStopName = document.getElementsByClassName('info')[0].textContent.split(' ')[2];
        updateInfoBox(`Arriving at ${busStopName}`)

        document.getElementById('depart').disabled = false;
        document.getElementById('arrive').disabled = true;
    };

    return {
        depart,
        arrive
    };

    function onError() {
        updateInfoBox('Error')
        document.getElementById('depart').disabled = true;
        document.getElementById('depart').disabled = true;
    }

    function getNextStop() {
        if (document.getElementsByClassName('info')[0].textContent === "Not Connected") {
            document.getElementsByClassName('info')[0].dataset.nextstopid = 'depot';
        };

        return document.getElementsByClassName('info')[0].dataset.nextstopid;
    };

    function updateInfoBox(text) {
        document.getElementsByClassName('info')[0].textContent = text;
    };
}

let result = solve();