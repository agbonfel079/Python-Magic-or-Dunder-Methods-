# Dunder or  magic methods 
from todo import Todo

k_todo = Todo(name='Kingsley')
e_todo = Todo(name='Emmanuel')
print(repr(k_todo))

print(str(k_todo))
print(str(e_todo))

k_todo.add('buy milk')

e_todo.add('wake up')
e_todo.add('code')

print(len(k_todo))

print(k_todo > e_todo)
print(k_todo < e_todo)





