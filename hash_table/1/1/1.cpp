#include <iostream>
#include <unordered_map>
#include <utility>

using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		
		unordered_map<int, int> position;
		for (int i = 0; i < (int)nums.size(); i++) {
			auto iter = position.find(target - nums[i]);
			if (iter != position.end()) {
				return vector<int>{ iter->second, i };
			}
			position.insert(pair<int, int>(nums[i], i));
		}
		return vector<int>{};
	}
};


int main(){
	Solution s;
	vector<int>nums {2, 7, 11, 15};
	vector<int> ans = s.twoSum(nums, 17);
	for (int n : ans) {
		cout << n << endl;
	}
}

