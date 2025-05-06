# Патерн Strategy
class WalkingStrategy:
    def walk(self):
        pass

class NormalWalk(WalkingStrategy):
    def walk(self):
        print("Робот іде звичайно.")

class FastWalk(WalkingStrategy):
    def walk(self):
        print("Робот іде швидко.")

# Патерн State
class RobotState:
    def handle(self):
        pass

class ChargedState(RobotState):
    def handle(self):
        print("Робот працює в повному режимі.")

class LowBatteryState(RobotState):
    def handle(self):
        print("Робот сповільнюється через низький заряд.")

# Клас Robot
class Robot:
    def __init__(self):
        self.walking_strategy = NormalWalk()
        self.state = ChargedState()

    def set_strategy(self, strategy: WalkingStrategy):
        self.walking_strategy = strategy

    def set_state(self, state: RobotState):
        self.state = state

    def move(self):
        self.state.handle()
        self.walking_strategy.walk()

# Основна програма
if __name__ == "__main__":
    robot = Robot()
    robot.move()

    print("\n🔋 Зміна стану і стратегії...\n")
    robot.set_state(LowBatteryState())
    robot.set_strategy(FastWalk())
    robot.move()
