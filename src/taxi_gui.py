import pygame
import time


class TaxiGUI:
    def __init__(self, env):
        pygame.init()
        self.env = env
        self.cell_size = 60
        self.width = env.size * self.cell_size
        self.height = (env.size * self.cell_size) + 100  # Extra space for info

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Taxi Q-Learning")

        # Load images
        self.taxi_img = pygame.transform.scale(
            pygame.image.load("assets/taxi.png"), (self.cell_size, self.cell_size))
        self.taxi_passenger_img = pygame.transform.scale(
            pygame.image.load("assets/taxi_passenger.png"), (self.cell_size, self.cell_size))
        self.wall_img = pygame.transform.scale(
            pygame.image.load("assets/wall.png"), (self.cell_size, self.cell_size))
        self.passenger_img = pygame.transform.scale(
            pygame.image.load("assets/passenger.png"), (self.cell_size, self.cell_size))
        self.destination_img = pygame.transform.scale(
            pygame.image.load("assets/destination.png"), (self.cell_size, self.cell_size))

        # Colors
        self.bg_color = (255, 255, 255)
        self.grid_color = (200, 200, 200)
        self.text_color = (0, 0, 0)

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.grid_color,
                             (x, 0), (x, self.env.size * self.cell_size))
        for y in range(0, self.env.size * self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, self.grid_color,
                             (0, y), (self.width, y))

    def draw_info_panel(self, current_reward, total_reward):
        font = pygame.font.Font(None, 30)
        y_position = self.env.size * self.cell_size + 10

        # Passenger status
        status = "Carrying passenger" if self.env.has_passenger else "Going for pickup"
        text = font.render(f"Status: {status}", True, self.text_color)
        self.screen.blit(text, (10, y_position))

        # Destination
        dest_text = font.render(f"Destination: {self.env.destination}", True, self.text_color)
        self.screen.blit(dest_text, (10, y_position + 30))

        # Rewards
        reward_text = font.render(
            f"Current Reward: {current_reward} | Total Reward: {total_reward}",
            True, self.text_color)
        self.screen.blit(reward_text, (10, y_position + 60))

    def render(self, current_reward, total_reward):
        self.screen.fill(self.bg_color)

        # Draw grid and elements
        for x in range(self.env.size):
            for y in range(self.env.size):
                rect = pygame.Rect(y * self.cell_size, x * self.cell_size,
                                   self.cell_size, self.cell_size)

                # Draw walls
                if (x, y) in self.env.walls:
                    self.screen.blit(self.wall_img, rect.topleft)

                # Draw passenger
                if (x, y) == self.env.pickup:
                    self.screen.blit(self.passenger_img, rect.topleft)

                # Draw destination
                if (x, y) == self.env.destination:
                    self.screen.blit(self.destination_img, rect.topleft)

                # Draw taxi
                if (x, y) == self.env.taxi_pos:
                    if self.env.has_passenger:
                        self.screen.blit(self.taxi_passenger_img, rect.topleft)
                    else:
                        self.screen.blit(self.taxi_img, rect.topleft)

        self.draw_grid()
        self.draw_info_panel(current_reward, total_reward)
        pygame.display.flip()

    def close(self):
        pygame.quit()