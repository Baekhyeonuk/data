

#with open("hello.txt", "w") as file:
 #   for i in range(3):
  #      file.write("Hello, world! {0}\n".format(i))

#lines = ["안녕하세요.\n", "파이썬\n", "핵 꿀잼입니다.\n"]

#with open("hello.txt", "w") as file:
 #   file.writelines(lines)
    # hello.txt 파일을 쓰기 모드(w)로 열기


#aa = input("정수 입력")

#if aa.isdigit():
 #   bb=int(aa)
  #  print(bb*bb)
#else:
 #   print("정수를 입력하세요")


# try : 오류가 발생할 수 있는 구문
# except : 오류가 발생 했을 때 처리 하는 구문
# else : 오류가 발생하지 않았을 때 처리하는 구문
# finally : 오류 발생과 관계없이 실행할 구문

while True:

    try:
        aa = input("정수 입력")
        bb = int(aa)
    except:
        print("정수를 입력하세요")
    else:
        print(bb*bb)
        break
    finally:
        print("=====")
        
