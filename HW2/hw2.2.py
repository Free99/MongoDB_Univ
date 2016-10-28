import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

try:
	result = grades.find({"type": "homework"}).sort( [("student_id", 1), ("score", 1)] )
except Exception as e:
	print "Exception: ", type(e), e

curID = -1
for cursor in result:
	if curID != cursor["student_id"]:
		curID = cursor["student_id"]
		#print "removed student_id: ", curID
		db.grades.remove({"_id": cursor["_id"]})