import matplotlib.pyplot as plt
import time
import numpy as np

class KurvaBezier_Brute_Force:
    def __init__(self,points):
        self.kurvaPoints = []
        self.midPoints = []
        self.points = points
        self.eksekusi = 0
       
    def getTime(self):
        return self.eksekusi
     
    def count_midpoint(self, p0, p1):
        return ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    
    def Brute_Force(self,points,iterasi):
        start = time.time()
        self.midPoints = [self.count_midpoint(points[i], points[i+1]) for i in range(len(points) - 1)]        
        for _ in range(iterasi - 1):
            tempKurvaPoints = [self.count_midpoint(self.midPoints[j], self.midPoints[j+1]) for j in range(len(self.midPoints) - 1)]
            tempKurvaPoints.insert(0, points[0])
            tempKurvaPoints.append(points[-1])
            self.kurvaPoints = tempKurvaPoints[:]
            tempMidPoints = []
            while self.midPoints:
                tempMidPoints.append(self.count_midpoint(tempKurvaPoints[0], self.midPoints[0]))
                if len(tempMidPoints) % 2 == 0:
                    self.midPoints.pop(0)
                else:
                    tempKurvaPoints.pop(0)
            self.midPoints = tempMidPoints[:]
        tempKurvaPoints = [self.count_midpoint(self.midPoints[j], self.midPoints[j+1]) for j in range(len(self.midPoints) - 1)]
        tempKurvaPoints.insert(0, points[0])
        tempKurvaPoints.append(points[-1])
        self.kurvaPoints = tempKurvaPoints[:]
        self.eksekusi = time.time() - start
        self.draw_kurva()
        
    def draw_kurva(self):
        plt.scatter([p[0] for p in self.points], [p[1] for p in self.points], color='blue', label='Control Points')
        plt.plot([p[0] for p in self.points], [p[1] for p in self.points], 'b--')
        poin = np.array(self.kurvaPoints)
        plt.plot(poin[:, 0], poin[:, 1], 'r-', label='Bezier Curve')
        plt.grid(True)