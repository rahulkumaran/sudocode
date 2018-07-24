# Sudocode

Sudocode, as the name suggests, is the supreme coding tool for everyone. Using sudocode, one actually need not learn how to code in C or C++.<br>
This particular tool helps you with converting your pseudocode to code.<br>
All you need to do is follow some rules laid here and you'll be good to go. For now, this particular thing only converts pseudocode to C code. But I'll soon be expanding this to convert pseudocode to python and C++ code too.<br>

It's a fairly simple project and does not involve any Machine Learning, but yes, implementing this using ML is definitely on the cards.<br>
But for now, it's going to be just some code written with some common sense to help achieve this.<br>

<h2>Possible Functionalities That Can Be Performed</h2>

- For loop
- While loop
- Function  definition
- Function calling
- Printing of statements and variables
- Initialising variables
- Basic increment and decrement statements

<b>All the above mentioned functionalities can be written in the form of a pseudocode and will be converted to code by our program</b><br>

<h2>Rules To Be Followed While Writing Pseudocode</h2>

- <h3>Starting main body</h3>
To start the code that's to be entered in the main body you need to start off with the word `start`

- <h3>Initialising Variables</h3>
Follow the following format:

    initialise <optional_type> <var_name>=<var_value>
    
    EXAMPLE: (1) initialise int temp=0
             (2) initialise var=100
Both the examples above are valid.<br>
Mentioning the type is optional. Incase you don't mention the type, the default type of the variable is float.

- <h3>Functions</h3>
To define a function that has n arguments, you can follow the following format:

    function <func_name> returns <return_type> with args <var_type> <var_1>, <var_type> <var_2>,.....,<var_type> <var_n>
    
    EXAMPLE: (1) function test returns int with args int a, float b, int c
             (2) function test returns void with args int size, float array_size
             
Incase you don't want to return anything, then you'll have to mention void.
Now to make sure you have some statements within the function, you can follow the format as mentioned for all above avaiable functionalities.<br>
Just make sure that you end your function with `endfunction`.<br>
An example is given below that gives you a clearer picture of how to define statements within a function.

    function test returns int with args int a, int b, int c
    print test func
    a++
    b++
    c++
    a = b + c
    return a
    endfunction
    
As you can see above, there's a `return` statement. This statement is optional.<br>
Incase you decide to return a value, just make sure you mention the value you want tor return.
