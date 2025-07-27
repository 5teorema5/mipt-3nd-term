class GasHolder:
    def __init__(self, V):
        if V < 0:
            raise Exception(ValueError)
        self.V = V
        self.T = 273  # K
        self.m = []
        self.M = []

    def inject(self, m, M):
        if m < 0 or M < 0:
            raise Exception(ValueError)
        self.m.append(m)
        self.M.append(M)

    def heat(self, dT):
        self.T += dT

    def cool(self, dT):
        if self.T - dT < 0:
            self.T = 0
        else:
            self.T -= dT

    def get_pressure(self):
        p = 0
        for i in range(len(self.m)):
            p += (self.m[i] / self.M[i]) * 8.31 * self.T / self.V
        return round(p, 2)


h = GasHolder(1.0)
h.inject(29, 29)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.inject(29, 29)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.heat(273)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.cool(373)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.cool(373)
print(f'Pressure after operation: {h.get_pressure()} Pa')
