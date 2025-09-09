import time
import os

def load_world(filename):
    world = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = []
            for c in line:
                if c == "#":
                    row.append(True)
                else:
                    row.append(False)
            world.append(row)
    return world
        
        
def espandi_world(world, larghezza, altezza):
    new_world = [[False] * larghezza for _ in range(altezza)]
    offset_x = (altezza - len(world)) // 2
    offset_y = (larghezza - len(world[0])) // 2

    for x in range(len(world)):
        for y in range(len(world[0])):
            new_world[offset_x + x][offset_y + y] = world[x][y]

    return new_world


        
def numero_celle_vive_nei_dintorni(world, x, y):
    numero_celle = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(world) and 0 <= ny < len(world[0]):
                if world[nx][ny]:
                    numero_celle += 1
  
    return numero_celle


def stampa_world(world):
    for riga in world:
        for cella in riga:
            if cella:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def un_ciclo(world):
    new_world = [[world[x][y] for y in range(len(world[0]))] for x in range(len(world))]
    for x in range(len(world)):
        for y in range(len(world[0])):
            numero_vicini_vivi = numero_celle_vive_nei_dintorni(world, x, y)
            if world[x][y]:
                if numero_vicini_vivi < 2 or numero_vicini_vivi > 3:
                    new_world[x][y] = False
                else: 
                    new_world[x][y] = True
            else:
                if numero_vicini_vivi == 3:
                    new_world[x][y] = True
                
    return new_world
            

if __name__ == "__main__":
    world = load_world("./world.txt")
    world = espandi_world(world, 40, 40)
    while True:
        world = un_ciclo(world)
        stampa_world(world)
        time.sleep(0.2)
        os.system('clear')
    