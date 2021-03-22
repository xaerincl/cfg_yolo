import os
import argparse


def calcular(classes,num_images):

	filters = int((int(classes)+5)*3)

	max_batches = int(classes)*2000

	if max_batches<6000:
		max_batches = 6000


	if max_batches<=int(num_images):
		max_batches = int(num_images)

	step_1 = int(max_batches*0.8)
	step_2 = int(max_batches*0.9)
	steps = f'{step_1},{step_2}'

	return  filters, max_batches, steps


def exact_filter_line(yolo_lines,filter_lines):
	# get the exact line of the last filter line before each yolo layer

	exact_filter_list = []

	for i in yolo_lines:
		it = filter(lambda number: number < i, filter_lines)
		filtered_numbers = list(it)
		exact_filter_list.append(filtered_numbers[-1])

	return exact_filter_list



def modify(file_name, classes, filters, max_batches, steps, width, height, batch, subdivisions, flip, random):

	new_file = file_name.split('.')[0] + '_custom.cfg'

	complete_file = []

	with open(file_name, 'r') as file_object:
		for line in file_object:
			complete_file.append(line)


	yolo_lines = [i for i,line in enumerate(complete_file) if '[yolo]' in line]
	filter_lines = [i for i,line in enumerate(complete_file) if 'filters' in line]
	# modify the 'filters=' line before each yolo layer
	filter_before_yolo = exact_filter_line(yolo_lines, filter_lines)

	training = 0
	hue_line = False



	with open(new_file, 'w') as file_object:
		for i,line in enumerate(complete_file):

			if 'Training' in line:
				training = 1

			if 'classes' in line:
				file_object.write(f'classes={classes}'+'\n')
				
			elif 'max_batches' in line:
				file_object.write(f'max_batches = {max_batches}'+'\n')
				
			elif 'steps' in line and 'policy' not in line:
				file_object.write(f'steps={steps}'+'\n')
				
			elif i in filter_before_yolo:
				file_object.write(f'filters={filters}'+'\n')

			elif 'subdivisions' in line:
				if training==1:
					file_object.write(f'subdivisions={subdivisions}'+'\n')
				else:
					file_object.write(f'#subdivisions=1'+'\n')

			elif 'batch' in line and 'batch_' not in line and '_batch' not in line:
				if training==1:
					file_object.write(f'batch={batch}'+'\n')
				else:
					file_object.write(f'#batch=1'+'\n')

			elif 'width' in line:
				file_object.write(f'width={width}'+'\n')

			elif 'height' in line:
				file_object.write(f'height={height}'+'\n')

			elif 'hue' in line and flip:
				file_object.write('hue=.1'+'\n')
				file_object.write('flip=0')

			elif 'random' in line and random:
				file_object.write('random=0'+'\n')

			else:
				file_object.write(line)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='''Create YOLO cfg''')
	parser.add_argument('-input', '-i',  type=str, required=True, help='Path to default .cfg')
	parser.add_argument('-classes', '-c',  type=int, required=True, help='Detect how many classes')
	parser.add_argument('-num_images', '-n',  type=int, default=6000, help='Number of training images')
	parser.add_argument('-width', '-wi',  type=int, default = 416, help='network size- width')
	parser.add_argument('-height', '-he', type=int, default = 416, help='network size- height')
	parser.add_argument('-batches', '-b',  type=int, default = 64, help='')
	parser.add_argument('-subdivisions', '-sub',  type=int,  default = 32, help='')

	parser.add_argument("-no_random", help="change random to 0", action="store_true")
	parser.add_argument("-no_flip", help="if the model needs to distinguish between left and right objects", action="store_true")
	args = parser.parse_args()


	f, m, s = calcular(args.classes, args.num_images)
	modify(args.input, args.classes, f, m, s, args.width, args.height, args.batches, args.subdivisions, args.no_flip, args.no_random)
