/* 
•	If one of the passed parameters is an empty string (""), undefined or null, this function should throw an error
        with the following message: "Invalid input!"
•	If salary is less than 0, this function should throw an error with the following message: "Invalid input!"
•	If the new employee is hired successfully, you should add him into the departments object 
        with the current name of the department and return the following message: `New employee is hired. Name: {name}. Position: {position}`

*/

class Company {
    constructor() {
        this.departments = {};
    };

    addEmployee(name, salary, position, department) {
        if (!name || typeof (salary) !== 'number' || salary < 0 || !position || !department) {
            throw new Error("Invalid input!");
        }

        if (this.departments.hasOwnProperty(department) === false) {
            this.departments[department] = [];
        };

        this.departments[department].push({
            name,
            salary,
            position
        });

        return `New employee is hired. Name: ${name}. Position: ${position}`;
    };

    bestDepartment() {
        let [department, bestAvgSalary] = this._bestAvgSalary();

        let sortedWorkers = this.departments[department]
            .sort((a, b) => b.salary - a.salary || a['name'].localeCompare(b['name']));

        let outputStr = `Best Department is: ${department}\nAverage salary: ${bestAvgSalary}\n`;
        let sortedWorkersStrings = sortedWorkers.map(worker => `${worker.name} ${worker.salary} ${worker.position}`);

        outputStr += sortedWorkersStrings.join('\n');
        return outputStr;
    };

    _bestAvgSalary() {
        let bestDepartment = '';
        let bestSalary = 0;
        for (let department in this.departments) {
            let salariesSum = this.departments[department].reduce((acc, worker) => acc + worker.salary, 0);
            let avgSalary = (salariesSum / this.departments[department].length).toFixed(2);
            if (avgSalary > bestSalary) {
                bestSalary = avgSalary;
                bestDepartment = department;
            }
        };

        return [bestDepartment, bestSalary]
    }
}



let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());

