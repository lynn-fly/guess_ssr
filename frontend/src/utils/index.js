import router from '@/router'

export const gotopPage = (url, query) => {
    router.push({
        path: url,
        query: { data: JSON.stringify(query || {}) },
    });
}