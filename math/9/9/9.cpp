#include <iostream>


int reverse(int x) {
	long res = 0;
	int ret = 0, max = INT32_MAX, min = 0;
	while (x) {
		res = res*10 + (x % 10);
		x /= 10;
	}
	return res > max || res < min ? 0 : res;
}

class Solution {
public:
	bool isPalindrome(int x) {
		if (x < 0) return false;
		return x == reverse(x);
	}
};

int main(){
	Solution s;
	std::cout << s.isPalindrome(1234567899);
}
