def is_Prime(x):
  if x == 2:
    return True
  elif x <= 1 or x%2 == 0:
    return False
  i = 3
  while i*i <= x:
    if x%i == 0:
      return False
    i += 2
    return True
    
user_input = input("整数を入力して下さい　").strip()
if not user_input:
  print("何も入力されていません")
elif user_input.isdigit():
  num = is_Prime(int(user_input)) 
  if num == True:
    print(f"結果:「{user_input}」は素数です")
  elif num == False: 
    print(f"結果:「{user_input}」は素数ではありません") 
else:
  print(f"「{user_input}」は整数ではありません（文字や記号が含まれています）")
