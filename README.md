# helloworld
#I Will Not Write a guide for using logs.py as it is not my creation
#organise.py User Guide
1. This is a script which is intended  to be used to remove a particular extension type files to destination folder of ur own choice.
2. Go to folder containing the script using terminal.
3. Now execute the following command..
	python organise.py <sourcefolder> <extension> <destinationfolder>
example:
	Suppose u want to move all the pdf files from Desktop in ubuntu to a folder in Documents named study, write the following command
	python organise.py /home/<username>/Desktop pdf /home/<username>/Documents/study
	Here the <username> by ur account name and the extension of the files must be written without '.'
#This is my first python script, So i have tried to be as detailed as possible.

<h1>flatten.py User Guide</h1>
<h3>Purpose</h3>
 convert nested lists in python to ordinary list.<br>
 example:['a',34,'asd',['as',3.4,[3,'l']]] is converted to ['a',34,'asd','as',3.4,3,'1']<br>
 <h3>Usage</h3>
 the file must be compiledbefore use<br>
 in the interpretor write the following commands<br>
 >nestedlist=[...]<br>
 >import flatten<br>
 >generator=flatten.my_flatten(nestedlist)<br>
 >list(generator)   ###this gives the required list
