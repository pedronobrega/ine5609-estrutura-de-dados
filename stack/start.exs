Code.require_file("stack.exs")

# Creating a new Stack
{:ok, stackInstance} = Stack.new

# Will push 3 to the top of the stack
{:ok, stackInstance} = stackInstance |> Stack.push(3)

# Will push 13 to the top of the stack
{:ok, stackInstance} = stackInstance |> Stack.push(13)

# Will print 13
{:ok, x} = Stack.top(stackInstance)
IO.inspect(x)

# Will print 13
{:ok, y, stackInstance} = stackInstance |> Stack.pop
IO.inspect(y)

# Will print 3
{:ok, z, stackInstance} = stackInstance |> Stack.pop
IO.inspect(z)

# Will raise an exception
stackInstance |> Stack.pop
