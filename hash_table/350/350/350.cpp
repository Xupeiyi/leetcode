#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
	vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
		unordered_map<int, int> map1;
		for (int n1 : nums1) {
			map1[n1]++;
		}

		vector<int> res;
		for (int n2 : nums2) {
			if (map1[n2] == 0) {
				continue;
			}
			map1[n2]--;
			res.push_back(n2);
		}
		return res;
	}
};


int main(){
	Solution s;
	vector<int> nums1{ 4,9,5 };
	vector<int> nums2{ 9, 4, 9, 8, 4 };
	vector<int> ans = s.intersect(nums1, nums2);
	for (int a : ans) {
		cout << a << ", ";
	}
}

