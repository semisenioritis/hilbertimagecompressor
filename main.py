from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
l0=2**20

# line 117, i76,201
def coordinate_locator(k):
    lcpy = l0
    Itt = 10
    Ans = []
    j = 1
    while j <= Itt:
        n = int(math.ceil((k * 4) / lcpy))
        Ans.append(n)
        lcpy = int(lcpy / 4)
        k = k - (lcpy * (n - 1))
        j = j + 1


    ############

    anscpy = Ans.copy()
    midlist = Ans.copy()
    Finans = []
    j = 1

    while j <= Itt:
        a = anscpy[0]
        r=midlist[0]
        Finans.append(r)
        midlist.pop(0)

        inercount = 0
        if a == 1:
            for b in midlist:

                if b == 2:
                    midlist[inercount] = midlist[inercount] + 2
                    # replace 2 with 4
                if b == 4:
                    midlist[inercount] = midlist[inercount] - 2
                    # replace 4 with 2

                inercount = inercount + 1

        if a == 4:
            for b in midlist:

                if b == 1:
                    midlist[inercount] = midlist[inercount] + 2
                    # replace 1 with 3
                if b == 3:
                    midlist[inercount] = midlist[inercount] - 2
                    # replace 3 with 1

                inercount = inercount + 1
        j = j + 1
        anscpy.pop(0)




    xcoordcpy= Finans.copy()
    ycoordcpy= Finans.copy()
    j=0
    for a in xcoordcpy:
      if a==2:
        xcoordcpy[j]=xcoordcpy[j]-1
      if a==3:
        xcoordcpy[j]=xcoordcpy[j]+1
      j=j+1



    j=0
    for a in ycoordcpy:
      if a==3:
        ycoordcpy[j]=ycoordcpy[j]-1
      if a==4:
        ycoordcpy[j]=ycoordcpy[j]-3
      j=j+1


    
    xbot=0
    ybot=0
    xtop=1024
    ytop=1024

    for i in xcoordcpy:
        if i==1:
            xtop= xtop-((xtop-xbot)/2)
        if i==4:
            xbot= xbot+((xtop-xbot)/2)
    xtop= int(xtop)


    for i in ycoordcpy:
        if i==1:
            ytop= ytop-((ytop-ybot)/2)
        if i==2:
            ybot= ybot+((ytop-ybot)/2)
    ytop= int(ytop)


    coordinates=[]
    coordinates.append(xtop)
    coordinates.append(ytop)

    return(coordinates)


###########################


#print(coordinate_locator(200))

############################


image1=Image.open("Spider-Man_PS4_Crouch.png")
left=0
top=0
right=1024
bottom=1024
crop_img=image1.crop((left,top,right,bottom))

l0=2**20

sqr_img_array=np.array(crop_img)



og_red_arr=[]
og_green_arr=[]
og_blue_arr=[]

j=1
while j<=1024*1024 :
    coor=coordinate_locator(j)
    xcor=coor[0]-1
    ycor=coor[1]-1
    red=sqr_img_array[xcor][ycor][0]
    green=sqr_img_array[xcor][ycor][1]
    blue=sqr_img_array[xcor][ycor][2]
    og_red_arr.append(red)
    og_green_arr.append(green)
    og_blue_arr.append(blue)
    j=j+1



rgb=3
size_cmprs= int(l0/4)
avg_arr=[[0 for i in range(rgb)]for j in range(size_cmprs)]

j=0
while j<(size_cmprs):
    avg_red = int(og_red_arr[(4*j)]) + int(og_red_arr[(4*j)+1]) + int(og_red_arr[(4*j)+2]) + int(og_red_arr[(4*j)+3])
    avg_red=int(avg_red/4)

    avg_green = int(og_green_arr[4*j]) + int(og_green_arr[4*j + 1]) + int(og_green_arr[4*j + 2]) + int(og_green_arr[4*j + 3])
    avg_green = int(avg_green / 4)

    avg_blue = int(og_blue_arr[4*j]) + int(og_blue_arr[4*j + 1]) + int(og_blue_arr[4*j + 2]) + int(og_blue_arr[4*j + 3])
    avg_blue = int(avg_blue / 4)


    avg_arr[j][0]=avg_red
    avg_arr[j][1]=avg_green
    avg_arr[j][2]=avg_blue

    j=j+1

#print(len(avg_arr))


