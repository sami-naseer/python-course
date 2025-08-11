name="sami"

def print_my_name():
    # global age
    age = 12
    print(f"my name is {name} age {age}")
    
    def nested_func():
        batch="sp24"
        print(f"my age is {age} my batch is {batch}")#parent ky methods and variables child fucntion mein accessible ho skty hein but child ky variables parent func mein accessible nai hoon
    # nested_func()
    return nested_func
    
ref = print_my_name()
ref()
# print(f"outside name is {name} outside age is{age}")
