documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
 
 
def people_num_doc(doc=documents):
  num_doc = input('Введите номер документа:')
  for hum in documents:
    if num_doc == hum['number']:
      print(hum['name'])
      break
  else:
    print('Номер документа введен неверно')


def num_shelf(dir=directories):
  num_doc = input('Введите номер документа: ') 
  for el in dir.items(): 
    if num_doc in el[1]:
      print(el[0]) 
      break
  if num_doc not in el[1]:
    print('Номер введен неверно')


def docs_list(docs=documents):
  for doc in documents:
    print(' '.join(list(doc.values())))



def add_doc(docs=documents, dir=directories):
  type = input('Введите тип документа: ')
  number_doc = input('Введите номер документа: ')
  doc_own = input('Введите имя владельца: ')
  shelf_num = input('На какую полку поместить документ?')

  
  
  if shelf_num in directories.keys():
    new_dict = ({'type': type, 'number': number_doc, 'name': doc_own})
    documents.append(new_dict)
    directories[shelf_num] = number_doc,
    directories[shelf_num]
    print(documents)
    print()
    print(directories)
    return documents, directories
  else:
    print('Такой полки не существует')


def main():
  print('Перечень команд и клавиш для их вызова:' 
'p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;',
's – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится.',
'l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"',
'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.','q - останавливает выполнение программы',sep = '\n')
  while True:
    comand = input('Введите команду:')
    if comand == 'p':
      people_num_doc()
    elif comand == 's':
      num_shelf()
    elif comand == 'l':
      docs_list()
    elif comand == 'a':
      add_doc()
    elif comand == 'q':
      print('Остановка программы...')
      break
    else:
      print('Такой команды нет')
      continue


main()