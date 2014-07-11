__author__ = 'Jerry Ling'


from Tkinter import *
import math


def rgb_to_web(n):
    return '#%02x%02x%02x' % tuple(n) #RGB convert to web color
#wavelengthto RGB: http://rohanhill.com/tools/WaveToRGB/index.asp?
#                  http://www.midnightkite.com/color.html


def wav2rgb(wavelength):
    w = int(wavelength)

    # colour
    if w >= 380 and w < 440:
        R = -(w - 440.) / (440. - 350.)
        G = 0.0
        B = 1.0
    elif w >= 440 and w < 490:
        R = 0.0
        G = (w - 440.) / (490. - 440.)
        B = 1.0
    elif w >= 490 and w < 510:
        R = 0.0
        G = 1.0
        B = -(w - 510.) / (510. - 490.)
    elif w >= 510 and w < 580:
        R = (w - 510.) / (580. - 510.)
        G = 1.0
        B = 0.0
    elif w >= 580 and w < 645:
        R = 1.0
        G = -(w - 645.) / (645. - 580.)
        B = 0.0
    elif w >= 645 and w <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    # intensity correction
    if w >= 380 and w < 420:
        SSS = 0.3 + 0.7*(w - 350) / (420 - 350)
    elif w >= 420 and w <= 700:
        SSS = 1.0
    elif w > 700 and w <= 780:
        SSS = 0.3 + 0.7*(780 - w) / (780 - 700)
    else:
        SSS = 0.0
    SSS *= 255
    return [int(SSS*R), int(SSS*G), int(SSS*B)]


def resize(ev=NONE):
    clocklabel1.config(font='Helvetica -%d bold' % scale.get())
    clocklabel2.config(font='Helvetica -%d bold' % scale.get())


def dopplerperiod(period,v):
    return period*(100+v)/100


def relat_dopplerperiod(period,v):
    return dopplerperiod(period,v)/math.sqrt(1.0-(v/100)*(v/100))


def sync():
    clock2.digit=clock3.digit
    clock1.digit=clock3.digit


def reset():
    clock1.digit=0
    clock2.digit=0
    clock3.digit=0


class Clocks(object):
    def __init__(self, period, wavelength, clocknumber):
        self.init_period = period
        self.out_period = self.init_period
        self.init_wavelength = wavelength
        self.out_wavelength = self.init_wavelength
        self.color = rgb_to_web(wav2rgb(wavelength))
        self.digit = 0
        self.clocknum = clocknumber

    def adjust_period(self):
        if self.clocknum == 1:
            self.out_period = dopplerperiod(self.init_period, float(speed.get()))
        if self.clocknum == 2:
            self.out_period = relat_dopplerperiod(self.init_period, float(speed.get()))

    def tick(self):
        if self.clocknum == 1:
            self.adjust_period()
            self.out_wavelength = self.init_wavelength/(1.0-speed.get()/100.0)
            self.color = rgb_to_web(wav2rgb(self.out_wavelength))
            clock1frequency.configure(text=str(round((3*10**8)/self.out_wavelength/1000, 3))+" THz\n"+str(round(self.out_wavelength, 3))+"nm")
            if clockpow1.get() == 1:
                self.digit += 1
                clocklabel1.configure(text=self.digit, fg=self.color)
        elif self.clocknum == 2:
            self.out_wavelength = (self.init_wavelength/(1.0-speed.get()/100.0))*math.sqrt(1.0+(float(speed.get())/100.0)**2)
            self.color = rgb_to_web(wav2rgb(self.out_wavelength))
            clock2frequency.configure(text=str(round((3*10**8)/self.out_wavelength/1000, 3))+" THz\n"+str(round(self.out_wavelength, 3))+"nm")
            if clockpow2.get() == 1:
                self.digit += 1
                clocklabel2.configure(text=self.digit, fg=self.color)
        elif self.clocknum == 3:
            clock3frequency.configure(text=str(round((3*10**8)/self.out_wavelength/1000, 3))+" THz\n"+str(round(self.out_wavelength, 3))+"nm")
            if clockpow3.get() == 1:
                self.digit += 1
                clocklabel3.configure(text=self.digit, fg=self.color)
        self.adjust_period()
        top.after(int(self.out_period), self.tick)
clock1 = Clocks(300.0, 560.0, 1)
clock2 = Clocks(300.0, 560.0, 2)
clock3 = Clocks(300.0, 560.0, 3)


top = Tk()
top.title("Ticking rate simulation")
top.geometry('1000x800')

speed = Scale(top, from_=-99.0, to=99.0, orient=HORIZONTAL, length=100)
speed.set(0)

clockpow1 = IntVar()
clockpow2 = IntVar()
clockpow3 = IntVar()

clocklabel1 = Label(top, text=clock1.digit, font='Helvetica -70 bold', fg=clock1.color)
clocklabel1.pack(fill=Y, expand=1)
clock1frequency = Label(text=str(round((3*10**8)/clock1.out_wavelength/1000, 3))+" nm")
clock1frequency.pack()

clocklabel2 = Label(top, text=clock2.digit, font='Helvetica -70 bold', fg=clock2.color)
clocklabel2.pack(fill=Y, expand=1)
clock2frequency = Label(text=str(round((3*10**8)/clock2.out_wavelength/1000, 3))+" nm")
clock2frequency.pack()

label2 = Label(top, text='===================ONLY THE RATE OF TICKING IS MEANINGFUL======================', font='Helvetica -20 bold', fg="#C70000")
label2.pack(fill=Y, expand=1)

clocklabel3 = Label(top, text=clock2.digit, font='Helvetica -70 bold', fg=clock1.color)
clocklabel3.pack(fill=Y, expand=1)
clock3frequency = Label(text=str(round((3*10**8)/clock3.out_wavelength/1000, 3))+" nm")
clock3frequency.pack()

clock1.tick()
clock2.tick()
clock3.tick()

speed.pack(fill=X, expand=1)

check1 = Checkbutton(top, text="Clock1", variable=clockpow1, onvalue=1, offvalue=0)
check1.pack()
check2 = Checkbutton(top, text="Clock2", variable=clockpow2, onvalue=1, offvalue=0)
check2.pack()
check3 = Checkbutton(top, text="Clock3", variable=clockpow3, onvalue=1, offvalue=0)
check3.pack()


sync = Button(text='Sync clocks', command=sync, activeforeground='white', activebackground='red')
sync.pack()

reset = Button(text='reset to zero', command=reset, activeforeground='white', activebackground='red')
reset.pack()

quit1 = Button(text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit1.pack()
mainloop()