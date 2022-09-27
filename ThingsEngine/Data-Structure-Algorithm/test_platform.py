from Sorting.seletion_sort import selection_sort
from Tools.mz_create_a_random_list import create_a_random_list


def main():

    arr = create_a_random_list(10)

    print(arr)

    print(selection_sort(arr))


if __name__ == "__main__":
    main()

