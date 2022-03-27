#############################
## Greatest Common Factors ##
#############################

def is_prime(number):
    if number > 1:
  
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                break
        else:
            return True
    
    return False


def check_factors(number):
    factor_list = []

    if is_prime(number):
        factor_list += [1, number]
        return factor_list

    for length in range(1, number + 1, 1):
        quotent = length    

        if (number / quotent).is_integer():
            factor_list += [quotent]

    return factor_list


def find_GCF(list_of_numbers):

    all_factors = []
    common_factors = []

    for number in list_of_numbers:
        all_factors += check_factors(number)

    for number in all_factors:
        if all_factors.count(number) == len(list_of_numbers):
            common_factors += [number]

    return max(common_factors)


####################
## Testing Script ##
####################

number_list = [44, 88, 96, 128]
print(f"The greatest common factor is {find_GCF(number_list)}")