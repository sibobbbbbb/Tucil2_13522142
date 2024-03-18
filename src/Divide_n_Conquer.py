import matplotlib.pyplot as plt
import time
import numpy as np

class KurvaBezier_DNC:
    def __init__(self,points):
        self.points = points
        self.kurvaPoints = []
        self.eksekusi = 0
            
    def count_midpoint(self, p0, p1):
        return ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    
    def getTime(self):
        return self.eksekusi

    def startDNC(self, points, iterasi):
        self.kurvaPoints = []
        self.kurvaPoints.append(points[0])
        self.DNC(points, iterasi)
        self.kurvaPoints.append(points[2])
    
    def DNC(self,points,iterasi):
        start_time = time.time()  # Waktu mulai iterasi
        if iterasi == 0:
            return
        else:
            left_mid = self.count_midpoint(points[0], points[1])
            right_mid = self.count_midpoint(points[1], points[2])
            hasil_mid = self.count_midpoint(left_mid, right_mid)
            
            self.DNC([points[0], left_mid, hasil_mid], iterasi-1)
            self.kurvaPoints.append(hasil_mid)
            self.DNC([hasil_mid, right_mid, points[2]], iterasi-1)
        self.eksekusi += time.time() - start_time  # Waktu eksekusi iterasi
  
    def draw_kurva(self):
        poin = np.array(self.kurvaPoints)
        plt.plot(poin[:, 0], poin[:, 1], 'r-', label='Bezier Curve')
        
    def animasi(self, frame):
        plt.cla()
        plt.scatter([p[0] for p in self.points], [p[1] for p in self.points], color='blue', label='Control Points')
        plt.plot([p[0] for p in self.points], [p[1] for p in self.points], 'b--')
        self.startDNC(self.points, frame)
        if frame != 0:
            self.draw_kurva()
        plt.title(f"Kurva Bezier iterasi ke-{frame}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')