#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - function that chacks if a singly linked list is a palindrome
 * @head: a pointer to a pointer pointed to the beginning of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *slow, *fast, *new_list;
	int mid;

	slow = *head;
	fast = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (fast->next != NULL)
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;
			mid +=1;
		}
		else if (fast->next != NULL && fast->next->next == NULL)
			fast = fast->next;
	}

	tmp = *head;
	new_list = reverse(&(slow->next));

	while (new_list != NULL)
	{
		if (tmp->n != new_list->n)
			return (0);
		new_list = new_list->next;
		tmp = tmp->next;
	}

	return (1);
}

/**
 * reverse_listint - function that reverse a linked list
 * @head: a pointer to a pointer pointed to the beginning of a linked list
 * Return: the beginning of a linked list reversed
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next, *current;

	prev = NULL;
	next = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
