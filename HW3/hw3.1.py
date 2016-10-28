import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
students = db.students

try:
	pipeline = [{"$match"  : { "scores.type":"homework"} }, {"$unwind" :   "$scores"}, {"$match"  : { "scores.type":"homework"} },{"$group"  : { "_id" : "$_id", "lowest" : {"$min":"$scores.score"}, }}]
	result = students.aggregate(pipeline);
except Exception as e:
	print "Exception: ", type(e), e

for cursor in result:
	students.update({"_id": cursor["_id"]}, {"$pull": {"scores": {"type": "homework", "score": cursor["lowest"]}}})