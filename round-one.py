#!/usr/bin/python3

def main():
  user = input('Enter you name: ')
  password = input('Enter your password must be 10 word and number: ')
  limit = 10
  limit2 = 6
  count = 0
  while len(password) != limit :
      print('Your maximum is only 10 not less or more')
      count = count +1
      if count >= 3:
          quit()
  else:
      print('Access your account')
  access = input("Enter your code: ")
  if len(access) != limit2:
      print('Please enter right code')
  else:
      print('done')

if __name__ == "__main__":
    main()
