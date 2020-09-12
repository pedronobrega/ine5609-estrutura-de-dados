Code.require_file("stack.exs")

# Creating a new Stack
stackInstance = Stack.new

# Same as => Stack.push(Stack.push(stackInstance, 3), 13)
stackInstance = stackInstance |> Stack.push(3) |> Stack.push(13)

# Should print 13
x = Stack.top(stackInstance)
IO.inspect(x)

# Should print 13
{y, stackInstance} = stackInstance |> Stack.pop
IO.inspect(y)

# Should print 3
{z, stackInstance} = stackInstance |> Stack.pop
IO.inspect(z)

# Should raise exception
stackInstance |> Stack.pop
