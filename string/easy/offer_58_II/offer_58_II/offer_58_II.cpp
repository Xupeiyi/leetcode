#include <iostream>
#include <string>

using namespace std;

// ----------------------------------------------
// Solution1
void reverseString(string& s, size_t start, size_t end) {
	if (start >= end) {
		return;
	}
	while (start < end) {
		char tmp = s[start];
		s[start] = s[end];
		s[end] = tmp;
		start++;
		end--;
	}
}

class Solution1 {
public:
	string reverseLeftWords(string s, int n) {
		reverseString(s, 0, s.size() - 1);
		reverseString(s, s.size() - n, s.size() - 1);
		reverseString(s, 0, s.size() - n - 1);
		return s;
	}
};


// ------------------------------------------
// Solution2

int gcd(int a, int b) {
	int mod = b % a;
	while (mod != 0) {
		b = a;
		a = mod;
		mod = b % a;
	}
	return a;
}


class Solution {
public:
	string reverseLeftWords(string s, int n) {
		int tmp;
		int j, k;   // the index to be replaced and the index to replace with
		for (int i = 0; i < gcd(n, s.size()); i++) {
			/* move i-th values of blocks */
			tmp = s[i];
			j = i;
			while (true){
				k = j + n;
				if (k >= s.size()) k -= s.size();
				if (k == i) break;
				s[j] = s[k];
				j = k;
			}
			s[j] = tmp;
		}
	return s;
	}
};



int main(){
	Solution1 s;
	cout << s.reverseLeftWords("abcaadefghi", 8);
}

