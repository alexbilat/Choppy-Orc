_author_ = "Alex Bilat"
_date_ = "2025/01/17"
_version_ = "1.12.2"
_filename_ = "username.py"
_description_ = "Creates text input on last level, saves to file"

from settings import *

class Username(pygame.sprite.Sprite):
    def __init__(self):
        """Unit username (but also end screen)"""
        super().__init__()
        pygame.font.init()
        self.font = pygame.font.Font('font/font.ttf', 50)
        self.text = ""
        self.active = False
        self.color_active = pygame.Color('dodgerblue2')
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color = self.color_inactive
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_blink_time = 500
        self.box_padding = 10
        self.width = 700
        self.height = 60
        self.box_rect = pygame.Rect((SCREEN_WIDTH - self.width) // 2, 400, self.width, self.height)
        self.saved = False
        self.save_button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, 500, 200, 60)
        self.continue_button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, 600, 200, 60)
        self.continue_clicked = False
        self.continue_surf = pygame.image.load('images/buttons/continue.png').convert()
        self.continue_rect = self.continue_surf.get_rect(center = (SCREEN_WIDTH//2, 800))
        self.score = None
        ts = time.time()
        self.date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def save_score(self, score_value):
        """Save username and score to file"""
        with open('highscores.txt', 'a') as file:
            file.write(f"\nName: {self.text}\nScore: {score_value}\nDate: {self.date}\n") #Actually write inside the highscores file
        self.saved = True         

    def handle_event(self, events, score):
        """Handle typing and clicking save"""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN: #Click the save button
                if self.save_button_rect.collidepoint(event.pos) and not self.saved:
                    self.save_score(score)
                    self.active = False
                    self.color = self.color_inactive
                    return score
                
                if self.saved and self.continue_rect.collidepoint(event.pos): #Return back to the start
                    return 'start'
                
                if not self.saved: #Change color of the box to show you're interacting
                    if self.box_rect.collidepoint(event.pos):
                        self.active = True
                        self.color = self.color_active
                    else:
                        self.active = False
                        self.color = self.color_inactive

            if not self.saved and event.type == pygame.KEYDOWN and self.active: #Allow typing under 15 chars (backspace always allowed)
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 15:
                        self.text += event.unicode
        return None

    def update(self):
        """Cursor blinking"""
        #Cursor blinking update
        current_time = pygame.time.get_ticks()
        if (current_time - self.cursor_timer >= self.cursor_blink_time):
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = current_time

    def draw(self, screen):
        """Drawing all elements of the endscreen"""
        #Box
        pygame.draw.rect(screen, self.color, self.box_rect, 2)
        
        #Text
        prompt = self.font.render("Enter username:", True, 'white')
        prompt_rect = prompt.get_rect(bottom=self.box_rect.top - 10, centerx=self.box_rect.centerx)
        screen.blit(prompt, prompt_rect)

        #Input
        text_surface = self.font.render(self.text, True, 'white')
        text_rect = text_surface.get_rect(center=self.box_rect.center)
        screen.blit(text_surface, text_rect)

        #Cursor
        if self.active and self.cursor_visible:
            cursor_x = text_rect.right + 2
            cursor_y = self.box_rect.centery - self.font.get_height() // 2
            pygame.draw.line(screen, 'white', (cursor_x, cursor_y), 
                           (cursor_x, cursor_y + self.font.get_height()), 2)
        
        #Save button
        button_color = 'grey' if self.saved else 'white'
        pygame.draw.rect(screen, button_color, self.save_button_rect, 2)
        save_text = self.font.render("Save", True, button_color)
        save_text_rect = save_text.get_rect(center=self.save_button_rect.center)
        screen.blit(save_text, save_text_rect)

        #Continue 
        screen.blit(self.continue_surf, self.continue_rect)

    