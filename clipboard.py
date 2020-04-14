import tkinter

def add_to_clipboard(STR):

	TmpWinodw = tkinter.Tk()

	TmpWinodw.withdraw()		# hides the window

	TmpWinodw.clipboard_append(STR)

	print(TmpWinodw.clipboard_get())

	t = 124

	TmpWinodw.after(t, TmpWinodw.destroy)	 # make the window disappears after t-ms

	TmpWinodw.mainloop()		# force Windows to recognize the path added to the clipboard

	return STR

