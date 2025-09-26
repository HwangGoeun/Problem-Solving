/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let maxLength;
    if (word1.length < word2.length) {
        maxLength = word2.length;
    }

    const temp_result = [];
    let str = word1;
    let index = 0;
    for (let i = 0; i < 2; i++) {
        for (const word of str) {
            temp_result[index] = word;
            index += 2;
        }
        str = word2;
        index = 1;
    }
    
    let result = temp_result.filter(function (e) {return e;});
    result = result.join('');

    return result;
};