from bucket import bucket


# TODO: can be async?
def all_bucket_objects_task():
	result = bucket.get_objects()
	return result
