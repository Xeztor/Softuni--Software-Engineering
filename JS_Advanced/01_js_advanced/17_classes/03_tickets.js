function solve(ticketsArr, criteria) {
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }
    }

    let tickets = [];
    for (let ticketStr of ticketsArr) {
        let [description, price, status] = ticketStr.split('|');
        price = Number(price);
        tickets.push(new Ticket(description, price, status))
    }

    sortTickets(criteria)

    return tickets

    function sortTickets(criteria) {
        if (criteria == 'price') {
            return tickets.sort((a, b) => a.price - b.price);
        };

        return tickets.sort((a, b) => a[criteria].localeCompare(b[criteria]))
    };
}

let test1 = [
    ['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'destination'
]

let test2 = [
    ['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'status'
]

let test3 = [
    ['Philadelphia|100.20|available',
        'New York City|95.99|available',
        'New York City|9.99|sold',
        'Boston|106.20|departed'],
    'price'
]

console.log(solve(...test1));
console.log(solve(...test2));
console.log(solve(...test3));
a = 5