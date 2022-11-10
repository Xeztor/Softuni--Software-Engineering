function attachEvents() {
    document.getElementById('submit').addEventListener('click', submit)

    const conditionSymbolsEnum = {
        'Sunny': '&#x2600;',
        'Partly sunny': '&#x26C5;',
        'Overcast': '&#x2601;',
        'Rain': '&#x2614;',
    }
    async function submit() {
        document.getElementById('forecast').style.display = 'block';

        const locationsURL = 'http://localhost:3030/jsonstore/forecaster/locations';
        try {
            const response = await fetch(locationsURL);
            if (response.ok === false) {
                throw new Error('');
            };
            const data = await response.json();

            const submittedLocation = document.getElementById('location').value;
            const code = data;
            find: {
                for (let location of data) {
                    if (location.name === submittedLocation) {

                        updateForecast(location.code);
                        break find;
                    };
                };
                throw new Error('location not found')
            };

        } catch (err) {
            onError()
        };
    };

    async function updateForecast(locationCode) {
        todayInfo(locationCode);
        upcomingInfo(locationCode);
    };

    async function todayInfo(code) {
        const url = `http://localhost:3030/jsonstore/forecaster/today/${code}`;
        try {
            const response = await fetch(url);

            if (response.ok === false) {
                throw new Error("Bad response");
            };

            const data = await response.json();

            let conditionSymbol = conditionSymbolsEnum[data.forecast.condition];
            document.getElementById('current').innerHTML +=
                `<div class="forecasts">` +
                `<span class="condition symbol">${conditionSymbol}</span>` +
                `<span class="condition">` +
                `<span class="forecast-data">${data.name}</span>` +
                `<span class="forecast-data">${data.forecast.low}&#176;/${data.forecast.high}&#176;</span>` +
                `<span class="forecast-data">${data.forecast.condition}</span>` +
                `</span>` +
                `</div>`

        } catch (err) {
            onError()
        };
    };

    async function upcomingInfo(code) {
        const url = `http://localhost:3030/jsonstore/forecaster/upcoming/${code}`;
        try {
            const response = await fetch(url);

            if (response.ok === false) {
                throw new Error("Bad response");
            };

            const data = await response.json();

            let div = document.createElement('div')
            div.classList.add('forecast-info');

            for (let forecast of data.forecast) {
                let conditionSymbol = conditionSymbolsEnum[forecast.condition];
                div.innerHTML +=
                    `<span class ="upcoming">` +
                    `<span class="symbol">${conditionSymbol}</span>` +
                    `<span class="forecast-data">${forecast.low}&#176;/${forecast.high}&#176;</span>` +
                    `<span class="forecast-data">${forecast.condition}</span>` +
                    `</span>`;

            };
            document.getElementById('upcoming').appendChild(div);

        } catch (err) {
            onError()
        };
    };

    function onError() {
        document.getElementById('forecast').textContent = 'Error';
    }
}

attachEvents();