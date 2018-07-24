# Sudocode

Sudocode, as the name suggests, is the supreme coding tool for everyone. Using sudocode, one actually need not learn how to code in C or C++.<br>
This particular tool helps you with converting your pseudocode to code.<br>
All you need to do is follow some rules laid here and you'll be good to go. For now, this particular thing only converts pseudocode to C code. But I'll soon be expanding this to convert pseudocode to python and C++ code too.<br>

It's a fairly simple project and does not involve any Machine Learning, but yes, implementing this using ML is definitely on the cards.<br>
But for now, it's going to be just some code written with some common sense to help achieve this.<br>

<h2>Possible Functionalities That Can Be Performed</h2>

![](https://media.giphy.com/media/5VKbvrjxpVJCM/giphy.gif)

- For loop
- While loop
- Function  definition
- Function calling
- Printing of statements and variables
- Initialising variables
- Basic increment and decrement statements

<b>All the above mentioned functionalities can be written in the form of a pseudocode and will be converted to code by our program</b><br>

<h2>Rules To Be Followed While Writing Pseudocode</h2>

![](https://media.giphy.com/media/3oxHQBuKWs2RuAwY5q/giphy.gif)


- <h3>Starting main body</h3>
To start the code that's to be entered in the main body you need to start off with the word `start`

- <h3>Initialising Variables</h3>
Follow the following format:

    initialise <optional_type> <var_name>=<var_value>
    
    EXAMPLE: (1) initialise int temp=0
             (2) initialise var=100
Both the examples above are valid.<br>
Mentioning the type is optional. Incase you don't mention the type, the default type of the variable is float.

- <h3>Print</h3>
`Print` helps you print things on console. It could be statements or variables.<br>
The best part about this application is that it understands whether you want to print a string or a variable.<br>
The only drawback here being that, you can print only one particular variable in one print statement for now.<br>
Let's see how it works!

        print <statement_or_variable to be printed>
        
        EXAMPLE: (1) print hey there
                 (2) print inside loop now
                 (3) Let's assume there's a variable "temp" in the main body, then
                     print temp

The last statement says print temp. Here, the application understands that temp means the variable temp and not the string temp to be printed. It also understands whether the variable mentioned is an integer or a float value and accordingly mentions the format specifier in C and C++.<br>

- <h3>For Loops</h3>
Incase you want utilise the functionality of for loops, you can do it in the following manner:

        for int <var_name>=<start_value> to <stop_value>
        
        EXAMPLE: (1) for int i=0 to 10
                     -------
                     -------
                     endfor
                 (2) for int i=50 to 10
                     -------
                     -------
                     endfor
`endfor` is used at the end of the for loop. As, you can see above, you can loop from a higher to a lower value and also the other way round.<br>
Also, the ----- can be filled with statements or operations that you want to perform within the for loop.<br>
By default, the increment and decrement in the loop is 1. Sometimes you might want to increment or decrement the looping variable by a value greater than 1. <br>
If that's the case, don't worry, we have provision for that as well. Follow the following steps:<br> 

        for int <var_name>=<start_value> to <stop_value> with gap=<gap_size>
        
        Example: (1) for int i=0 to 60 with gap=3
                     -------
                     -------
                     endfor
                 (2) for int i=60 to 10 with gap=3
                     -------
                     -------
                     endfor

You need not mention a negative gap as the application understands that it's supposed to give a negative gap.<br>

Now, an example of a loop:

        for int i=10 to 1 and gap=2
        print i
        endfor
        
Here, the application understands that the program is supposed to print `i` as a variable and hence it print the value of `i` and not just `i` as it is.
 
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
