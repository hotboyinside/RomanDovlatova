class Stats:
    """Данные о игроке"""
    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """статистика изменяющееся вовремя игры"""
        self.player_life = 3
        self.score = 0
