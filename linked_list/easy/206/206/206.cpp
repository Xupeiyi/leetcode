#include <cstdio>
#include <iostream>

 
 struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

	void print() {
		ListNode* curr = this;
		while (curr != NULL) {
			std::cout << curr->val << "->";
			curr = curr->next;
		}
		std::cout << std::endl;
	}
 };
 

class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		ListNode* prev = NULL;
		ListNode* curr = head;
		ListNode* next;

		while (curr != NULL) {
			next = curr->next;
			curr->next = prev;
			prev = curr;
			curr = next;
		}
		return prev;
	}
};

int main(){
	Solution s;
	ListNode n0(0);
	ListNode n1(1, &n0);
	ListNode n2(2, &n1);
	n2.print();
	ListNode* res = s.reverseList(&n2);
	res->print();
}
