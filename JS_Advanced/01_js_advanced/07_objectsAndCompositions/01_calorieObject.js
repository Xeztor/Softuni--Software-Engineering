function createObj(arr){
    let obj = {};
    for (i = 0; i < arr.length; i += 2){
        obj[arr[i]] = Number(arr[i+1]);
    }
    console.log(obj);
}