#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - Frees a list
 *
 * @head: A pointer to d 1st element of the list
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *node;

	while (head)
	{
		node = head;
		head = head->next;
		free(node);
	}
}
