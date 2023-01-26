from hashlib import sha256
import json
import os

block_dir = os.curdir + '/block/'

def get_hash(files_name):
  file = open(block_dir + files_name,'rb').read()
  return sha256(file).hexdigest()

def get_files():
  files = os.listdir(block_dir)
  return sorted([int(i) for i in files])

def check_integrity():
  # 1. Считать хеш предыдущего блока
  # 2. Вычислить хеш предыдущего блока
  # 3. Сравнить полученные данные
  files = get_files()
  r = []

  for file in files[1:]:
      f = open(block_dir + str(file))
      h = json.load(f)['hash']
      
      prev_file = str(file - 1)
      actual_hash = get_hash(prev_file)

      if h == actual_hash:
        res = 'Ok'
      else:
        res = 'No'
      # print(f'Block {prev_file} is: {res}')
      r.append({'block': prev_file, 'result': res})
  return r

def write_block(name, amount, to_whom, prev_hash=''):
  files_int = get_files()
  files_list = files_int[-1]
  files_name = str(files_list + 1)
  prev_hash = get_hash(str(files_list))
  
  
  # print(files_name)

  data = {
          "name": name, 
          "amount": amount,   
          "to_whom": to_whom, 
          "hash": prev_hash}
  with open(block_dir + files_name, 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

def main():
  # write_block(name='Misha', amount=5, to_whom='Dasha')
  print(check_integrity())

if __name__ == '__main__':
  main()






