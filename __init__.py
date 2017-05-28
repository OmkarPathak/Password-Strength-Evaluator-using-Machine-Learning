from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/main/', methods = ["GET", "POST"])
def mainPage():
	if request.method == "POST":
		enteredPassword = request.form['password']


		from sklearn import svm
		import re


		with open('test.txt','w') as test:
			testData = str(enteredPassword) + '|' + str(2)
			test.write(testData)

		# Returns feature & label arrays [ feature, label ]
		def parseData(data):
			features = list()
			labels = list()
			passwords = list()

			with open(data) as f:
				for line in f:
					if line != "":

						both = line.replace('\n', '').split("|")
						password = both[0]
						label = both[1]

						feature = [0,0,0,0,0]

						# FEATURES
						lenMin = False; # more than 8 chars
						specChar = False # special character
						ucChar = False # uppercase character
						numChar = False # numeric character

						# More than 8 characters
						if len(password) > 8:
							lenMin = True

						# Special Character
						specialMatch = re.search(r'([^a-zA-Z0-9]+)', password, re.M)
						if specialMatch:
							specChar = True

						# Uppercase Character
						ucMatch = re.search(r'([A-Z])', password, re.M)
						if ucMatch:
							ucChar = True

						# Numeric Character
						numMatch = re.search(r'([0-9])', password, re.M)
						if numMatch:
							numChar = True

						# Create rules
						if lenMin:
							feature[0] = 1

						if specChar and ucChar and numChar:
							feature[1] = 3

						if ucChar and numChar:
							feature[2] = 1

						if specChar and numChar:
							feature[3] = 2

						if specChar and ucChar:
							feature[4] = 2

						features.append(feature)
						labels.append(int(label))
						passwords.append(password)

			return [features,  labels, passwords]


		# Prepare the data
		trainingData = parseData( 'training.txt' )
		testingData = parseData( 'test.txt' )

		#A SVM Classifier
		clf = svm.SVC(kernel='linear', C = 1.0)

		#Training the classifier with the passwords and their labels.
		clf = clf.fit(trainingData[0], trainingData[1])

		#Predicting a password Strength
		prediction = clf.predict(testingData[0])

		target = len(testingData[1])
		current = 0
		incorrect = 0
		for index in range(target):
				if(prediction[index] == 0):
					predicted = "Very Weak Password"
				elif(prediction[index] == 1):
					predicted = "Weak Password"
				elif(prediction[index] == 2):
					predicted = "Strong Password"
				elif(prediction[index] == 3):
					predicted = "Very Strong Password"
	return render_template("main.html", predicted = predicted, target = len(trainingData[1]))


if __name__ == "__main__":
    app.run(host= '0.0.0.0')


