# 24

# 1 ------------------------------------------------------------------------------------------------------------------------------------------------

from math import copysign

A, B = 200000000000000, 400000000000000

with open('i24.txt') as f:
    lines = []
    velocities = []
    for line in f:
        pos, vel = line.split(' @ ')
        pos = tuple(map(int, pos.split(', ')))
        vel = tuple(map(int, vel.split(', ')))
        p1 = tuple(pos[:2])
        p2 = (p1[0] + vel[0], p1[1] + vel[1])
        lines.append((p1, p2))
        velocities.append(vel[:2])

def lineIntersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return x, y

def checkInArea(x, y):
    return A <= x <= B and A <= y <= B

def checkFuture(start, end, vel):
    return copysign(1, end[0] - start[0]) == copysign(1, vel[0])

total = 0
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        intersectionPoint = lineIntersection(lines[i], lines[j])
        if intersectionPoint is not None and checkInArea(*intersectionPoint) and checkFuture(lines[i][0], intersectionPoint, velocities[i]) and checkFuture(lines[j][0], intersectionPoint, velocities[j]):
            total += 1

print(total)

# 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

'''import { readFileSync } from 'node:fs';

function add(A, B, hails, n) {
  const [px0, py0, pz0, vx0, vy0, vz0] = hails[0];
  const [pxN, pyN, pzN, vxN, vyN, vzN] = hails[n];
  A.push([vy0 - vyN, vxN - vx0, 0n, pyN - py0, px0 - pxN, 0n]);
  B.push(px0 * vy0 - py0 * vx0 - pxN * vyN + pyN * vxN);
  A.push([vz0 - vzN, 0n, vxN - vx0, pzN - pz0, 0n, px0 - pxN]);
  B.push(px0 * vz0 - pz0 * vx0 - pxN * vzN + pzN * vxN);
}

function det(m) {
  if (m.length === 0) return 1n;
  let [l, ...r] = m;
  r = l.map((n, i) => n * det(r.map(row => row.toSpliced(i, 1))));
  return r.reduce((a, b, i) => (i % 2 ? a - b : a + b), 0n);
}

function cramer(A, B) {
  const detA = det(A);
  return A.map((_, i) => det(A.map((r, j) => r.toSpliced(i, 1, B[j]))) / detA);
}

function part2(input) {
  const hails = input.split('\n').map(line => line.match(/-?\d+/g).map(BigInt));
  const A = [];
  const B = [];
  for (let i = 1; i <= 3; i++) add(A, B, hails, i);
  const [pxr, pyr, pzr] = cramer(A, B);
  return pxr + pyr + pzr;
}

console.log(part2(readFileSync('./day24.txt').toString().trim()));'''

#15593