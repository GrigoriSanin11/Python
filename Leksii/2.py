  # cpicok
  
  List_1 = []
  list = list()
  list = [1, 2, 3, 4]
  print (*list) # вывод без запятых
  
  for i in list:
      print(i) # вывод всех чисел из списка по очереди(перебор списка)
  
  print(len(list))  # вывод количства элементов в списке 
  
  
  print(list[0]) # вывод числа с индексом 0
  
  
  list = [1, 5]
  list.append(8) # добавить число в список
  
  print(list.insert(2,11)) # добавить число в список 2 индекс, 11 число
  
  
  for i in range(5): # список состоит из 5 элементов
  
  
  print(list.pop(4)) # удалить последний элемент/ индекс 


t = (1,) # изюминка в запятой _ картетж неизменяемый список 'tuple'
print(type(t))


d = {} или dict() # создаем словарь
d['w'] = 'werty' # записали в словарь
print(d['w']) # вывод из словаря
dex = {'up' : 'вверх', 'left' : 'levo'} # первое ключ, второе выводимое зачение 


Colors =  {'red', 'blue', 'green'} # множества