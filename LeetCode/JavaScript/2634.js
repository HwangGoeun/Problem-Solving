/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        const filtering = fn(arr[i], i);
        if (filtering) result.push(arr[i]);
    }

    return result;
};
