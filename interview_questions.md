## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
Accessing an array is O(1) constant time, add/remove from the front is O(n) linear time, and add/remove at the end is O(1) constant time. Worst case scenario for adding a new element is O(n)

* What is the worse case scenario if you try to extend the storage size of a dynamic array?
In the event you try to append to a dynamic array without space, it will need to extend and will run in O(n) linear time.

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
A blockchain is a linked list(chain) of 'mined' blocks. The blocks are objects that contain a transaction ledger, proof of work, and a hash of the previous block -- the chain is a linked list of blocks. The blocks each have an index, timestamp, list of transactions, proof of work, and a hash of the preceding block. The chain is a linked list of blocks pointing toward the beginning of the chain.
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
A computationally difficult problem whose solution cannot be re-used, but is easy to verify. The proofs require the hash of the previous block and a new value, so they can't be created or manipulated out of order or be reused. A blockchain could be manipulated by an attacker with the ability to change a transaction and mine a new version of every block between that modified one and the most recent -- before a new one is created. 