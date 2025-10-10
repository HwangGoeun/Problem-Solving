// https://leetcode.com/problems/function-composition/?envType=study-plan-v2&envId=30-days-of-javascript

var compose = function(functions) {
	return function (x) {
		if (functions.length === 0) return x;
		
		if (functions.length === 1) return functions[0](x);
		
		return functions[0]( compose( functions.slice(1) )(x) );
	}
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
