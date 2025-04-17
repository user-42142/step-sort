# step-sort
A new sort algorithim

This algorithm is a method for sorting any shuffled list of numbers. The main idea is to build, in each round, a growing subsequence from the first elements that are not yet in order.

At the beginning, a list is defined as the current version of the shuffled list, and an auxiliary variable stores the growing subsequence formed in the previous round. The algorithm enters a loop that continues until all elements are in ascending order.

In each round, the part of the list that still needs to be organized is analyzed. From this part, the algorithm tries to form an increasing subsequence (called sorted_part), adding elements as long as they are greater than the last inserted value. Elements that do not fit into this sequence go into a separate list (called unsorted_part).

After that, the increasing subsequence from the previous round is used to assist with organization. Through a binary search, it is divided into two parts: the elements that are still greater than the last one in sorted_part, and those that are smaller or equal. The larger ones are added to the end of sorted_part, maintaining the increasing order, while the others go into unsorted_part, since they still need more rounds to be properly positioned.

The main list is then updated by placing first the unordered elements (unsorted_part), followed by those already in order (sorted_part). The sorted_part subsequence formed in this round becomes the new reference for the next iteration.

This process repeats until all elements in the list form a single increasing sequence — in other words, until the list is completely sorted.

A curious phenomenon that can be observed during the execution of this algorithm is the formation of visible increasing blocks in the graphical visualization of the list. These blocks resemble small stairs or pyramids and represent locally sorted subsequences. Since the algorithm only adds an element to the growing sequence if it is greater than the last inserted value, elements that do not fit are postponed to future rounds, creating these "islands" of partial order. With each iteration, these blocks gradually merge until the entire list is in ascending order. This reveals a progressive and structured behavior, in which complete sorting emerges from multiple local orderings.

