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
	ListNode* swapPairs(ListNode* head) {
		if (head == NULL || head->next == NULL) {
			return head;
		}
		ListNode* rest = swapPairs(head->next->next);
		ListNode* new_head = head->next;
		head->next->next = head;
		head->next = rest;
		return new_head;
	}
};
int main(){
	Solution s;
	ListNode* n0 = new ListNode(0);
	ListNode* n1 = new ListNode(1, n0);
	ListNode* n2 = new ListNode(2, n1);
	ListNode* n3 = new ListNode(3, n2);
	n3->print();
	s.swapPairs(n3)->print();




}

