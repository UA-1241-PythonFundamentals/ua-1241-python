#1 PART
zen_string="""
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
"""

find_word1, find_word2, find_word3="better", "never", "is"
print(f"{find_word1} is {zen_string.count(find_word1)} times")
print(f"{find_word2} is {zen_string.count(find_word2)} times")
print(f"{find_word3} is {zen_string.count(find_word3)} times")

print(zen_string.upper())

zen_replace_string=zen_string.replace("i","&")
print(zen_replace_string)


#PART2
random_four_digit_number="5947"
int_rn=int(5947)
n1,n2,n3,n4=int_rn//1000, (int_rn//100)%10, (int_rn%100)//10, int_rn%10
product=n1*n2*n3*n4
sum=n1+n2+n3+n4
print(f"sum = {sum}")
print(f"product = {product}")

print(f"Reverse numbers is {str(int_rn)[::-1]}")

sorted_list=(sorted((random_four_digit_number)))
string_with_trash='-'.join(sorted_list)
free_sorted_string=string_with_trash.replace('-','')
print(f"Sorted numbers is {int(free_sorted_string)}")

#PART3
sino='Right hand'
soloma='Left hand'
print(f"Was {sino,soloma}")

sino,soloma=soloma,sino
print(f"Became {sino,soloma}")

