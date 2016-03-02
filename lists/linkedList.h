//other notes: install gcc compiler + linux on this laptop.
//my linked list compilation code

//linkedlist.h
//properties of lists:
//-no definite length
//-each item contains a pointer to the next
//-last item points to NULL to indicate the end
//-
#include <stdlib.h>
#include <stdio.h>

typedef _node *Node;
typedef _list *List;

//standard functions:

List newList(void); //creates new list
Node newNode(E v);
void addFront(List, Node);  //adds node to front of list
void addEnd(List, Node); // adds node to end of list
void printList(List);   //prints out the linked list

