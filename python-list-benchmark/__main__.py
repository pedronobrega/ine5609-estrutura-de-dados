import time

def main():
    lista = []
    for i in range(2000):
        lista.append(i)
    
    zero_time_start = time.time()
    for i in range(10000):
        lista[0]
    zero_time_end = time.time()

    n_time_start = time.time()
    for i in range(10000):
        lista[1151]
    n_time_end = time.time()

    return [
            [zero_time_end - zero_time_start],
            [n_time_end - n_time_start]
        ]

if __name__ == "__main__":
    print(main())