exp_compress=[]
j=0
for i in  avg_arr:
    dupli_el=avg_arr[j]
    exp_compress.append(dupli_el)
    exp_compress.append(dupli_el)
    exp_compress.append(dupli_el)
    exp_compress.append(dupli_el)
    j=j+1

side_len=1024
fin_disp=[[0 for i in range(side_len)]for j in range(side_len)]

for i in range(l0):
    j=i+1
    fin_cord=coordinate_locator(j)
    fin_xcord=fin_cord[0]-1
    fin_ycord=fin_cord[1]-1
    loc=exp_compress[i]
    fin_disp[fin_xcord][fin_ycord]=loc
fin_fin_disp = np.array(fin_disp)

#print(fin_disp)
output_img= Image.fromarray(fin_fin_disp.astype('uint8'))
output_img.save("new_Spider-Man_PS4_Crouch.png")

'''

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math

l0 = 2 ** 22


# line 117, i76,201
def coordinate_locator(k):
    lcpy = l0
    Itt = 11
    Ans = []
    j = 1
    while j <= Itt:
        n = int(math.ceil((k * 4) / lcpy))
        Ans.append(n)
        lcpy = int(lcpy / 4)
        k = k - (lcpy * (n - 1))
        j = j + 1

    ############

    anscpy = Ans.copy()
    midlist = Ans.copy()
    Finans = []
    j = 1

    while j <= Itt:
        a = anscpy[0]
        r = midlist[0]
        Finans.append(r)
        midlist.pop(0)

        inercount = 0
        if a == 1:
            for b in midlist:

                if b == 2:
                    midlist[inercount] = midlist[inercount] + 2
                    # replace 2 with 4
                if b == 4:
                    midlist[inercount] = midlist[inercount] - 2
                    # replace 4 with 2

                inercount = inercount + 1

        if a == 4:
            for b in midlist:

                if b == 1:
                    midlist[inercount] = midlist[inercount] + 2
                    # replace 1 with 3
                if b == 3:
                    midlist[inercount] = midlist[inercount] - 2
                    # replace 3 with 1

                inercount = inercount + 1
        j = j + 1
        anscpy.pop(0)

    xcoordcpy = Finans.copy()
    ycoordcpy = Finans.copy()
    j = 0
    for a in xcoordcpy:
        if a == 2:
            xcoordcpy[j] = xcoordcpy[j] - 1
        if a == 3:
            xcoordcpy[j] = xcoordcpy[j] + 1
        j = j + 1

    j = 0
    for a in ycoordcpy:
        if a == 3:
            ycoordcpy[j] = ycoordcpy[j] - 1
        if a == 4:
            ycoordcpy[j] = ycoordcpy[j] - 3
        j = j + 1

    xbot = 0
    ybot = 0
    xtop = 2048
    ytop = 2048

    for i in xcoordcpy:
        if i == 1:
            xtop = xtop - ((xtop - xbot) / 2)
        if i == 4:
            xbot = xbot + ((xtop - xbot) / 2)
    xtop = int(xtop)

    for i in ycoordcpy:
        if i == 1:
            ytop = ytop - ((ytop - ybot) / 2)
        if i == 2:
            ybot = ybot + ((ytop - ybot) / 2)
    ytop = int(ytop)

    coordinates = []
    coordinates.append(xtop)
    coordinates.append(ytop)

    return (coordinates)


def coordinate_locator(k):
    lcpy = l0
    Itt = 11
    Ans = []
    j = 1
    while j <= Itt:
        n = int(math.ceil((k * 4) / lcpy))
        Ans.append(n)
        lcpy = int(lcpy / 4)
        k = k - (lcpy * (n - 1))
        j = j + 1

    ############

    anscpy = Ans.copy()
    midlist = Ans.copy()
    Finans = []
    j = 1

    while j <= Itt:
        a = anscpy[0]
        r = midlist[0]
        Finans.append(r)
        midlist.pop(0)

        inercount = 0
        if a == 1:
            for b in midlist:

                if b == 2:
                    midlist[inercount] = midlist[inercount] + 2
                    # replace 2 with 4
                if b == 4:
                    midlist[inercount] = midlist[inercount] - 2
                    # replace 4 with 2

                inercount = inercount + 1

        if a == 4:
            for b in midlist:

                if b == 1:
                    midlist[inercount] = midlist[inercount] + 2
                    # replace 1 with 3
                if b == 3:
                    midlist[inercount] = midlist[inercount] - 2
                    # replace 3 with 1

                inercount = inercount + 1
        j = j + 1
        anscpy.pop(0)

    xcoordcpy = Finans.copy()
    ycoordcpy = Finans.copy()
    j = 0
    for a in xcoordcpy:
        if a == 2:
            xcoordcpy[j] = xcoordcpy[j] - 1
        if a == 3:
            xcoordcpy[j] = xcoordcpy[j] + 1
        j = j + 1

    j = 0
    for a in ycoordcpy:
        if a == 3:
            ycoordcpy[j] = ycoordcpy[j] - 1
        if a == 4:
            ycoordcpy[j] = ycoordcpy[j] - 3
        j = j + 1

    xbot = 0
    ybot = 0
    xtop = 2048
    ytop = 2048

    for i in xcoordcpy:
        if i == 1:
            xtop = xtop - ((xtop - xbot) / 2)
        if i == 4:
            xbot = xbot + ((xtop - xbot) / 2)
    xtop = int(xtop)

    for i in ycoordcpy:
        if i == 1:
            ytop = ytop - ((ytop - ybot) / 2)
        if i == 2:
            ybot = ybot + ((ytop - ybot) / 2)
    ytop = int(ytop)

    coordinates = []
    coordinates.append(xtop)
    coordinates.append(ytop)

    return (coordinates)


###########################


# print(coordinate_locator(200))

############################


image1 = Image.open("3fBDYDq-marvels-spider-man-wallpapers.jpg")
ogwidth,ogheight = image1.size
left = 0
top = 0
right = 2048
bottom = 2048
crop_img = image1.crop((left, top, right, bottom))

l0 = 2 ** 22

sqr_img_array = np.array(crop_img)

og_red_arr = []
og_green_arr = []
og_blue_arr = []

j = 1
while j <= 2048 * 2048:
    coor = coordinate_locator(j)
    xcor = coor[0] - 1
    ycor = coor[1] - 1
    red = sqr_img_array[xcor][ycor][0]
    green = sqr_img_array[xcor][ycor][1]
    blue = sqr_img_array[xcor][ycor][2]
    og_red_arr.append(red)
    og_green_arr.append(green)
    og_blue_arr.append(blue)
    j = j + 1

rgb = 3
size_cmprs = int(l0 / 4)
avg_arr = [[0 for i in range(rgb)] for j in range(size_cmprs)]

j = 0
while j < (size_cmprs):
    avg_red = int(og_red_arr[(4 * j)]) + int(og_red_arr[(4 * j) + 1]) + int(og_red_arr[(4 * j) + 2]) + int(
        og_red_arr[(4 * j) + 3])
    avg_red = int(avg_red / 4)

    avg_green = int(og_green_arr[4 * j]) + int(og_green_arr[4 * j + 1]) + int(og_green_arr[4 * j + 2]) + int(
        og_green_arr[4 * j + 3])
    avg_green = int(avg_green / 4)

    avg_blue = int(og_blue_arr[4 * j]) + int(og_blue_arr[4 * j + 1]) + int(og_blue_arr[4 * j + 2]) + int(
        og_blue_arr[4 * j + 3])
    avg_blue = int(avg_blue / 4)

    avg_arr[j][0] = avg_red
    avg_arr[j][1] = avg_green
    avg_arr[j][2] = avg_blue

    j = j + 1

# print(len(avg_arr))


exp_compress = []
j = 0
for i in avg_arr:
    dupli_el = avg_arr[j]
    exp_compress.append(dupli_el)
    exp_compress.append(dupli_el)
    exp_compress.append(dupli_el)
    exp_compress.append(dupli_el)
    j = j + 1

side_len = 2048
fin_disp = [[0 for i in range(side_len)] for j in range(side_len)]

for i in range(l0):
    j = i + 1
    fin_cord = coordinate_locator(j)
    fin_xcord = fin_cord[0] - 1
    fin_ycord = fin_cord[1] - 1
    loc = exp_compress[i]
    fin_disp[fin_xcord][fin_ycord] = loc
fin_fin_disp = np.array(fin_disp)

# print(fin_disp)

output_img = Image.fromarray(fin_fin_disp.astype('uint8'))

left = 0
top = 0
right = ogwidth
bottom = ogheight
output_img = output_img.crop((left, top, right, bottom))

output_img.save("new_3fBDYDq-marvels-spider-man-wallpapers.png")
'''
