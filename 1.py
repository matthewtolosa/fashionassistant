image_ids = [1001, 1002, 1003, 1004, 1005, 1006]

# Create a DataFrame with the image paths and IDs
data = {"paths": image_paths, "id": image_ids}
df = pd.DataFrame(data)

# Print the resulting DataFrame
print(df)

def compare_color(a1,a2):
	x=0
	if(a1 == 1001 and a2 == 1002):
	    x=5
	    #print(x)
	elif (a1 == 1001 and a2 == 1003):
		x=4
	elif(a1 == 1001 and a2 == 1005):
		x=1
	elif(a1 == 1004 and a2 == 1002):
		x=3
	elif(a1 == 1004 and a2 == 1003):
		x=4
	elif(a1 == 1004 and a2 == 1005):
		x=4
	elif(a1 == 1006 and a2 == 1002):
		x=3
	elif(a1 == 1006 and a2 == 1003):
		x=3
	elif(a1 == 1006 and a2 == 1005):
		x=4
	return x
def compare_fit(a1,a2):
	x=0
	if(a1==1001 and a2 ==1002):
		x=5
	if(a1==1001 and a2 ==1003):
		x=3
	if(a1==1001 and a2 ==1005):
		x=4
	if(a1==1004 and a2 ==1002):
		x=2
	if(a1==1004 and a2 ==1003):
		x=4
	if(a1==1004 and a2 ==1005):
		x=3
	if(a1==1006 and a2 ==1002):
		x=2
	if(a1==1006 and a2 ==1003):
		x=4
	if(a1==1006 and a2 ==1005):
		x=2
	return x
def compare_material(a1,a2):
	x=0
	if(a1==1001 and a2 ==1002):
		x=3
	if(a1==1001 and a2 ==1003):
		x=4
	if(a1==1001 and a2 ==1005):
		x=2
	if(a1==1004 and a2 ==1002):
		x=3
	if(a1==1004 and a2 ==1003):
		x=4
	if(a1==1004 and a2 ==1005):
		x=4
	if(a1==1006 and a2 ==1002):
		x=3
	if(a1==1006 and a2 ==1003):
		x=4
	if(a1==1006 and a2 ==1005):
		x=4
	return x
a1=1001
a2=1002
a1=int(a1)
a2=int(a2)
a=compare_color(1001,1002)
b=compare_fit(1001,1002)
c=compare_material(1001,1002)
print(a,b,c)


@app.route('/')
def index():
    # Call the compare function with image IDs
    score = compare(1001, 1002)
    return render_template('createoutfit.html', score=score)

if name == 'main':
    app.run()