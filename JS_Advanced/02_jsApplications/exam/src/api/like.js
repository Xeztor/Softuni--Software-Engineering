import { get, post } from "./api.js"

const endpoints = {
    like: '/data/likes',
    likesCount(albumId) { return `/data/likes?where=albumId%3D%22${albumId}%22&distinct=_ownerId&count` },
    userLiked(userId, albumId) { return `/data/likes?where=albumId%3D%22${albumId}%22%20and%20_ownerId%3D%22${userId}%22&count` },
}

export async function likeAlbum(albumId) {
    await post(endpoints.like, { albumId });
}

export async function albumLikes(id) {
    return await get(endpoints.likesCount(id));
}
export async function hasUserLiked(userId, albumId) {
    return await get(endpoints.userLiked(userId, albumId));
}