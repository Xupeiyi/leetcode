/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function(arr) {
    if (arr.length <= 1){
        return arr.length;
    }

    diffs = [];
    for (let i = 1; i < arr.length; i++){
        diffs.push(arr[i] - arr[i-1]);
    }

    // start should never point at 0
    let start = 0;
    while (start < diffs.length && diffs[start] == 0){
        start++;
    }
    if (start == diffs.length){
        return 1;
    }

    let maxLength = 1;
    for (let end = start + 1; end < diffs.length; end++){
        if (diffs[end] * diffs[end-1] >= 0){
            maxLength = Math.max(maxLength, end-start);
            start = end;
            
            // skip zeros
            while (start < diffs.length && diffs[start] == 0){
                start++;
                end++;
            }
        }
    }

    return Math.max(maxLength, diffs.length-start) + 1;
};

let a = [9,4,2,10,7,8,8, 8,1,9, 9, 9];
let ans = maxTurbulenceSize(a); 
console.log(ans);