from multiprocessing import Pool, cpu_count
from timeit import default_timer as timer


def pi_part(n):
    print(n)
    Rs = 0

    for i in range(n):
        Rs += i


def main():

    start = timer()

    np = cpu_count()
    print(f"You have {np} cores")

    n = 100_000_000

    testlist = [n, n, n, n]
    with Pool(processes=np) as pool:
        count = pool.map(pi_part, testlist)
        end = timer()
        print(f"elapsed time: {end - start}")
        print(f"estimate: {count}")

    start = timer()
    pi_part(100_000_000)
    pi_part(100_000_000)
    pi_part(100_000_000)
    pi_part(100_000_000)
    end = timer()
    print(f"elapsed time: {end - start}")
    print(f"estimate: {count}")


if __name__ == "__main__":
    main()
