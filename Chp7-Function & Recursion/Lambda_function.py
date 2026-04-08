# Lambda Function is an anonymous function that can have any number of arguments but only one expression. It is defined using the lambda keyword, followed by the arguments, a colon, and the expression. The expression is evaluated and returned when the function is called.
# Lambda functions are often used for short, simple functions that are not worth defining with a full function definition. They are commonly used in conjunction with higher-order functions like map(), filter(), and reduce().
# Example of a lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

lambda x: x * 2  # This is a lambda function that takes one argument x and returns x multiplied by 2. However, since it is not assigned to a variable or called, it will not produce any output. To use this lambda function, you can assign it to a variable or call it directly with an argument.
double = lambda x: x * 2
print(double(5))  # Output: 10