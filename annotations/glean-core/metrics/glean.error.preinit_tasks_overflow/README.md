In Version 0 this figure includes the number of tasks that didn't overflow the queue.
That is to say, for a preinit dispatcher queue with a max size of 100,
this metric will either be absent or be reported with a value > 100.

In Version 1 (current) this figure counts only the tasks that overflowed the pre-initialization queue. 
