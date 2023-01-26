The script was taking too long to process, so I made some stuff in async

# add_story()
The function is defined as `async`, it means that we need to `await` its return value somewhere, as the point is to parallelize the calls to add the stories, we simply `await` each return value after they are all started

