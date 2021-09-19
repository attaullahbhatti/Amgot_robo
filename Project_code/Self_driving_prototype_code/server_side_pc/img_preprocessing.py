import numpy as np
import matplotlib.pyplot as plt
import cv2
import math


#%%
height = 240#image.shape[0]
width  = 360#image.shape[1]
line_thickness = 3
#%%
def region_of_interest(image_roi,line_thickness):
    x1, y1, x2, y2 = 5 ,70 ,45 ,40 # x1,y1
    cv2.line(image_roi,(x1,y1),(x2,y2),(0,0,255),line_thickness)
    
    # To see on which points line is drawn
    # =============================================================================
    # cv2.circle(image,(3 ,200),5,(255,0,0),cv2.FILLED)
    # cv2.circle(image,(33 ,150),5,(0,255,0),cv2.FILLED)
    # plt.imshow(image)
    # =============================================================================
    
    x1, y1, x2, y2 = 340 ,70,295 ,40 # x2,y2
    cv2.line(image_roi,(x1,y1),(x2,y2),(0,0,255),line_thickness)
    
    # To see on which points line is drawn
    # =============================================================================
    # cv2.circle(image,(width ,200),5,(255,0,0),cv2.FILLED)
    # cv2.circle(image,(327 ,150),5,(0,255,0),cv2.FILLED)
    # plt.imshow(image)
    # =============================================================================
    
    x1, y1, x2, y2 =  5 ,70  ,340 ,70 # x1,x2
    cv2.line(image_roi,(x1,y1),(x2,y2),(0,0,255),line_thickness)
    
    # To see on which points line is drawn
    # =============================================================================
    # cv2.circle(image,(33 ,170),5,(0,255,0),cv2.FILLED)
    # cv2.circle(image,(327 ,170),5,(255,0,0),cv2.FILLED)
    # plt.imshow(image)
    # =============================================================================
    
    x1, y1, x2, y2 = 45 ,40 ,295 ,40 # y1,y2
    cv2.line(image_roi,(x1,y1),(x2,y2),(0,0,255),line_thickness)
    
    # To see on which points line is drawn
    # =============================================================================
    # cv2.circle(image,(3 ,200),5,(255,0,0),cv2.FILLED)
    # cv2.circle(image,(width ,200),5,(0,255,0),cv2.FILLED)
    # plt.imshow(image)
    # =============================================================================
    return image_roi

def get_perspective(width,height,image):
    # points on which you want to transform
    pts1 = np.float32([[5 ,70], [340 ,70], [45 ,40], [295 ,40]]) # x1,x2,y1,y2
    from_begin, from_end = 40, 310
    pts2 = np.float32([[from_begin, height], [from_end, height], [from_begin, 0], [from_end, 0]])
    
    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    perspective_image = cv2.warpPerspective(image, matrix, (width,height))
    return perspective_image

def ranged_image(ranged_perspective_image):
    # To get only lanes, applying filter for color(white)
# =============================================================================
#     For debugging:
#     print('ranged_perspective_image',ranged_perspective_image.shape)
# =============================================================================
    lower_color_range = 170
    upper_color_range = 255
    lower_bound = np.array([lower_color_range,lower_color_range,lower_color_range]) 
    upper_bound = np.array([upper_color_range,upper_color_range,upper_color_range])
    
    # Define the masked area
    
    # =============================================================================
    # This returns a gray scale img so no need to convert to gray scale in canny function
    ranged_perspective_image = cv2.inRange(ranged_perspective_image, lower_bound, upper_bound)
    # =============================================================================
    return ranged_perspective_image

def canny(lanes_image):
    blur = cv2.GaussianBlur(lanes_image,(5,5),0)
    canny = cv2.Canny(blur,50,150) 
    return canny

def find_lanes(gray_rc_combined_image):
    histogram = []
    normalized_rc_combined_image = (gray_rc_combined_image)/255 # gray_rc_combined_image remember
    for i in range(width):
        sum=0
        for row in range(0,height):
            sum+=round(normalized_rc_combined_image[row][i],2)
        histogram.append(sum)
# =============================================================================
#     For debugging:
#     print('histogram',np.array(histogram).shape)
# =============================================================================
    
    #  indexes for array indexing
    start = 0
    mid = math.floor(len(histogram)/2)
    end = len(histogram)    
