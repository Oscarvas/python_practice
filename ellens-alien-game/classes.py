from __future__ import annotations
"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    
    total_aliens_created = 0
    x_coordinate = 0
    y_coordinate = 0
    health = 3

    def __init__(self, coord_x: int, coord_y: int):
        '''
        This is an instance or object property, attribute, or variable.
        Note that we are unpacking the tuple argument into two separate instance variables.
        '''
        # Alter instance variable
        self.x_coordinate = coord_x
        self.y_coordinate = coord_y
        self.health = 3

        # Alter class variable
        Alien.total_aliens_created += 1

    def hit(self):
        '''
        Decrement Alien health by one point.
        '''
        self.health -= 1

    def is_alive(self) -> bool:
        '''
        Return a boolean for if Alien is alive (if health is > 0).
        '''
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        '''
        Move Alien object to new coordinates.
        '''
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
    
    def collision_detection(self, other: object):
        pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(coordinates: list[tuple[int]]) -> list[Alien]:
    return [Alien(coord[0], coord[1]) for coord in coordinates]