from timeit import default_timer as timer
start = timer()
# function_you_want_to_time()
# import script_to_time
import p9
p9.main()
end = timer()
elapsed = str(end - start)
print(f'Run time in seconds: {elapsed}')

