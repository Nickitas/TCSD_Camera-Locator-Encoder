import re

def validate_floor(floor_input: str) -> int:
    """Validate and convert floor input to an integer."""
    floor_pattern = re.compile(r"^\d+$")
    if not floor_pattern.match(floor_input):
        raise ValueError("Floor must be a non-negative integer.")
    return int(floor_input)

def validate_side(side_input: str) -> str:
    """Validate side input."""
    sides = {"N", "S", "E", "W", "NE", "NW", "SE", "SW", "C"}
    if side_input not in sides:
        raise ValueError(f"Invalid side. Choose from {', '.join(sides)}.")
    return side_input

def validate_direction(direction_input: str) -> str:
    """Validate direction input."""
    directions = {"N", "NE", "E", "SE", "S", "SW", "W", "NW", "C"}
    if direction_input not in directions:
        raise ValueError(f"Invalid direction. Choose from {', '.join(directions)}.")
    return direction_input

def validate_camera_id(camera_id_input: str) -> int:
    """Validate and convert camera ID input to an integer."""
    camera_id_pattern = re.compile(r"^\d{1,4}$")
    if not camera_id_pattern.match(camera_id_input) or not (0 <= int(camera_id_input) <= 9999):
        raise ValueError("Camera ID must be a number between 0 and 9999.")
    return int(camera_id_input)