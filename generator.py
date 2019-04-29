#Generator
def square_number(nums):
    result=[]
    for i in nums:
        result.append(i*i)

    return result


my_nums=square_number([1,2,3,4,5])
print(my_nums)


def square_number(nums):
    for i in nums:
        yield(i*i)

mynums=square_number([1,2,3,4,5])

for num in mynums:
    print(num)

#list comprihension
new_list=[x*x for x in [1,2,3,4,5,6]]
print(new_list)

#Generator
new_generator=(x*x for x in [1,2,3,4,5])

for i in new_generator:
    print(i)

#Generator don't hold entire result in the memory. It yield one result at a time.
#Generator has higher performance as compare to list

