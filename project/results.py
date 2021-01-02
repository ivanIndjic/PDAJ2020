import requests
import json
import matplotlib.pyplot as plt
import random

n = 1000
m = 1000
#points = ["1,3", "3,2", "6,8", "9,6", "5,5"]
#points = ["1,3","3,2","6,8","9,6","5,5","12,12","66,3","13,2","6,38","9,16","5,35","52,2"]
points = ["11,300","9,420","1,3", "3,2", "6,8", "9,6", "5,5","15,15","76,54","89,430","336,423","211,211","350,350","426,18","0,500","7,420","766,894","999,3","876,542","667,718","319,54","1,800","803,20"]

url = 'http://localhost:8000/calc/par/'

json_data = {
	"n": n,
	"m": m,
	"points": points
	}


def get_results(url, points):
	res = requests.post(url=url, json=json_data)
	data = json.loads(res.content)
	results = data["result"]
	time_in_s = data["time_in_s"]
	max_memory_in_MB = data["max_memory_in_MB"]
	return results, time_in_s, max_memory_in_MB


def random_color():
	return "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])


def display_results(res, n, m, points):
	for i in range(0, n):
		for j in range(0, m):
			if (i, j) in read_points(points):
				print('*', end=" ")
			else:
				index = res[i * n + j]
				print(index, end=" ")
		print()


def show_table(res, n, m, points):
	random_colors = [random_color() for p in points]
	colors = []

	for i in range(0, n):
		row_colors = []
		for j in range(0, m):
			if (i, j) in read_points(points):
				row_colors.append((0, 0, 0))
			else:
				index = res[i * n + j]
				row_colors.append(random_colors[index])
		colors.append(row_colors)
	columns = range(0, n)
	fig, ax = plt.subplots()
	ax.set_axis_off()
	ax.table(cellColours=colors, colWidths=[0.02 for x in columns], cellLoc ='center', loc ='upper left')
	plt.show()


def read_points(points):
	point_list = []
	for p in points:
		x, y = p.split(',')
		x, y = int(x), int(y)
		point_list.append((x, y))
	return point_list

def main():
	results, time_in_s, max_memory_in_MB = get_results(url, points)
	print(f"Time is {time_in_s}s")
	print(f"Max memory is {max_memory_in_MB}MB")
	#display_results(results, n, m, points)
	#show_table(results, n, m, points)


if __name__ == "__main__":
	main()
