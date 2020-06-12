# AdvancedMindBlock_Compiler
A program written in Python 3.7 to tokenize all keywords, symbols, integer, character, string, and label grammars of our custom langauge, Advanced Mindblock. Also parses the tokens properly, informing the user whenever they have made a mistake in our language.

AdvancedMindBlock is really simple functional programming language that fulfills the very basic of what makes a programming language a programming language (input, output, arithmetic, conditionals, and looping).

# Table of Contents
- [Quick Start](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#quick-start)
- [Hello World: Writing your First Lines of AMB](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#hello-world-writing-your-first-lines-of-amb)
  - [Setting Up Our File](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#setting-up-your-file)
  - [Encapsulating our Code](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#encapsulating-our-code)
  - [Declaring and Initializing Variables](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#declaring-and-initializing-varibles)
  - [Creating Our First Subroutine](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#creating-our-first-subroutine)
  - [Loops and Conditionals](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#loops-and-conditionals)
  - [Printing Out Our Answers](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#printing-out-our-answers)
- [Compiling Our AMB File](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#compiling-our-amb-file)
- [Dependencies/Technicals](https://github.com/jbakeacake/AdvancedMindBlock_Compiler#dependencies--technicals)
## Quick Start
To get a quick glimpse of the compiler, start by navigating to ```C:\...\my\path\to\AdvancedMindBlock_Compiler\``` and opening up ```test.amb``` with any text editor (notepad, vscode, sublime, atom, etc.) then examine some of the 
code inside our ```.amb``` file. Notice that the bulk of our code occurs inside our ```main``` method. In order for any ```.amb``` file to execute, it requires a ```main``` subroutine. Also, notice our ```printHello``` subroutine is written above our ```main``` subroutine.
To avoid any potential errors, make sure that any subroutine is written before our ```main``` method -- this is due partly because we're compiling to C.

Feel free to make some changes to some of the variables in the ```.amb``` file. Once you're finished making your changes, run the ```main.py``` python file, to compile your newly updated ```.amb``` file.

## Hello World: Writing your first lines of AMB
In this section, I'll cover some of the basics of our language. First, we're going to look at creating our own ```.amb``` file, and printing out "Hello World" to the console.

### Setting up our file
Start by making a new file inside ```C:\...\my\path\to\AdvancedMindBlock_Compiler\``` directory with the file extension ```.amb```.

Example: ```myFile.amb```

### Encapsulating our code
Any code written in our file must be encapsulated with the two identifiers, ```START_PROGRAM``` and ```END_PROGRAM.```. In addition to this, we need to make sure we have a ```main``` method to run our code. Any code you want to be executed must be written inside this method.

<br/>So our first few lines of code should be:
``` 
START_PROGRAM

CODE
START_SUB main:

END_SUB.

END_PROGRAM.
```

```START_PROGRAM``` indicates the opening to AMB code within our file.<br/>
```END_PROGRAM.``` indicates the end of AMB code within our file.<br/>
```CODE``` represents the start of any subroutines/methods.<br/>
```START_SUB``` indicates the opening to a subroutine/method that encapsulates a block of code.<br/>
```END_SUB.``` indicates the end of subroutine's block of code.<br/>

### Declaring and Initializing Varibles
Once we have our AMB file set up, we can begin our first few lines of actual code! First, we need some variables. There are 3 different types of variables that AMB uses -- ```INT```, ```STRING```, and ```[TYPE]```. The first 2 types are exactly what you would think them to be, INT is an integer,
and STRING is a string of characters. The last type represents how we can create an array with AMB -- which we can simply do by replacing ```TYPE``` with ```INT``` or ```STRING```.

Now, to declare a variable, we have have to write it inside our 'program' and before we start our 'code', i.e. after opening with ```START_PROGRAM``` and before we establish our ```CODE``` indicator. Let's start by declaring two ```INT``` variables.
``` 
START_PROGRAM

INT x;
INT y;

CODE
START_SUB main:

END_SUB.

END_PROGRAM.
```
To give these variables some values, must initialize them inside our ```main``` method. We can do this by using the assignment operator, ```:=```.

``` 
START_PROGRAM

INT x;
INT y;

CODE
START_SUB main:
  x := 5;
  y := 10;
END_SUB.

END_PROGRAM.
```

Now, let's look at what we can do with these variables.

### Creating our first subroutine 
Although we could simply multiply these two variables together by using an asterisk, let's say we want to do something a little more interesting, like finding the factorial of these numbers.
Though we could write out a solution in our ```main``` method, let's look at a more efficient way of solving this. We're going to create a subroutine that
will be ran every time we want to find a factorial of something.

First, let's make some variables to work with when we do our calculation inside our subroutine. We'll make three new ```INT```'s called ```factorialOf```, ```result```, and ```counter```.
Next, let's set up a new subroutine, and make sure we place this above our ```main``` method, and below our ```CODE``` indicator.

Our code should now look like this:
``` 
START_PROGRAM

INT x;
INT y;
INT factorialOf;
INT counter;
INT result;

CODE
START_SUB findFactorial:
  
END_SUB.

START_SUB main:
  x := 5;
  y := 10;
END_SUB.

END_PROGRAM.
```

### Loops and Conditionals
In most languages, we could solve for the factorial recursively -- meaning that we'd call our subroutine ```findFactorial``` inside it self until we get our desired result, but AMB doesn't allow us to pass variables to subroutines. So, we'll have to settle for an iterative solution.

The syntax for a while loop is as follows:
```
WHILE [boolean condition] DO
  // code goes here...
END_WHILE
```
The syntax for a conditional is as follows:
```
IF [boolean condition] THEN
  // code goes here
ELSE
  // else code goes here
END_IF
```
or, alternatively
```
IF [boolean condition] THEN
  // code goes here
END_IF
```

Utilizing a ```WHILE``` loop, we can solve for the factorial like so -- and to just throw in how we could use a conditional, let's use an ```IF...ELSE``` statement:
``` 
START_PROGRAM

...

START_SUB findFactorial:
  result := factorialOf;
  counter := factorialOf - 1;
  IF result != 1 THEN
      WHILE counter > 0 DO
        result := result * counter;
        counter := counter - 1;
      END_WHILE
  ELSE
    PRINT("Enter a REAL number please! \n");
  END_IF
END_SUB.

...
END_PROGRAM.
```

Now that we have our new factorial subroutine, let's call it inside our ```main``` method to make sure it executes when we compile our file. We do this by using the ```GOSUB``` keyword before our subroutine name, and appending ```()``` to the end of the subroutine name.

``` 
START_PROGRAM

...

START_SUB main:
  x := 5;
  y := 10;
  factorialOf := x;
  GOSUB findFactorial();
  factorialOf := y;
  GOSUB findFactorial();
END_SUB.

END_PROGRAM.
```

To make sure we're getting the correct answer, let's output our ```result``` to the console.

### Printing out our answers 
In order to print something out to the console, we have to we use the ```PRINT(...)``` method. You probably noticed this while writing out our subroutine. This method can only handle a single variable at one time, meaning that we can't concatenate an ```INT``` with a ```STRING```, nor can we further concatenate a ```STRING``` with a ```STRING```.

Let's utilize this method to print out the ```result``` of our factorial subroutine:
``` 
START_PROGRAM

...

START_SUB main:
  x := 5;
  y := 10;
  factorialOf := x;
  GOSUB findFactorial();
  PRINT(result);
  factorialOf := y;
  GOSUB findFactorial();
  PRINT(result);
END_SUB.

END_PROGRAM.
```

Great! Everything should be in order with our ```.amb``` file. All we have to do compile it, and run it!

If you wanna make sure your code matches what we've wrote, you can see the full code below:
``` 
START_PROGRAM

INT x;
INT y;
INT factorialOf;
INT counter;
INT result;

CODE

START_SUB findFactorial:
  result := factorialOf;
  counter := factorialOf - 1;
  IF result != 1 THEN
      WHILE counter > 0 DO
        result := result * counter;
        counter := counter - 1;
      END_WHILE
  ELSE
    PRINT("Enter a REAL number please! \n");
  END_IF
END_SUB.

START_SUB main:
  x := 5;
  y := 10;
  factorialOf := x;
  GOSUB findFactorial();
  PRINT(result);
  factorialOf := y;
  GOSUB findFactorial();
  PRINT(result);
END_SUB.

END_PROGRAM.
```
## Compiling our .amb file
To compile your own ```.amb``` file, find the ```main.py``` python file in the ```C:\...\my\path\to\AdvancedMindBlock_Compiler\``` directory and change the string found inside the ```readFile(...)``` method to the name of your ```.amb```
file.

![example_pythonChange](https://res.cloudinary.com/jbakeacake/image/upload/v1591945779/amb_pic1_pmijfg.png)

Once, you've inserted your file name, save the python file and run ```main.py``` to compile your code! After it completes it should display the results in your console similar to the output below. If not, navigate to the ```C:\...\my\path\to\AdvancedMindBlock_Compiler\RunnableFiles``` directory and run ```main.exe```.

![example_output](https://res.cloudinary.com/jbakeacake/image/upload/v1591946170/amb_pic2_ucd1ej.png)


## Dependencies / Technicals
- GCC Version 7.2.0
- Python 3.x
