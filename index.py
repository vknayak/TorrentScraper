
import json,pprint
with open("books_data1.json","r+") as naik:
	python_data=json.load(naik)

for data in python_data:
	print(data['name'])


books =open("elibrary.html", "w")
books.write("<html>\n")
books.write("<head>\n")
books.write("<title>Mobile Phones</title>\n")
books.write("</head>\n")
books.write("<body>\n")
books.write("<table border=1>")
books.write("<thead><tr><td>Position</td><td>Name</td><td>Magnetic Link</td><td>Size</td></tr></thead>")
for data in python_data:
	books.write("<tr><td>"+data['position']+"</td>")
	books.write("<td>"+data['name']+"</td>")
	books.write('<td><a href="')
	books.write(data['link'])
	books.write('">+Magnet Link</a></td>')
	books.write("<td>"+data['size']+"</td>")

	# for each in data[i]:
	# 	if "https" in data[i][each]:
	# 		# students_file.write("<td><img width="+"200"+"px height="+"200"+"px src="+data[i][each]+"></td>")
	# 		books.write("<td><img src="+data[i][each]+"></td>")
	# 		continue
	# 	books.write("<td>"+data[i][each]+"</td>")
	books.write("</tr>")
	
books.write("</table>")

books.write("</body>\n")
books.write("</html>\n")
books.close()
