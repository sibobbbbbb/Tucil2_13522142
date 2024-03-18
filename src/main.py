from tkinter import *
from Divide_n_Conquer import *
from Brute_Force import *
from matplotlib.animation import FuncAnimation

class App:
    def __init__(self, master):
        self.master = master
        master.title("Kurva Bezier")

        self.label = Label(master, text="Masukkan 3 titik koordinat dalam bentuk tuple seperti (0, 0)")
        self.label.pack()
        
        self.label = Label(master, text="Titik 1")
        self.label.pack()
        self.p0_entry = Entry(master)
        self.p0_entry.pack()
        
        self.label = Label(master, text="Titik 2")
        self.label.pack()
        self.p1_entry = Entry(master)
        self.p1_entry.pack()
        
        self.label = Label(master, text="Titik 3")
        self.label.pack()
        self.p2_entry = Entry(master)
        self.p2_entry.pack()
        
        self.label = Label(master, text="Masukkan jumlah iterasi")
        self.label.pack()
        self.iterasi_entry = Entry(master)
        self.iterasi_entry.pack()

        self.label = Label(master, text="Pilih metode perhitungan:")
        self.label.pack()
        self.label = Label(master, text="1. Divide and Conquer")
        self.label.pack()
        self.label = Label(master, text="2. Brute Force")
        self.label.pack()

        self.choice_entry = Entry(master)
        self.choice_entry.pack()

        self.calculate_button = Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        p0 = eval(self.p0_entry.get())
        p1 = eval(self.p1_entry.get())
        p2 = eval(self.p2_entry.get())
        iterasi = int(self.iterasi_entry.get())
        choice = int(self.choice_entry.get())

        if choice == 1 :
            self.DivideNConquer([p0, p1, p2], iterasi)
        else:
            self.Bruteforce([p0, p1, p2], iterasi)

    def Bruteforce(self, points, iterasi):
        print("-------------------------Brute Force------------------------------")
        print("==================================================================")
        print("Berikut adalah hasil dari kurva bezier dengan iterasi sebanyak", iterasi)
        kurva_bf = KurvaBezier_Brute_Force(points)
        kurva_bf.Brute_Force(points, iterasi)
        print("Waktu eksekusi : ", kurva_bf.getTime() , "detik")
        plt.show()
        print("==================================================================")

    def DivideNConquer(self, points, iterasi):
        print("----------------------Divide and Conquer--------------------------")
        print("==================================================================")
        print("Berikut adalah hasil dari kurva bezier dengan iterasi sebanyak", iterasi)
        kurva_dnc = KurvaBezier_DNC(points)
        animasi = FuncAnimation(plt.gcf(), kurva_dnc.animasi, frames=iterasi+1,repeat=False)
        plt.show()
        print("Waktu eksekusi : ", kurva_dnc.getTime() , "detik")
        print("==================================================================")

root = Tk()
app = App(root)
root.mainloop()