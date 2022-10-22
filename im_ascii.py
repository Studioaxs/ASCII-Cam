import cv2
import numpy as np 


def main():

    '''
    Main function that opens the video device, and calls pic_to_ASCII to convert a pictur into an str.
    Inputs : None
    Outputs : None
    '''
    cap = cv2.VideoCapture(0) #Capture a video flow (On fisrt video device found)

    #Check if the video device could be opened, else, set return value to False to break the loop
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret: #If vieo device could be opened, continue 
        ret, frame = cap.read() #Read the video flow
        print(pic_to_ASCII(frame)) #Print the video frame converted i to ASCII characters
        key = cv2.waitKey(50) #Wait 50 ms and store pressed keys in 'key'
        cv2.namedWindow('leave', cv2.WINDOW_NORMAL)
        if key == ord("q"): #If key is 'Escape', break the loop
            print("leave")
            break
def pic_to_ASCII(frame,columns = 120, rows = 35):

    '''
    This function convert an input picture into a string of ASCII characters that replaces pixels. It allows to print an image in the console. 'frame' is the input picture
    'columns' and 'rows' are parameters the define the nb of columns and rows in the ASCII picture.
    Inputs : Array (frame), int (columns), int (rows)
    Outputs : str'''

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convert input image to grayscale image

    height, width = frame.shape #Get the height and width of the frame

    #Calculate cells dimensions, each cell will be replaced by a character later, depending of mean value of the px of the cell
    cell_height = height / rows
    cell_width = width / columns

    #Raise errors if we set too many columns and rows
    if cell_height > height :
        print("Error ! Too many rows")
    if cell_width > width:
        print("Error ! Too many columns")
    
    result = "" #Initialisation of an empty string to store the result

    #Browse each cell of the frame
    for i in range(rows):
        for j in range(columns):
            gray_line = np.mean(
                frame[int(i*cell_height):min(int((i+1)*cell_height),height) , int(j*cell_width) : min(int((j+1)*cell_width), width)] #Select all px in the cell
            )
            result += gray_2_char(gray_line) #Convert 'gray_line' into characters and add to result
        result+='\n' #At the end of a row of cells, return to another line
    return result #Return the result string of characters

def gray_2_char(gray):

    '''
    This function takes an integer as input and returns a character. The character is determined depending on the input value in the 'char_list'.
    Inputs : int
    Outputs : str
    '''
    
    char_list = ' .:-=+*#%@' #Store some characters to replace cells, depending of the mean value of px of the cells
    num_char = len(char_list) #Store the length of the 'char_list'
    #Return the index of the character that will replace the selected cell
    return char_list[
        min(
            int(gray * num_char/255), #'num_car/255' is the step between each character in the 'char_list'. We multiply gray with this step to obtain the corresponding character to the cell value
            num_char-1) #Take the minimum of 'gray * num_char/255' and 'num_char-1' to avoid 'Out of Index' errors, so we can't try to use an higher index than 'num_char - 1' (because there are 'num_char' elements in 'char_list')
            ]

if __name__ == '__main__':
    main()