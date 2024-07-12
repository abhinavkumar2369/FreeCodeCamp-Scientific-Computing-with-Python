import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Copy the hat to perform the experiment without altering the original hat
        experiment_hat = copy.deepcopy(hat)
        
        # Draw balls from the hat
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        
        # Count the balls drawn
        drawn_balls_count = {}
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1
        
        # Check if the drawn balls meet the expected condition
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1

    return success_count / num_experiments
