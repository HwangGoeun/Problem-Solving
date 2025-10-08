/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {

        for (let i = 0; i < arguments.length; i++) {
            createCounter(n);
        }

        return n++;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
