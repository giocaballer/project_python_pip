import csv
'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      print('***' * 5)
      print(row)

if __name__ == '__main__':
  read_csv('data.csv')

'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) # avanzamos a la siguiente linea
    data = []
    for row in reader:
      iterable = zip(header, row) # unimos los dos valores en una tupla
      # recorremos las llaves y valores en las tupas iterable
      country_dict = {key: value for key, value in iterable} 
      # recorremos las llaves y valores en las tupas iterable
      data.append(country_dict) # Añadimos los diccionarios a una lista
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])
