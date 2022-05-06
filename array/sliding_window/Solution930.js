/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function(nums, goal) {
    let ans = 0;
    let start1 = 0;
    let start2 = 0;
    let sum1 = 0;
    let sum2 = 0;
    const n = nums.length;
    for (let end = 0; end < n; end++){
        sum1 += nums[end];
        sum2 += nums[end];
        while ((start1 <= end) && (sum1 > goal)) sum1 -= nums[start1++];
        while ((start2 <= end) && (sum2 >= goal)) sum2 -= nums[start2++];
        ans += (start2 - start1);
    }
    return ans;
};

var ans = numSubarraysWithSum([0, 0, 0, 0, 0], 0);
console.log(ans);