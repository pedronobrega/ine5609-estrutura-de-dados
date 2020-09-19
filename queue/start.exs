Code.require_file("queue.exs")

{:ok, queue} = Queue.new

# This will enqueue in the order 3 -> 4 -> k5
{:ok, queue} = queue |> Queue.enqueue(3)
{:ok, queue} = queue |> Queue.enqueue(4)
{:ok, queue} = queue |> Queue.enqueue(5)

# This will print 3
{:ok, x, queue} = Queue.dequeue(queue)
IO.inspect(x)

# This will print 4
{:ok, y, queue} = queue |> Queue.dequeue
IO.inspect(y)

# This will enqueue 15 at the end of the queue
{:ok, queue} = Queue.enqueue(queue, 15)

# This will print 5
{:ok, z, queue} = queue |> Queue.dequeue
IO.inspect z

# This will print 15
{:ok, a, queue} = queue |> Queue.dequeue
IO.inspect a

# This throw an exception
queue |> Queue.dequeue