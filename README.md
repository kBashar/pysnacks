# pysnacks

Problem statement

1. There is a food object, eating(colliding with) that makes the snakes bigger.
2. Snake can move in three directions 
    a. up
    b. down
    c. forword
3. If snake is a chain of objects, every object shifts to the previous object's position. 
4. If the snakes collide with itself, it's dead, Game Over!
5. If the snake hits an edge, Game Over!

ToDos
>> 1.a. Make a grid in the screen.
>> 1.b. Create an object that moves in three directions.
>> 1.c. snake object moves automatically 
2. Make the frog object appear randomly on screen.
    >> cell conversion math
    make a random integer to select cell
    check for the presence of the snake

3. On eating(colliding with) the object the sanke object grows in length.
4. Follow the snake path
5. A new Oject pop up excluding the sanke body.


20 x 20 400 cell 
400 x 400 
array = [5][6]
array[3][2] = 1
array[3][3] = 1

0 0 0 0 0
0 0 1 0 0
0 1 1 0 0
0 0 0 0 0
0 0 2 0 0
0 0 0 0 0
[210] = 0 
210/20 10 10

refs:
https://realpython.com/python-scope-legb-rule/

How to make the Snake grow:
1. first make a  function grow_snake to take a paramiter Index and drawes the snake at an index.
2. it will take in the index position of x_tail_cell, and y_tail_cell and draw a snake block.
3. it will also clear it's tail position and keeps on drawing a block as it will continue to take index param.
4. this function will be called everytime snake collides with frog.
5. it will only inherit positon of its previous cell/block meaning 2nd time it is called it will take param from it's previous call.
6. This will keep going on.
7. I am running out of ideas.  