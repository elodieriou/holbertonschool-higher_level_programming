#include "lists.h"

/**
 * insert_node - function that inserts a number into a linked list
 * @head: a pointer to a pointer pointing at the beginning of a linked list
 * @number: the value of the node
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || tmp->n >= number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}

	else
	{
		while (tmp && tmp->next && tmp->next->n < number)
			tmp = tmp->next;

		new->next = tmp->next;
		tmp->next = new;
	}
	return (new);
}
