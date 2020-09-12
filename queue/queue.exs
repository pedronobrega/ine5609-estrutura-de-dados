defmodule Queue do
    defstruct items: []

    def new do
        %Queue{}
    end

    def enqueue(%Queue{items: items}, item) do
        %Queue{items: items ++ [item]}
    end

    def dequeue(%Queue{items: []}) do
        raise("Cannot remove item from an empty queue")
    end

    def dequeue(%Queue{items: [head | tail]}) do
        {head, %Queue{items: tail}}
    end
end