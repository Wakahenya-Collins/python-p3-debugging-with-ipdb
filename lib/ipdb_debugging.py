# #!/usr/bin/env python3

# import ipdb

# def plus_two(num):
#     num = 3
#     num + 2
#     # ipdb.set_trace()
#     return num
def plus_two(num):
    result = num + 2  
    return result     

def test_plus_two():
    result = plus_two(3)
    assert result == 5  

test_plus_two() 


