const host = 'http://localhost:3030'

async function request(method, url, body) {
    const options = {
        method,
        headers: {},
    }
    if (body !== undefined) {
        options.headers['content-type'] = 'application/json';
        options.body = JSON.stringify(body);
    };

    const response = await fetch(host + url, options);
    const data = await response.json();

    return data;
}

export const get = request.bind(null, 'get');
export const post = request.bind(null, 'post');
export const put = request.bind(null, 'put');
export const del = request.bind(null, 'delete');