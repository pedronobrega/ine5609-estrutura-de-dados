Code.require_file("queue.exs")

queue = Queue.new

# This will enqueue in the order 3 -> 4 -> 5
queue = queue
    |> Queue.enqueue(3)
    |> Queue.enqueue(4)
    |> Queue.enqueue(5)

# This will print 3
{x, queue} = Queue.dequeue(queue)
IO.inspect(x)

# This will print 4
{y, queue} = queue |> Queue.dequeue
IO.inspect(y)

# This will enqueue 15 at the end of the queue
queue = Queue.enqueue(queue, 15)

# This will print 5
{z, queue} = queue |> Queue.dequeue
IO.inspect z

# This will print 15
{a, queue} = queue |> Queue.dequeue
IO.inspect a

# This throw an exception
queue |> Queue.dequeue