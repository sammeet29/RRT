'''
Sammeet Koli
skoli@uncc.edu
Uncc
Draws random obstacles and uses RRT to find a path without colliding with them
'''
from Graph import my_Graph
from Vertex import my_Vertex
from dfs import Dfs
import pygame
import math
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
NO_OF_VERTEX = 1000

class Block(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self. image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class move_on_line:
    def __init__(self,start_x,start_y,end_x,end_y):
        #calculate steps depending on length
        #initialize the dot at start of line
        self.pos_x = start_x
        self.pos_y = start_y
        self.end_x =end_x
        self.end_y = end_y
        dy = end_y-start_y
        dx = end_x-start_x
        angle = math.atan2(dy,dx)
        self.frac_y = (math.sin(angle) * 5)
        self.frac_x = (math.cos(angle) * 5)
        self.endLine = True
        # decide fraction
        dist = math.sqrt(dy**2 + dx**2)
        print dist
        self.count = int(dist/5) 
        print self.count
        
    def move(self):
        #caculate and update the pos depending on step
        self.pos_x = self.pos_x + self.frac_x
        self.pos_y = self.pos_y + self.frac_y
        
    def render(self):
        #use this function to move on the line
        self.move()
        if self.count<=0:
            self.endLine = False
        #display point
        elif self.count == 1:
            #print "count: %s x:%s y:%s" %(self.count,self.end_x,self.end_y)
            self.count = self.count - 1
        else:
            #print "count: %s x:%s y:%s" %(self.count,int(self.pos_x),int(self.pos_y))
            self.count = self.count - 1

def draw_circle(screen, pos, color):
    pygame.draw.circle(screen, color, pos, 5, 0)
   
def draw_path(screen, graph,  start_ver, end_ver):
    dfs_obj = Dfs(graph, start_ver, end_ver)
    stack = dfs_obj.printPath()

def main():
    graph = my_Graph()
    game_running = True
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    start_rrt, complete_rrt, got_dest = False, False, False
    no_of_vertex = NO_OF_VERTEX
    count = 1
    init , goal = 0, 0
    
    obs = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()
    
    #create obstacles
    for i in range(10):
        x = random.randrange(SCREEN_WIDTH)
        y = random.randrange(SCREEN_HEIGHT)
        width = random.randint(50, 100)
        height = random.randint(50, 100)
        block = Block(x,y, width, height)
        obs.add(block)
    
    #create a bot 
    bot = Block(0, 0, 5, 5)
    
    
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                val = pygame.mouse.get_pressed()
                if val[0]:
                    pos_start = pygame.mouse.get_pos()
                    start_ver = graph.addVertex(count, pos_start[0], pos_start[1])     #used to find path later
                    init = count
                    count += 1
                    #pygame.draw.circle(screen,  GREEN, pos_start, 5, )
                    draw_circle(screen, pos_start, GREEN)
                    start_rrt = True
                elif val[2]:
                    pos_end = pygame.mouse.get_pos()
                    ver=graph.getNearestNode(pos_end[0], pos_end[1])
                    end_ver=graph.addVertex(count, pos_end[0], pos_end[1])              #used to find path later
                    graph.addEdge(end_ver.getId(), ver.getId())
                    pygame.draw.line(screen,PURPLE, (ver.posx, ver.posy), pos_end, 2 )
                    draw_circle(screen, pos_end, RED)
                    goal = count
                    count += 1
                    got_dest = True
                    print end_ver, ver
                print "mouse down", val
        '''
        Draws a rrt graph. Extends edges until it meets the point or obstacle.
        Adds the vertex and edge to the graph
        '''        
        if start_rrt:    
            x_rand = random.randrange(SCREEN_WIDTH)
            y_rand = random.randrange(SCREEN_HEIGHT)
            fv = graph.getNearestNode(x_rand, y_rand)
            line = move_on_line(fv.posx, fv.posy, x_rand, y_rand)
            while line.endLine:             #checks if it reached the end of line
                line.render()
                bot.rect.x = int(line.pos_x)
                bot.rect.y = int(line.pos_y)
                collide = pygame.sprite.spritecollide(bot, obs, False)
                if collide:
                    break
            tv = graph.addVertex(count, bot.rect.x, bot.rect.y)
            count += 1
            graph.addEdge(fv.getId(), tv.getId())
            pygame.draw.line(screen, BLUE, (fv.posx, fv.posy), (bot.rect.x, bot.rect.y), 1)
            
            if count>no_of_vertex:
                start_rrt = False
                complete_rrt = True
        '''Draw path from init to goal only if rrt is drawn and final position is recieved'''
        
        if complete_rrt and got_dest:
            fv = graph.getVertex(init)
            tv = graph.getVertex(goal)
            dfs_obj = Dfs(graph, fv, tv)
            stack = dfs_obj.printPath()
            #print "path", stack
            for i in range(len(stack)-1):
                a,b = stack[i],stack[i+1]
                pygame.draw.line(screen,RED, (a.getPosX(),a.getPosY()),(b.getPosX(),b.getPosY()),2)
                pygame.display.update()
        
        
        
        obs.draw(screen)
        pygame.display.update()
        #clock.tick(10)

if __name__ == "__main__":
    main()
