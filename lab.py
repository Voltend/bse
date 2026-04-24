def point_line_side(point, p1, p2):
    x, y = point
    x1, y1 = p1
    x2, y2 = p2
    value = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
    return -1 if value > 0 else 1 if value < 0 else 0

def find_best_pair(points):
    n = len(points)
    min_diff = float('inf')
    best_pair = (None, None)
    
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            if p1 == p2: continue
            
            left = right = 0
            for point in points:
                if point == p1 or point == p2: continue
                side = point_line_side(point, p1, p2)
                if side == -1: left += 1
                elif side == 1: right += 1
            
            diff = abs(left - right)
            if diff < min_diff:
                min_diff = diff
                best_pair = (p1, p2)
    
    return best_pair[0], best_pair[1], min_diff

def main():
    # ПРИМЕР №1
    n = 6
    points = [(0, 0), (1, 0), (2, 0), (10, 10), (11, 11), (50, 0)] 
    p1, p2, diff = find_best_pair(points)
    print(f"\nЛучшая прямая: A{p1} B{p2}")
    print(f"Минимальная разность: {diff}")

if __name__ == "__main__":
    main()
