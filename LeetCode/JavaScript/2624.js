/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    const result = [];
    
    if (rowsCount === 1) {
        return [nums];
    }
    if (colsCount === 1) {
        for (let i = 0; i < rowsCount; i++) {
            result.push([nums[i]]);
        }
        return result;
    }
    
    if (rowsCount * colsCount > nums.length) {
        return [];
    }
    
    const num = rowsCount + colsCount;
    
    for (let i = 0; i < rowsCount; i++) {
        result.push(new Array(colsCount));
    }
    
    for (let row = 0; row < rowsCount; row++) {
        for (let cols = 0; cols < colsCount; cols++) {
            result[row] = [ nums[row], nums[num - row], nums[num + row + 1], nums[num * 2 + 1 - row] ];
        }
    }
    
    return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */