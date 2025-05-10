from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("Myne Tower Defense")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 70)
small_font = pygame.font.Font(None, 35)

what_window = "menu"
rect_start = pygame.Rect(size_window[0]//2 - 125, 200, 250, 80)
rect_end = pygame.Rect(size_window[0]//2 - 125, 350, 250, 80)
rect_leave = pygame.Rect(0, 0, 100, 50)
text_start = font.render("START", True, BLACK)
text_end = font.render("END", True, BLACK)
text_leave = small_font.render("LEAVE", True, BLACK)

wave = 1
mob_spawn_timer = 0
mob_spawn_delay = 60
mob_index = 0
mobs_per_wave = 5
current_wave_mobs = []

game = True

while game:
    events = pygame.event.get()

    if what_window == "menu":
        window.blit(menu_background_image, (0, 0))
        
        pygame.draw.rect(window, GREEN, rect_start)
        pygame.draw.rect(window, RED, rect_end)

        window.blit(text_start, (rect_start.centerx - font.size("START")[0] // 2, rect_start.centery - font.size("START")[1] // 2))
        window.blit(text_end, (rect_end.centerx - font.size("END")[0] // 2, rect_end.centery - font.size("END")[1] // 2))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if rect_start.collidepoint(x, y):
                    what_window = "game"
                    wave = 1
                    mob_index = 0
                    mobs_per_wave = 5
                    current_wave_mobs = []
                    mob_spawn_timer = 0
                elif rect_end.collidepoint(x, y):
                    game = False

    elif what_window == "game":
        window.blit(background_image, (0, 0))

        pygame.draw.rect(window, RED, rect_leave)
        window.blit(text_leave, (rect_leave.centerx - small_font.size("LEAVE")[0] // 2, rect_leave.centery - small_font.size("LEAVE")[1] // 2))

        wave_text = small_font.render(f"Wave: {wave}", True, BLACK)
        window.blit(wave_text, (size_window[0] - 200, 10))

        mob_spawn_timer += 1
        if mob_spawn_timer >= mob_spawn_delay and mob_index < mobs_per_wave:
            current_wave_mobs.append(Mob(path))
            mob_index += 1
            mob_spawn_timer = 0

        for mob in current_wave_mobs:
            mob.move()
            mob.draw(window)

        current_wave_mobs = [mob for mob in current_wave_mobs if mob.current_point < len(path) - 1]

        if len(current_wave_mobs) == 0 and mob_index >= mobs_per_wave:
            wave += 1
            mob_index = 0
            mobs_per_wave += 2
            mob_spawn_timer = 0

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if rect_leave.collidepoint(x, y):
                    what_window = "menu"

            if event.type == pygame.QUIT:
                game = False

    clock.tick(FPS)
    pygame.display.flip()
