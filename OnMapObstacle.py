from Vec import *


class OnMapObstacle:
    def __init__(self, pos, illegal_directions_encoded):
        """
        For encoding of the illegal_directions:
        binary form each bit at 1 means illegal
        1st bit for (1, 0)  (right)
        2nd bit for (0, -1) (up)
        3rd bit for (-1, 0) (left)
        4th bit for (0, 1)  (down)
        """
        self.pos = pos
        if isinstance(illegal_directions_encoded, int):
            self.illegalDirectionsEncoded = illegal_directions_encoded
        else:
            self.illegalDirectionsEncoded = 0
            for vec in illegal_directions_encoded:
                self.illegalDirectionsEncoded += 1 << self.vec2bit_position(vec)

    def vec2bit_position(self, v):
        n = -v.x + 1
        if n == 1: n = v.y + 2
        return n

    def is_illegal_direction(self, v):
        n = self.vec2bit_position(v)
        return (self.illegalDirectionsEncoded >> n) % 2 == 1
    
    def draw(self, pos, view):
        y_, x_ = divmod(self.invertedIllegalDirectionEncoded, 4)
        tile_id = x_ * 2 + y_ * 8 * 2
        view.draw_tile(pos, "basic_obstacles", tile_id, Vec(2, 2))

    @property
    def invertedIllegalDirectionEncoded(self):
        res = 0
        encode = self.illegalDirectionsEncoded
        for i in range(4):
            res = res << 1
            res += encode % 2
            encode = encode >> 1
        res = res << 2
        res = res % 16 + (res >> 4)
        return res
