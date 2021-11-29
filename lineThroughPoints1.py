def lineThroughPoints(points):
    
	N = 0
	
	for i in range(len(points)):
		for j in range(i, len(points)):
			
			# Get slope and intercept
			slope, intercept = getLineParams(points[i], points[j])
			
			# Store isOnLine in a logical array and take sum
			n = sum([isOnLine(slope, intercept, p) for p in points])
			
			# Update maximum number of points
			if n > N:
				N = n

    return N

# Get parameters of line passing through p1 and p2
def getLineParams(p1, p2):
	
	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]

	if dx != 0:
		slope = dy / dx
		intercept = p1[1] - slope * p1[0]
	else:
		slope = float('inf');
		intercept = p1[0] # Store x in intercept term if slope is infinite

	return slope, intercept

# Check if point is on line of given equation
def isOnLine(slope, intercept, p):
	
	if slope == float('inf') and intercept == p[0]:
		return True # Edge case : vertical line
	else:	
		return p[1] == slope * p[0] + intercept
