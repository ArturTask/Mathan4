def my_print(f,output_mode,word):
    if(output_mode==0):
        print(word)
    elif(output_mode==1):
        f.write(word + "\n")