# =============================================================================
#     For debugging:
#     print(mid,end)
#     checking histogram 
#     print(histogram[start:mid])
# =============================================================================
    
    # getting left and right lane positions
    left  = histogram.index(max(histogram[start:mid]))
    right = histogram[mid:end].index(max(histogram[mid:end]))+mid

    rc_combined_image = cv2.cvtColor(gray_rc_combined_image,cv2.COLOR_GRAY2RGB) # convert to RGB
    
    #After determinig lane poistions drawing line on them thats almost overlaps them
    
    cv2.line(rc_combined_image,(left,0),(left,height),(0,0,255),line_thickness)
    cv2.line(rc_combined_image,(right,0),(right,height),(0,0,255),line_thickness)
    return rc_combined_image,left,right

def get_centers_and_turn(lined_rc_combined_image,left,right):
    lane_center = int(((right-left)/2)+left)
    frame_center = 180
# =============================================================================
#     For debugging:
#     print('lc',lane_center)
# =============================================================================
    cv2.line(lined_rc_combined_image,(lane_center,0),(lane_center,height),(255,0,255),line_thickness) # pink
    cv2.line(lined_rc_combined_image,(frame_center,0),(frame_center,height),(0,255,0),line_thickness) # Green
    turn_value = frame_center - lane_center
    return lined_rc_combined_image,turn_value
#%%
def image_preprocessing(): 
    image = cv2.imread('C:/Users/Bhatti/Desktop/FYP/SELF_DRIVING/new-method/current.jpeg') # image path 
    while image is  None:
        # print('empty')
        image = cv2.imread('C:/Users/Bhatti/Desktop/FYP/SELF_DRIVING/new-method/current.jpeg')
    print('done')
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = cv2.resize(image,(360,240))
    origional = np.copy(image)
    
#     For debugging:    
# =============================================================================
#     print(height,width)
#     Draw image_roi to see results
#     image_roi = region_of_interest(image,line_thickness)
#     plt.imshow(image_roi,cmap='gray')
#     plt.title('image_roi')
#     plt.show()
# =============================================================================

    
# =============================================================================
#     get perspective
#     Can run below line to check are we going right with roi 
#     perspective_image = get_perspective(width,height,image_roi)   
    perspective_image = get_perspective(width,height,origional) 
#     plt.imshow(perspective_image)
#     plt.title('perspective_image')
#     plt.show()
#     print('perspective_image',perspective_image.shape)
# =============================================================================
    

# get ranged image
    ranged_perspective_image = ranged_image(perspective_image)
# =============================================================================
#     plt.imshow(ranged_perspective_image,cmap='gray')
#     plt.title('ranged_perspective_image')
#     plt.show()
#     print('ranged_perspective_image',ranged_perspective_image.shape)
# =============================================================================
# =============================================================================
# if want to show using open cv use below lines
# cv2.imshow("ranged_perspective_image",ranged_perspective_image)
# cv2.waitKey(0)
# =============================================================================
    
# get canny image
    canny_img = canny(ranged_perspective_image)
# =============================================================================
#     plt.imshow(canny_img,cmap='gray')
#     plt.title('canny_image')
#     plt.show()
# =============================================================================
    
#  ranged and canny combined image
    gray_rc_combined_image = cv2.addWeighted(canny_img,1,ranged_perspective_image,0.8,1)
    
# find lanes
    lined_rc_combined_image,left,right = find_lanes(gray_rc_combined_image)
# =============================================================================
#     plt.imshow(lined_rc_combined_image)
#     plt.title('lined_rc_combined_image')
#     plt.show()
# =============================================================================
# =============================================================================
# cv2.imshow('rc_combined_image',rc_combined_image)
# cv2.waitKey(0)
# =============================================================================
    
    # draw centers and get turn value 
    center_lined_rc_image,turn_value = get_centers_and_turn(lined_rc_combined_image,left,right)
# =============================================================================
#     plt.imshow(center_lined_rc_image)
#     plt.title('center_lined_rc_image')
#     plt.show()
#     print('turnvalue',turn_value)
# =============================================================================
    return turn_value
image_preprocessing()
#%%
# =============================================================================
# cv2.imshow('center_lined_rc_image',center_lined_rc_image)
# cv2.waitKey(0)
# =============================================================================
#%%
# notes
# cv2.circle(image,(33 ,150),5,(255,0,0),cv2.FILLED)
#temp_img =np.array(cv2.rectangle(final_img,(i,160),(i+1,160+78),(255,255,255),1))