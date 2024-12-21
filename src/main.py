from Encode import Encoder
from utils.helper import validate_floor, validate_side, validate_direction, validate_camera_id

if __name__ == "__main__":
    encoder = Encoder()

    try:
        # User inputs
        floor_input = input("Enter floor number (non-negative integer): ").strip()
        side_input = input("Enter side of the building (N, S, E, W, NE, NW, SE, SW, C): ").strip().upper()
        direction_input = input("Enter camera direction (N, NE, E, SE, S, SW, W, NW, C): ").strip().upper()
        camera_id_input = input("Enter camera ID (0-9999): ").strip()

        # Validating inputs
        floor = validate_floor(floor_input)
        side = validate_side(side_input)
        direction = validate_direction(direction_input)
        camera_id = validate_camera_id(camera_id_input)

        # Encoding the camera location
        encoded = encoder.encode_camera_location(floor, side, direction, camera_id)
        print("Binary Code:", encoded["binary_code"])
        print("Decimal Code:", encoded["decimal_code"])

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
