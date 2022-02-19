#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
# include <algorithm>

using namespace std;
/* first trial
#define tuple pair<int, int>

class Solution {
public:
	vector<vector<int> > threeSum(vector<int>& nums) {
		set<tuple> invalid;
		unordered_map<int, vector<tuple>> cplmt;
		vector<vector<int> > results;

		for (int i = 0; i < (int)nums.size(); i++) {
			// find results
			auto it = cplmt.find(nums[i]);
			if (it != cplmt.end()) {
				for (tuple valid : it->second) {
					if ((invalid.find(tuple(nums[i], valid.first)) == invalid.end())
						&& (invalid.find(tuple(nums[i], valid.second)) == invalid.end())
						) {
						vector<int> res = { nums[i], valid.first, valid.second };
						results.push_back(res);

						for (int i = 0; i < (int)res.size(); i++) {
							for (int j = 0; j < (int)res.size(); j++) {
								if (i != j) invalid.insert(tuple(res[i], res[j]));
							}
						}
					}
				}
			}
			// update cplmt
			for (int j = 0; j < i; j++) {
				auto it = invalid.find(tuple(nums[i], nums[j]));
				if (it == invalid.end()) {
					cplmt[0 - nums[i] - nums[j]].push_back(tuple(nums[i], nums[j]));
				
				}
			}
		}
		return results;
	}
};
*/

class Solution {
public:
	vector<vector<int> >threeSum(vector<int>& nums) {
		vector<vector<int>> result;
		sort(nums.begin(), nums.end());
		// find a + b + c = 0
		// a = nums[i], b = nums[j], c = -(a + b)
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] > 0) continue;
			if (i > 0 && nums[i] == nums[i - 1]) continue;

			unordered_set<int> met; // numbers that have been met before
			for (int j = i + 1; j < nums.size(); j++) {
				// do not allow more than two repeative numbers
				if (j > i + 2 && nums[j] == nums[j - 1] 
					&& nums[j - 1] == nums[j - 2]) continue;
				int c = 0 - nums[i] - nums[j];
				if (met.find(c) != met.end()) {
					result.push_back({ nums[i], nums[j], c });
					met.erase(c);
				}
				else {
					met.insert(nums[j]);
				}
			}
		}
		return result;
	}
};

void print(vector<int>& nums) {
	for (size_t i = 0; i < nums.size(); i++){
		cout << nums[i] << ", ";
	}
	cout << endl;
}
int main(){
	Solution s;
	vector<int> nums{ 0, 0, 0, 0 };
	vector<vector<int>> ans = s.threeSum(nums);
	for (vector<int> v : ans) {
		print(v);
	}
}

