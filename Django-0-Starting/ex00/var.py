def my_var():
    
    var_int = 42
    var_str = "42"
    var_str_2 = "quarante deux"
    var_float = 42.0
    var_bool = True
    var_list = [42]
    var_dict = {42: 42}
    var_tuple = (42,)
    var_set = set()

    print(f"{var_int} est de type", type(var_int))
    print(f"{var_str} est de type", type(var_str))
    print(f"{var_str_2} est de type", type(var_str_2))
    print(f"{var_float} est de type", type(var_float))
    print(f"{var_bool} est de type", type(var_bool))
    print(f"{var_list} est de type", type(var_list))
    print(f"{var_dict} est de type", type(var_dict))
    print(f"{var_tuple} est de type", type(var_tuple))
    print(f"{var_set} est de type", type(var_set))

if __name__ == '__main__':
    my_var()