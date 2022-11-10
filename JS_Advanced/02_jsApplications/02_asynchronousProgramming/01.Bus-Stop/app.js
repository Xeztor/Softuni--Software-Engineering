function getInfo() {
    let busId = document.getElementById('stopId').value;

    getData(busId)
    async function getData(busId) {
        clearUl()
        try {
            const response = await fetch(`http://localhost:3030/jsonstore/bus/businfo/${busId}`);

            if (response.ok == false) {
                changeStopName('Error');
            };

            const data = await response.json();

            changeStopName(data.name);
            changeBusesList(data.buses);
            
        } catch (err) {
            changeStopName('Error');
        }
    }

    function changeBusesList(busesObj) {
        let list = document.getElementById("buses");
        for (busId in busesObj) {
            let listItem = document.createElement('li');
            listItem.textContent = `Bus ${busId} arrives in ${busesObj[busId]} minutes`

            list.appendChild(listItem)
        }
    };

    function changeStopName(name) {
        document.getElementById('stopName').textContent = name;
    };

    function clearUl() {
        let parent = document.getElementById('buses');
        while (parent.firstChild) {
            parent.removeChild(parent.firstChild);
        }
    }
}