import random
import time

			
class vaccumCleaner(object):
    
    def __init__(self, rooms):
        self.rooms = rooms
        self.current = random.choice(list(rooms.keys()))
        self.performance = 0
			
    def move(self):
	    if self.current == 'A':
		    self.current = 'B'
		    self.performance -= 5
	    else:
		    self.current = 'A'
		    self.performance -= 5
		
	    self.check()
	
    def check(self):
	    if not self.rooms[self.current]:
		    self.clean()
	
    def clean(self):
        self.rooms[self.current] = True
        self.performance += 15
        print('Sala ' + self.current + 'foi limpa!')

def get_dirty(vc, wait):
    time.sleep(wait)
    for x in vc.rooms:
        if random.random() < 0.3:
            vc.rooms[x] = False
	
    return vc
			
rooms = {'A': True, 'B': True}
v1 = vaccumCleaner(rooms)

count = 0

while count < 600:
    
	v1 = get_dirty(v1, 5)
	v1 = get_dirty(v1, 5)
	v1.move()
	count += 10


