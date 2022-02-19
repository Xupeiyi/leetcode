class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy:
            return False
        
        if tx > ty:
            if sy == ty:
                return sx >= (tx % ty) and (tx - sx) % sy == 0
            return self.reachingPoints(sx, sy, tx % ty, ty)
        elif tx < ty:
            if sx == tx:
                return sy >= (ty % tx) && (ty - sy) % sx == 0
            return self.reachingPoints(sx, sy, tx, ty % tx)