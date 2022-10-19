function validate(reqObj) {
    const methods = ["GET", "POST", "DELETE", "CONNECT"];
    const versions = ["HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/2.0"];

    const uriRegExp = new RegExp(/^[a-zA-Z01234567890.]+$|\*/);
    const messageRegExpTest = new RegExp(/[<>\\'"]/);

    if (!reqObj.hasOwnProperty("method") || !methods.includes(reqObj.method)) {
        throw new Error("Invalid request header: Invalid Method");
    };

    if (!reqObj.hasOwnProperty("uri") || !uriRegExp.test(reqObj.uri)) {
        throw new Error("Invalid request header: Invalid URI");
    }

    if (!reqObj.hasOwnProperty("version") || !versions.includes(reqObj.version)) {
        throw new Error("Invalid request header: Invalid Version");
    };

    if (!reqObj.hasOwnProperty("message") || messageRegExpTest.test(reqObj.message)) {
        throw new Error("Invalid request header: Invalid Message")
    };

    return reqObj

}
//
let test1 = {
    method: 'GET',
    uri: '*',
    version: 'HTTP/1.1',
    message: ''
};
let test2 = {
    method: 'OPTIONS',
    uri: 'git.master',
    version: 'HTTP/1.1',
    message: '-recursive'
};
let test3 = {
    method: 'POST',
    uri: 'home.bash',
    version: 'HTTP/2.0'
};


let test1Result = validate(test1);
console.log(test1)

// let test2Result = validate(test2);
// let test3Result = validate(test3);