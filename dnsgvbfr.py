file=open('hello.jpg','rb')
img=file.read()
file.close()
file=open('copy.jpg','wb')
file.write(img)
file.close()

