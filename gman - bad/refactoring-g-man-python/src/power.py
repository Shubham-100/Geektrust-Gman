from src import constants

class Power:
    sx = sy = dx = dy = 0
    facing = ""
    power = 200
    movecost = 10
    turncost = 5
    moves = 0
    turns = 0
    quad = ""
    fi = ""

    def __init__(self, file):
        self.fi = file

    def readFile(self):
        f = open(self.fi, 'r')
        lines = f.readlines()
        
        for line in lines:
            tokens = line.split()
            if tokens[0] == "SOURCE":
                self.sx = int(tokens[1])
                self.sy = int(tokens[2])
                self.facing = tokens[3]

            if tokens[0] == "DESTINATION":
                self.dx = int(tokens[1])
                self.dy = int(tokens[2])
            
            if tokens[0] == "PRINT_POWER":
                x  = Power.calculatePower(self)
                print("POWER %3d" %x)

    def calculatePower(self):
        self.moves = abs(self.sx - self.dx) + abs(self.sy - self.dy)

        if self.sx == self.dx and self.dy == self.sy:
            return self.power

        # if both points are on the same line, i.e Y axis
        if self.dx == self.sx and self.sy < self.dy:
            turns = constants.map_wrt_N[self.facing]
            return self.power - (self.movecost*self.moves + self.turncost*turns)
        elif self.dx == self.sx and self.sy > self.dy:
            turns = constants.map_wrt_S[self.facing]
            return self.power - (self.movecost*self.moves + self.turncost*turns)
        
        # if both points are on the same line, i.e X axis
        if self.dy == self.sy and self.sx < self.dx:
            turns = constants.map_wrt_E[self.facing]
            return self.power - (self.movecost*self.moves + self.turncost*turns)
        elif self.dy == self.sy and self.sx > self.dx:
            turns = constants.map_wrt_W[self.facing]
            return self.power - (self.movecost*self.moves + self.turncost*turns)


        # # determine relative quadrant for destination point wrt starting point
        # NW NE
        # SW SE
        if self.dx < self.sx and self.dy > self.sy:
            quad = "NW"
        elif self.dx > self.sx and self.dy > self.sy:
            quad = "NE"
        elif self.dx < self.sx and self.dy < self.sy:
            quad = "SW"
        elif self.dx > self.sx and self.dy < self.sy:
            quad = "SE"


        # For every quadrant, there are 2 possible ways to reach it, we have to choose the one with minimum turns
        # To reach NW, we can go from Dir->N->W or Dir->W->N, calculate turns for each and choose the one with minimum turns
        if quad == "NW":
            NW = constants.map_wrt_N[self.facing]
            WN = constants.map_wrt_W[self.facing]
            turns = min(NW, WN) + 1
        elif quad == "NE":
            NE = constants.map_wrt_N[self.facing]
            EN = constants.map_wrt_E[self.facing]
            turns = min(NE, EN) + 1
        elif quad == "SW":
            SW = constants.map_wrt_S[self.facing]
            WS = constants.map_wrt_W[self.facing]
            turns = min(SW, WS) + 1
        else:
            SE = constants.map_wrt_S[self.facing]
            ES = constants.map_wrt_E[self.facing]
            turns = min(SE, ES) + 1

        f = open("out.txt", "w")
        f.write("moves"+str(self.moves))
        f.write("turns"+str(self.turns))
        f.close()

        return self.power - (self.movecost*self.moves + self.turncost*turns)
