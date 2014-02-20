def print_my_list(my_list):
    for item in my_list:
        print (item)

def main():
    with open("data.txt") as f:
        temporary_list = f.readlines()
    my_list = []
    for item in temporary_list:
        my_list.append(item.strip().capitalize())
    print_my_list(my_list)

if __name__ == '__main__':
    main()