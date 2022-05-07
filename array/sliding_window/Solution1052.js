/**
 * @param {number[]} customers
 * @param {number[]} grumpy
 * @param {number} minutes
 * @return {number}
 */
var maxSatisfied = function(customers, grumpy, minutes) {
    let base = 0;
    for (let i = 0; i < customers.length; i++){
        base += (1 - grumpy[i]) * customers[i];
    }

    let start = 0;
    let extra = 0;
    let maxExtra = 0;
    for (let end = 0; end < customers.length; end++){
        extra += grumpy[end] * customers[end];
        maxExtra = Math.max(maxExtra, extra);
        if (end - start + 1 == minutes){
            extra -= grumpy[start] * customers[start];
            start++;
        }
    }
    return base + maxExtra;
};

let ans = maxSatisfied([2, 6, 6, 9], [0, 0, 1, 1], 1);
console.log(ans);