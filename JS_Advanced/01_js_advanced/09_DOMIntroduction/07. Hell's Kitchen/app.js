function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
      let input = document.querySelector("#inputs textarea").value;
      input = input.substring(1, input.length - 2);

      let bestRestaurant = getBestRestaurant(input);
      let restaurantName = Object.keys(bestRestaurant)[0];
      let restaurantInfo = Object.values(bestRestaurant)[0];

      let bestRestaurantP = document.querySelector("#bestRestaurant p");
      let workersP = document.querySelector("#workers p");

      bestRestaurantP.textContent = `Name: ${restaurantName} Average Salary: ${restaurantInfo["avgSalary"]} Best Salary: ${restaurantInfo["bestSalary"]}`;
      let workersStrings = Object.entries(restaurantInfo["workers"]).map(worker => `Name: ${worker[0]} With Salary: ${worker[1]}`);

      workersP.textContent = workersStrings.join(' ');


      function getBestRestaurant(input) {
         let restaurants = {};

         let restaurantsInput = input.split('","').map(string => string.replace("\"", ''));

         for (let input of restaurantsInput) {
            let [restaurantName, workersList] = input.split(' - ');
            let workersStrings = workersList.split(', ');

            if (!(restaurantName in restaurants)) {
               restaurants[restaurantName] = {
                  "workers": {},
                  "avgSalary": 0,
                  "bestSalary": 0,
               };
            };

            let currentRestaurant = restaurants[restaurantName];

            addWorkersToRestaurant(workersStrings, currentRestaurant)
            sortWorkersBySalary(currentRestaurant);
            setBestSalary(currentRestaurant);
            setAvgSalary(currentRestaurant);
         };

         let restaurantsEntries = Object.entries(restaurants);
         restaurantsEntries.sort((a, b) => b[1]["avgSalary"] - a[1]["avgSalary"]);
         let bestRestaurant = [restaurantsEntries[0]];

         return Object.fromEntries(bestRestaurant);
      }

      function addWorkersToRestaurant(workersStrings, currentRestaurant) {
         for (let worker of workersStrings) {
            let [workerName, salary] = worker.split(' ');
            salary = Number(salary);
            currentRestaurant['workers'][workerName] = salary;
         };
      }

      function setAvgSalary(currentRestaurant) {
         let salariesSum = Object.entries(currentRestaurant["workers"])
            .map((el, i) => el[1])
            .reduce((acc, el) => acc += el, 0);
         currentRestaurant["avgSalary"] = (salariesSum / Object.keys(currentRestaurant["workers"]).length).toFixed(2);
      }

      function setBestSalary(currentRestaurant) {
         currentRestaurant["bestSalary"] = Object.values(currentRestaurant["workers"])[0].toFixed(2);
      }
      function sortWorkersBySalary(currentRestaurant) {
         let sortedWorkersEntries = Object.entries(currentRestaurant["workers"]).sort((a, b) => b[1] - a[1]);
         currentRestaurant["workers"] = Object.fromEntries(sortedWorkersEntries);
      }

   }
}