#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
		unordered_set<int> set1(nums1.cbegin(), nums1.cend());
		unordered_set<int> ans;
		for (int n : nums2) {
			if (set1.find(n) != set1.end()) {
				ans.insert(n);
			}
		}
		return vector<int>(ans.cbegin(), ans.cend());
	}
};

int main() {
	Solution s;

	vector<int> v1{ 4, 9, 5 };
	vector<int> v2{ 9, 4, 9, 8, 4 };
	vector<int> ans = s.intersection(v1, v2);
	for (int a : ans) {
		cout << a << endl;
	}
}