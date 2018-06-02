from wifi import Cell, Scheme

cell = Cell.all('wlp3s0')[0]
scheme = Scheme.for_cell('wlp3s0', 'home', cell, passkey)
scheme.save()
scheme.activate()

scheme = Scheme.find('wlp3s0', 'home')
scheme.activate()
