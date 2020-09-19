defmodule Stack do

    defstruct items: []

    def new do
        {:ok, %Stack{}}
    end

    def push(%Stack{items: items}, item) do
        {:ok, %Stack{ items: [item] ++ items }}
    end

    def pop(%Stack{items: []}) do
        raise("Cannot pop an empty Stack")
    end

    def pop(%Stack{items: [head | tail]}) do
        {:ok, head, %Stack{items: tail}}
    end

    def top(%Stack{items: []}) do 
        raise("Cannot see the top of an empty Stack")
    end

    def top(%Stack{items: [head | _tail]}) do
        {:ok, head}
    end

end
