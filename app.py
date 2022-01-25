def is_secret(str):
    is_string_secret = str.startswith('secret')
    return is_string_secret


def array_is_secret(list1):
    for item in list1:
        is_item_secret = item.startswith('secret')
        if(is_item_secret == True):
            print(is_item_secret)
            return is_item_secret

    return False


def is_divisible(num):
    if(num < 2):
        print('Number must be greater than 2 to be prime')
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                print('Notprime')
                return False
    print("prime")
    return True


this_is_secret = "secret message"
this_is_not_secret = "Not secret message"

is_secret(this_is_secret)
is_secret(this_is_not_secret)

secret_list = ["not", "yes", "no"]

array_is_secret(secret_list)

is_divisible(2)
