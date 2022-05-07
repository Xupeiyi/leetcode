/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let sum = 0;
    let start = 0;
    const length = nums.length;
    for (let end = 0; end < length; end++){
        sum += nums[end];
        if (sum + k < end - start + 1){
            sum -= nums[start];
            start++;
        }
    } 
    return length - start;
};