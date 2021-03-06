#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: a pointer to a linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node2 = list;

	while(list && list->next && node2 && node2->next)
	{
		list = list->next;
		node2 = node2->next->next;
		if (list == node2)
			return (1);
	}
	return (0);
}
