/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {

    return {
      toBe: function(arg) {
          if (val === arg) {
              return true;
          } else {
              throw new Error('Not Equal');
              return false;
          }
      },
    
        notToBe: function(arg) {
          if (val !== arg) {
              return true;
          } else {
              throw new Error('Equal');
              return false;
          }
      }     
  };
};

/**
* expect(5).toBe(5); // true
* expect(5).notToBe(5); // throws "Equal"
*/
