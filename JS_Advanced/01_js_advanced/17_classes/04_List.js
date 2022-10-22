class List {
    constructor() {
        this.numList = [];
        this.size = 0;
    }

    add(value) {
        this.numList.push(value);
        this._sortList();
        this.size++;
    };

    remove(index) {
        this._validateIndex(index);
        this.numList.splice(index, 1);
        this._sortList();
        this.size--;
    };

    get(index) {
        this._validateIndex(index);
        return this.numList[index];
    };

    _validateIndex(index) {
        if (index >= this.numList.length || index < 0) {
            throw new Error('Index out of boundaries');
        };
    };

    _sortList() {
        this.numList = this.numList.sort((a, b) => a - b)
    }
}

module.exports = { List };

// let list = new List();
// list.add(5);
// list.add(6);
// list.add(7);
// console.log(list.get(1));
// list.remove(1);
// console.log(list.get(1));
