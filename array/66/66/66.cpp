#include <iostream>
#include <vector>

using namespace std;


vector<int> plusOne(vector<int>& digits) {
	int carry = 1;
	for (int i = digits.size() - 1; i >= 0; i--) {
		int sum = digits[i] + carry;
		int digit = sum % 10;
		digits[i] = digit;
		carry = sum / 10;
	}
	if ((carry == 1) & (digits[0] == 0)) {
		digits.insert(digits.begin(), 1);
	}
	return digits;
}

int main(){
	vector<int> nums{ 1,9,9,9 };
	plusOne(nums);
	for (int n : nums) {
		cout << n;
	};
}
