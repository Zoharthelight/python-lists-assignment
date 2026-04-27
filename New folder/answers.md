# Answers – Python Lists Assignment

## Task 6: Memory Model

### Why did both lists change?
Because `b = a` does not create a new list. It creates a reference to the same list in memory.

### Why are ids same?
Both variables point to the same memory location, so Python assigns them the same ID.

### What does this mean?
It means lists are mutable and shared references can lead to unintended side effects if not handled carefully.