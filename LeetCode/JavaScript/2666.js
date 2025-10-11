// https://leetcode.com/problems/allow-one-function-call/description/?envType=study-plan-v2&envId=30-days-of-javascript

var once = function(fn) {
  let i = 0;
  
  return function(...args){
    if (i !== 0)    return undefined;

    i++;
    return fn(...args);     
  }
};
