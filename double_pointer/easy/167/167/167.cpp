#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& numbers, int target) {
		int i = 0;
		int j = (int)numbers.size() - 1;
		while (i < j) {
			if (numbers[i] + numbers[j] == target) {
				return vector<int>{i+1, j+1};
			}
			else if (numbers[i] + numbers[j] < target) {
				i++;
			}
			else {
				j--;
			}
		}
	}
};


int main(){
	Solution s;
	vector<int> nums{ -1, 2, 7, 10, 11, 13, 15 };
	vector<int> ans = s.twoSum(nums, 18);
	cout << ans[0] << ", " << ans[1] << endl;
}

