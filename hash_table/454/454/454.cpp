#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
		unordered_map<int, int>sum12;
		for (int n1 : nums1) {
			for (int n2 : nums2) {
				sum12[n1 + n2]++;
			}
		}
		
		int count = 0;
		for (int n3 : nums3) {
			for (int n4 : nums4) {
				auto it = sum12.find(-(n3 + n4));
				if (it != sum12.end()) {
					count += it->second;
				}
			}
		}
		return count;
	}
};


int main(){
	Solution s;
	vector<int> A{ 1, 2 };
	vector<int> B{ -2, -1 };
	vector<int> C{ -1, 2 };
	vector<int> D{ 0, 2 };
	cout << s.fourSumCount(A, B, C, D);
}

