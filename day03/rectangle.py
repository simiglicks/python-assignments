
def rectangle(width, length):
    area= width*length
    perimeter= 2*width + 2*length
    print(area)
    print(perimeter)
    #i did perimeter not circumference

# check if file was run instead of imported
if __name__ == '__main__':
    width = int(input('enter width value: '))
    length = int(input('enter length value: '))

    rectangle(width, length)
    #I called the function re last weeks input