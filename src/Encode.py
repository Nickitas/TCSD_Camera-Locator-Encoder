class Encoder:
    def __init__(self):
        self.binary_code = None
        self.decimal_code = None

    def encode_camera_location(self, floor: int, side: str, direction: str, camera_id: int) -> dict:
        """
        Encode camera location information into a binary and decimal code.

        Parameters:
            floor (int): Floor number (unlimited, but encoded as 0-255).
            side (str): Side of the building (N, S, E, W, NE, NW, SE, SW, C).
            direction (str): Camera orientation (N, NE, E, SE, S, SW, W, NW, C).
            camera_id (int): Unique camera ID (0-9999).

        Returns:
            dict: Dictionary containing binary and decimal codes.
        """
        # Mapping for sides and directions
        sides_map = {
            "N": 0b0001, "S": 0b0010, "E": 0b0100, "W": 0b1000,
            "NE": 0b00010100, "NW": 0b00011000, "SE": 0b00100100, "SW": 0b00101000, "C": 0b0000
        }

        directions_map = {
            "N": 0b000, "NE": 0b001, "E": 0b010, "SE": 0b011,
            "S": 0b100, "SW": 0b101, "W": 0b110, "NW": 0b111, "C": 0b000
        }

        # Validate inputs
        if floor < 0:
            raise ValueError("Floor must be a non-negative number.")

        if side not in sides_map:
            raise ValueError(f"Invalid side. Choose from {list(sides_map.keys())}.")

        if direction not in directions_map:
            raise ValueError(f"Invalid direction. Choose from {list(directions_map.keys())}.")

        if not (0 <= camera_id <= 9999):
            raise ValueError("Camera ID must be between 0 and 9999.")

        # Encoding values
        floor_encoded = floor % 256  # Limit to 0-255 for encoding
        floor_binary = format(floor_encoded, '08b')
        side_binary = format(sides_map[side], '04b')[-4:]  # Ensure 4 bits
        direction_binary = format(directions_map[direction], '03b')
        camera_id_binary = format(camera_id, '016b')

        # Combine binary code
        binary_code = f"{floor_binary} {side_binary} {direction_binary} {camera_id_binary}"

        # Combine decimal code
        decimal_code = f"{floor_encoded:03}{sides_map[side]:02}{directions_map[direction]:02}{camera_id:04}"

        return {
            "binary_code": binary_code,
            "decimal_code": decimal_code
        }