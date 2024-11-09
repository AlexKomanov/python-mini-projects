from datetime import datetime

# name = "Alex"
# age = 36
#
# # Trick 1
#
# # regular_format
# print("Hello, my name is", name, "and I am", age, "years old")
#
# # Using format method
# format_method = "Hello, my name is {} and I am {} years old".format(name, age)
# print("Using format method:", format_method)
#
# # Using F-String
# f_string = f"Hello, my name is {name} and I am {age} years old"
# print("Using f_string:", f_string)

#
# # Trick 2
# price = 1234.56789
# print(round(price, 2))
# print(f"The price is ₪ {price:.2f}")
#
# large_number = 1000000000000
# print(large_number)
# print(f"{large_number:_}")
#
# now = datetime.now()
# print(now.date())
# print(str(now).split()[0])
# print(f"Today's date is {now:%d-%m-%Y}")
# print(f"Current time is is {now:%H:%M}")


# Trick 3
# x = 10
# y = 25
# print(f"x = {x}, y = {y}, x + y = {x + y}")
# print(f"{x = }, {y = }, {x + y = }")


# Trick 4
number = 456
print(number)
print (f"{number:b} | Binary")
print (f"{number:x} | Hexadecimal (lowercase)")
print (f"{number:X} | Hexadecimal (uppercase)")
print (f"{number:#x} | Hexadecimal with prefix")

percentage = 0.8764
print(f"{percentage:.2%} | Percentage format with 2 decimal places")


number = 12345.6789
print(number)
print (f"{number:.2f} | Two decimal places")
print (f"{number:_.2f} | Comma as thousands separator")
print (f"{number:010.2f} | Zero-padded width 10")
print (f"{number:+.2f} | Show sign")