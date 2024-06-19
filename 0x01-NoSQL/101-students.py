#!/usr/bin/env python3
"""return all students sorted by average score"""



def top_students(mongo_collection):
    # Aggregation pipeline to calculate the average score and sort by it
    pipeline = [
		{
			"$project": {
				"name": "$name",
				"averageScore": {"$avg": "$topics.score"}
			}
		},
        {
            '$sort': {'averageScore': -1}
        }
    ]

    results = mongo_collection.aggregate(pipeline)
    # Convert the aggregation cursor to a list and return it
    return list(results)

