import pygame

import sys
import pygame
import sys

class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 20
        self.color = (255, 0, 0)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Difficulty Selection")

font = pygame.font.Font(None, 36)
text = font.render("Choose Difficulty: Press 'e' for Easy, 'm' for Medium, 'h' for Hard", True, (0, 0, 0))
text_rect = text.get_rect(center=(400, 300))

ball = Ball(400, 900, 10)  # Default ball speed

print("Selected Difficulty - Ball Speed:", ball.speed)
pygame.init()

# Main loop for difficulty selection
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                ball.speed = 3  # Easy difficulty
                running = False
            elif event.key == pygame.K_m:
                ball.speed = 5  # Medium difficulty
                running = False
            elif event.key == pygame.K_h:
                ball.speed = 10  # Hard difficulty
                running = False

    ball.update()
    ball.draw(screen)

    pygame.display.flip()

# Main game loop with the selected ball speed
print("Selected Difficulty - Ball Speed:", ball.speed)
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("welocome to pong!!")

# Font setup
font = pygame.font.Font(None, 36)
text = font.render("Press Space to Start", True, (0, 0, 0))
text_rect = text.get_rect(center=(400, 300))

# Main loop for the title screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False  # Exit the title screen loop

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Display the text
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Start your main game loop here
# Include your existing game code or import your game script here


# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
blue = (51, 255, 255)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock() 
FPS = 30

# Striker class


class Striker:
		# Take the initial position, dimensions, speed and color of the object
	def __init__(self, posx, posy, width, height, speed, color):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		# Rect that is used to control the position and collision of the object
		self.geekRect = pygame.Rect(posx, posy, width, height)
		# Object that is blit on the screen
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	# Used to display the object on the screen
	def display(self):
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	def update(self, yFac):
		self.posy = self.posy + self.speed*yFac

		# Restricting the striker to be below the top surface of the screen
		if self.posy <= 0:
			self.posy = 0
		# Restricting the striker to be above the bottom surface of the screen
		elif self.posy + self.height >= HEIGHT:
			self.posy = HEIGHT-self.height

		# Updating the rect with the new values
		self.geekRect = (self.posx, self.posy, self.width, self.height)

	def displayScore(self, text, score, x, y, color):
		text = font20.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)

		screen.blit(text, textRect)

	def getRect(self):
		return self.geekRect

# Ball class

class Ball:
	def __init__(self, posx, posy, radius, speed, color):
		self.posx = posx
		self.posy = posy
		self.radius = radius
		self.speed = speed
		self.color = color
		self.xFac = 1
		self.yFac = -1
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius)
		self.firstTime = 1

	def display(self):
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius)

	def update(self):
		self.posx += self.speed*self.xFac
		self.posy += self.speed*self.yFac

		# If the ball hits the top or bottom surfaces, 
		# then the sign of yFac is changed and 
		# it results in a reflection
		if self.posy <= 0 or self.posy >= HEIGHT:
			self.yFac *= -1

		if self.posx <= 0 and self.firstTime:
			self.firstTime = 0
			return 1
		elif self.posx >= WIDTH and self.firstTime:
			self.firstTime = 0
			return -1
		else:
			return 0

	def reset(self):
		self.posx = WIDTH//2
		self.posy = HEIGHT//2
		self.xFac *= -1
		self.firstTime = 1

	# Used to reflect the ball along the X-axis
	def hit(self):
		self.xFac *= -1

	def getRect(self):
		return self.ball

# Game Manager


def main():
	running = True

	# Defining the objects
	geek1 = Striker(20, 0, 10, 100, 10, blue)
	geek2 = Striker(WIDTH-30, 0, 10, 100, 10, blue)
	ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

	listOfGeeks = [geek1, geek2]

	# Initial parameters of the players
	geek1Score, geek2Score = 0, 0
	geek1YFac, geek2YFac = 0, 0

	while running:
		screen.fill(BLACK)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					geek2YFac = -1
				if event.key == pygame.K_DOWN:
					geek2YFac = 1
				if event.key == pygame.K_w:
					geek1YFac = -1
				if event.key == pygame.K_s:
					geek1YFac = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					geek2YFac = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					geek1YFac = 0

		# Collision detection
		for geek in listOfGeeks:
			if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
				ball.hit()

		# Updating the objects
		geek1.update(geek1YFac)
		geek2.update(geek2YFac)
		point = ball.update()

		# -1 -> PLAYER 1 has scored
		# +1 -> PLAYER 2 has scored
		# 0 -> None of them scored
		if point == -1:
			geek1Score += 1
		elif point == 1:
			geek2Score += 1

		# Someone has scored
		# a point and the ball is out of bounds.
		# So, we reset it's position
		if point: 
			ball.reset()

		# Displaying the objects on the screen
		geek1.display()
		geek2.display()
		ball.display()

		# Displaying the scores of the players
		geek1.displayScore("PLAYER 1 : ", 
						geek1Score, 100, 20, WHITE)
		geek2.displayScore("PLAYER 2 : ", 
						geek2Score, WIDTH-100, 20, WHITE)

		pygame.display.update()
		clock.tick(FPS)	 

if __name__ == "__main__":
	main()
	pygame.quit()
