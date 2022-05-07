/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    const count = new Array(26).fill(0);
    let maxCount = 0;
    let start = 0;
    const length = s.length;
    for (let end = 0; end < length; end++){
        let idx = s[end].charCodeAt() - 'A'.charCodeAt();
        count[idx]++;
        maxCount = Math.max(maxCount, count[idx]);
        if (end - start + 1 > maxCount + k){
            count[s[start].charCodeAt() - 'A'.charCodeAt()]--;
            start++;
        }
    }
    return length - start;
};

let ans = characterReplacement("AABABBA", 1);
console.log(ans);