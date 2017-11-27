# Randomly add 1000 'A' samples
#####################################################################
#####################################################################
import os
import sys
import shutil
import numpy as np
from subprocess import call

a_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/A/'
a_files = []

for root, dirs, files in os.walk(a_path):
	for f in files:
		a_files.append(os.path.join(root, f))

a_files = [a_files[i] for i in np.random.choice(np.arange(len(a_files)), len(a_files), replace=False)]


for i in range(1000):
	j = np.random.choice(np.arange(len(a_files)), 1)
	# print(j[0])
	shutil.copy2(a_files[j[0]], a_path+'A-train'+str(len(a_files)+i)+'.ppm')


# # Randomly add 500 'V' samples
# #####################################################################
# #####################################################################
# import os
# import sys
# import shutil
# import numpy as np
# from subprocess import call

# v_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/V/'
# v_files = []

# for root, dirs, files in os.walk(v_path):
# 	for f in files:
# 		v_files.append(os.path.join(root, f))

# v_files = [v_files[i] for i in np.random.choice(np.arange(len(v_files)), len(v_files), replace=False)]


# for i in range(1500):
# 	j = np.random.choice(np.arange(len(v_files)), 1)
# 	shutil.copy2(v_files[j[0]], v_path+'V-train'+str(len(v_files)+i)+'.ppm')


# Remove 700 'Point' samples
#####################################################################
#####################################################################
import os
import sys
import numpy as np
from subprocess import call

point_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/Point/'
point_files = []

for root, dirs, files in os.walk(point_path):
	for f in files:
		point_files.append(os.path.join(root, f))

point_files = [point_files[i] for i in np.random.choice(np.arange(len(point_files)), len(point_files), replace=False)]


for i in range(900):
	os.remove(point_files[i])


# Remove 200 'Five' samples
#####################################################################
#####################################################################
import os
import sys
import numpy as np
from subprocess import call

five_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/Five/'
five_files = []

for root, dirs, files in os.walk(five_path):
	for f in files:
		five_files.append(os.path.join(root, f))

five_files = [five_files[i] for i in np.random.choice(np.arange(len(five_files)), len(five_files), replace=False)]


for i in range(300):
	os.remove(five_files[i])


# # Generate A samples with mixture of 'Five' samples
# #####################################################################
# #####################################################################
# import os
# import sys
# import numpy as np
# import PIL
# from PIL import Image
# import scipy.misc
# from subprocess import call
# size = 224

# five_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/Five/'
# five_files = []
# a_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/A/'
# a_files = []

# for root, dirs, files in os.walk(five_path):
# 	for f in files:
# 		five_files.append(os.path.join(root, f))

# five_files = [five_files[i] for i in np.random.choice(np.arange(len(five_files)), len(five_files), replace=False)]

# for root, dirs, files in os.walk(a_path):
# 	for f in files:
# 		a_files.append(os.path.join(root, f))

# a_files = [a_files[i] for i in np.random.choice(np.arange(len(a_files)), len(a_files), replace=False)]

# for i in range(400):
# 	# ii = np.random.choice(np.arange(len(a_files)), 1, replace=False)
# 	a = Image.open(a_files[i])
# 	a = a.resize((size, size), PIL.Image.BILINEAR)
# 	a = np.array(a)

# 	ii = np.random.choice(np.arange(len(five_files)), 1, replace=False)
# 	five = Image.open(five_files[ii])
# 	five = five.resize((size, size), PIL.Image.BILINEAR)
# 	five = np.array(five)

# 	temp = (a*0.3+five*0.7)
# 	scipy.misc.imsave(a_path+'A-train'+str(len(a_files)+i)+'.ppm', temp)
# 	# temp = Image.fromarray(temp)
# 	# temp.save(a_path+'A-train'+str(len(a_files)+i)+'.ppm')


# Generate A samples with mixture of 'Point' samples
#####################################################################
#####################################################################
# import os
# import sys
# import numpy as np
# import PIL
# from PIL import Image
# import scipy.misc
# from scipy import misc
# from subprocess import call
# size = 224

# a_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/A/'
# a_files = []
# for root, dirs, files in os.walk(a_path):
# 	for f in files:
# 		a_files.append(os.path.join(root, f))

# a_files = [a_files[i] for i in np.random.choice(np.arange(len(a_files)), len(a_files), replace=False)]


# point_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/Point/'
# point_files = []
# for root, dirs, files in os.walk(point_path):
# 	for f in files:
# 		point_files.append(os.path.join(root, f))

# point_files = [point_files[i] for i in np.random.choice(np.arange(len(point_files)), len(point_files), replace=False)]

# for i in range(300):
# 	# ii = np.random.choice(np.arange(len(v_files)), 1, replace=False)
# 	a = Image.open(a_files[i])
# 	a = a.resize((size, size), PIL.Image.BILINEAR)
# 	a = np.array(a)

# 	# ii = np.random.choice(np.arange(len(point_files)), 1, replace=False)
# 	point = Image.open(point_files[i])
# 	point = point.resize((size, size), PIL.Image.BILINEAR)
# 	point = np.array(point)

# 	temp = (a+point)/2.
# 	scipy.misc.imsave(a_path+'A-train'+str(len(a_files)+i)+'.ppm', temp)


# # Generate V samples with mixture of 'point' samples
# #####################################################################
# #####################################################################
# import os
# import sys
# import numpy as np
# import PIL
# from PIL import Image
# from subprocess import call
# size = 224

# v_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/V/'
# v_files = []
# for root, dirs, files in os.walk(v_path):
# 	for f in files:
# 		v_files.append(os.path.join(root, f))

# v_files = [v_files[i] for i in np.random.choice(np.arange(len(v_files)), len(v_files), replace=False)]


# point_path = '/home/vivekb/python/hackathon/handgesture/shp_marcel_train/Marcel-Train/Point/'
# point_files = []
# for root, dirs, files in os.walk(point_path):
# 	for f in files:
# 		point_files.append(os.path.join(root, f))

# point_files = [point_files[i] for i in np.random.choice(np.arange(len(point_files)), len(point_files), replace=False)]

# for i in range(400):
# 	# ii = np.random.choice(np.arange(len(v_files)), 1, replace=False)
# 	v = Image.open(v_files[i])
# 	v = v.resize((size, size), PIL.Image.BILINEAR)
# 	v = np.array(v)

# 	ii = np.random.choice(np.arange(len(point_files)), 1, replace=False)
# 	point = Image.open(point_files[ii])
# 	point = point.resize((size, size), PIL.Image.BILINEAR)
# 	point = np.array(point)

# 	temp = (v*0.3+point*0.7)
# 	scipy.misc.imsave(v_path+'V-train'+str(len(v_files)+i)+'.ppm', temp)
# 	# temp = Image.fromarray(temp)
# 	# temp.save(v_path+'V-train'+str(len(v_files)+i)+'.ppm')
