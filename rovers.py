from enum import Enum

class Direction(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

    @staticmethod
    def turn_left(current_direction):
        turns = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH
        }
        return turns[current_direction]

    @staticmethod
    def turn_right(current_direction):
        turns = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        return turns[current_direction]

class Rover:
    def __init__(self, x, y, direction, plateau_x, plateau_y):
        self.x = x
        self.y = y
        self.direction = Direction(direction.upper())
        self.plateau_x = plateau_x
        self.plateau_y = plateau_y

    def turn_left(self):
        self.direction = Direction.turn_left(self.direction)

    def turn_right(self):
        self.direction = Direction.turn_right(self.direction)

    def move(self):
        new_x, new_y = self.x, self.y

        if self.direction == Direction.NORTH:
            new_y += 1
        elif self.direction == Direction.EAST:
            new_x += 1
        elif self.direction == Direction.SOUTH:
            new_y -= 1
        elif self.direction == Direction.WEST:
            new_x -= 1

        # Boundary validation
        if 0 <= new_x <= self.plateau_x and 0 <= new_y <= self.plateau_y:
            self.x, self.y = new_x, new_y
        else:
            raise Exception(f"Error: Rover at ({self.x}, {self.y}) attempted to move out of the plateau to ({new_x}, {new_y}). Try again.")

    def execute_commands(self, commands):
        commands = commands.replace(" ", "").upper()
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move()

    def get_position(self):
        return f"{self.x} {self.y} {self.direction.value}" 

def main():
    plateau_input = input("Enter the plateau dimensions: ").strip()
    if not plateau_input:
        print("Error: Plateau dimensions were not provided.")
        return

    try:
        plateau_x, plateau_y = map(int, plateau_input.split())
    except ValueError:
        print("Error: The plateau dimensions must be two integers separated by a space.")
        return

    rovers = []
    first_rover = True  

    while True:
        try:
            if first_rover:
                position_input = input("Enter the rover's location: ").strip()
                if not position_input:
                    print("Error: The rover's location was not provided. Try again.")
                    return
                first_rover = False  
            else:
                position_input = input("Enter the next rover's location or press Enter to display the result: ").strip()
                if not position_input:  
                    break
            
            position_parts = position_input.split()
            if len(position_parts) != 3:
                print("Error: The rover's location must contain 3 values (example: '2 3 N'). Try again.")
                return
            
            try:
                x, y = int(position_parts[0]), int(position_parts[1])
            except ValueError:
                print("Error: The rover's coordinates must be integers. Try again.")
                return

            direction = position_parts[2].upper()
            if direction not in {'N', 'E', 'S', 'W'}:
                print("Error: Invalid direction. It must be 'N', 'E', 'S', or 'W'.")
                return

            if not (0 <= x <= plateau_x and 0 <= y <= plateau_y):
                print(f"Error: The rover was initialized outside the plateau at ({x}, {y}). Try again.")
                return

            commands = input("Enter the movement commands: ").strip()
            if not commands:
                print("Error: No movement commands were entered. Try again.")
                return

            commands = commands.replace(" ", "").upper()

            if not set(commands) <= {'L', 'R', 'M'}:
                print(f"Error: Invalid commands detected in '{commands}'. Only 'L', 'R', and 'M' are allowed. Try again.")
                return

            rover = Rover(x, y, direction, plateau_x, plateau_y)
            rover.execute_commands(commands)
            rovers.append(rover)

        except EOFError:
            break 

    print("\nFinal rover positions:")
    for rover in rovers:
        print(rover.get_position())


if __name__ == "__main__":
    main()
