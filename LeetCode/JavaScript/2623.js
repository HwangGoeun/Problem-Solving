// https://leetcode.com/problems/memoize/?envType=study-plan-v2&envId=30-days-of-javascript

function memoize(fn) {
  const cache = {};
  
  return function(...args) {
    const keyName = JSON.stringify(args);

    if (!(keyName in cache)) {
      cache[keyName] = fn(...args);
    };
    
    return cache[keyName];
  }
}
