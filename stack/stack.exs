defmodule Stack do

    defstruct items: []

    def new do
        %Stack{}
    end

    def push(%Stack{items: items}, item) do
        %Stack{ items: [item | items] }
    end

    def pop(%Stack{items: []}) do
        raise("Cannot pop an empty Stack")
    end

    def pop(%Stack{items: [head | tail]}) do
        {head, %Stack{items: tail}}
    end

    def top(%Stack{items: []}) do 
        raise("Cannot see the top of an empty Stack")
    end

    def top(%Stack{items: [head | _tail]}) do
        head
    end

end
