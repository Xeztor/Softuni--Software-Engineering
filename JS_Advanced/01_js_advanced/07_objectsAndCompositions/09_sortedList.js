function createSortedList() {
    return {
        size: 0,
        numbers: [],
        add(num) {
            this.numbers.push(num);
            this.numbers.sort((a, b) => a - b);
            this.size++;
        },
        remove(index) {
            this.checkIndexExist(index);
            this.numbers.splice(index, 1)
            this.size--;
        },
        get(index) {
            this.checkIndexExist(index);
            return this.numbers[index];
        },
        checkIndexExist(index) {
            if (index < 0 || index > this.numbers.length - 1) {
                throw '';
            };
        }
    };
}

// let list = createSortedList();
// list.add(5);
// list.add(6);
// list.add(7);
// console.log(list.get(1));
// list.remove(1);
// console.log(list.get(1));
