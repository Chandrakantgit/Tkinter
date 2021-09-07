from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("images..images")
##root.iconbitmap('address of icon in memory')
#python aonly supports two image type .gif and .pnm
# we have to import a libray pil (Python Image Library),we use pillow updated version of it
def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
	button_back = button(root,text="<<",command=lambda:back(image_number-1))
	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_next.grid(row=1,column=2)
	##for end condition of list

	if image_number == 4:
		button_forward=Button(root,text=">>",state=DISABLED)

	


def back(image_number):
	global my_label
	global button_forward
	global button_back 

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
	button_back = button(root,text="<<",command=lambda:back(image_number-1))
	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_next.grid(row=1,column=2)
	#at the last button fades
	if image_number == 4:
		button_forward=Button(root,text=">>",state=DISABLED)
	


my_img1=ImageTk.PhotoImage(Image.open("imagee.jpeg"))
my_img2=ImageTk.PhotoImage(Image.open("image5.jpeg"))
my_img3=ImageTk.PhotoImage(Image.open("image6.jpeg"))
my_img4=ImageTk.PhotoImage(Image.open("image7.jpeg"))

image_list = [my_img1,my_img2,my_img3,my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

button_quit=Button(root,text="Exit program",command=root.quit)
button_back=Button(root,text="<<",command=back,state=DISABLED)
button_next=Button(root,text=">>",command=lambda:forward(2))



button_quit.grid(row=1,column=1)
button_back.grid(row=1,column=0)
button_next.grid(row=1,column=2)

root.mainloop()


