const host = 'http://localhost:3030'

async function request(method, url, body) {
    const options = {
        method,
        headers: {},
    }

    if (body !== undefined) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(body);
    };

    const token = localStorage.getItem('accessToken')
    if (token) {
        options.headers['X-Authorization'] = token;
    };

    try {
        const response = await fetch(host + url, options);

        if (response.ok === false) {
            throw new Error('Bad Response');
        };

        if (response.status == 204) {
            return;
        }

        return await response.json()
    } catch (err) {
        console.log(err);
        throw err;
    }

}

export const get = request.bind(null, 'get');
export const post = request.bind(null, 'post');
export const put = request.bind(null, 'put');
export const del = request.bind(null, 'delete');