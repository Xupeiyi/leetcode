var checkInclusion = function(s1, s2) {
    const length1 = s1.length, length2 = s2.length;
    if (length1 > length2){
        return false;
    }

    // key: use a hash map to represent the difference between two strings
    // initial state of the window
    const count = new Array(26).fill(0);
    for (let i = 0; i < length1; ++i) {
        count[s1[i].charCodeAt() - 'a'.charCodeAt()]--;
        count[s2[i].charCodeAt() - 'a'.charCodeAt()]++;
    }

    let diff = 0;
    for (const char of count){
        if (char != 0) diff++;
    }
    if (diff == 0){
        return true;
    }

    // move window
    for (let end = length1; end < length2; end++){
        let inIdx = s2[end].charCodeAt() - 'a'.charCodeAt();
        let outIdx = s2[end - length1].charCodeAt() - 'a'.charCodeAt();

        if (inIdx == outIdx) continue;
        
        if (count[inIdx] == 0) diff++;
        else if (count[inIdx] == -1) diff--;
        count[inIdx]++;

        if (count[outIdx] == 0) diff++;
        else if (count[outIdx] == 1) diff--;
        count[outIdx]--;

        if (diff == 0) return true;
    }
    return false;
};

let ans = checkInclusion("abc", "efgcabggh");
console.log(ans);