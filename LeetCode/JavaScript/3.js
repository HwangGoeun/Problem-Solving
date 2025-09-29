/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let result = 0;
    let currSubLength = 0;
    let subCharList = [];
    
    for (let i = 0; i < s.length; i++) {
        const currChar = JSON.stringify(s[i]);
        
        if (subCharList.includes(currChar)) {
            const startIdx = subCharList.indexOf(currChar);
            subCharList = subCharList.slice(startIdx + 1);
            subCharList.push(currChar);
        } else {
            subCharList.push(currChar);
        }
        
        result = (result < subCharList.length) ? subCharList.length : result;
    }
    
    return result;
};