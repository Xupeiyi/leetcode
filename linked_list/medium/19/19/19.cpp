#include <iostream>

struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
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
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		// 1. set a pointer to the n th element
		size_t count = 1;
		ListNode* i = head;
		while (count < n) {
			i = i->next;
			count++;
		}
		// 2. set another pointer to the head element
		ListNode** j = &head;
		
		// 3. move i and j together until i points at the last element
		while (i->next != NULL) {
			i = i->next;
			j = &(*j)->next;
		}

		// 4. remove what j is now pointing at
		ListNode* to_remove = *j;
		*j = (*j)->next;
		delete to_remove;

		return head;
	}
};



int main() {
	Solution s;
	ListNode* n0 = new ListNode(0);
	ListNode* n1 = new ListNode(1, n0);
	ListNode* n2 = new ListNode(2, n1);
	ListNode* n3 = new ListNode(3, n2);
	ListNode* n4 = new ListNode(4, n3);
	ListNode* n5 = new ListNode(5, n4);
	n5->print();

	s.removeNthFromEnd(n5, 1)->print();




}