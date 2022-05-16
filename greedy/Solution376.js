/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    let ans = 1;
    let pre_diff = 0;
    for (let i = 1; i < nums.length; i++){
        let diff = nums[i] - nums[i-1];
        if(diff * pre_diff <= 0 && diff != 0){
            ans++;
            pre_diff = diff;
        }
    }
    return ans;
};

const nums = [1,17,5,10,13,15,10,5,16,8];
let res = wiggleMaxLength(nums);
console.log(res);