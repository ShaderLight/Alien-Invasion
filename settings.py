class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (5,5,30)
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,250,0)
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3

        self.speedup_scale = 1
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0
        self.fleet_drop_speed = 5

        self.fleet_direction = 1

        self.alien_points = 10

    def increase_speed(self):
        self.bullet_speed_factor += self.speedup_scale
        self.alien_speed_factor += self.speedup_scale
        self.fleet_drop_speed  += self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
