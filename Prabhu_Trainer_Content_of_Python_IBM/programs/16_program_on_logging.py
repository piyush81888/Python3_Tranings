"""
logging: To capture the logs in file

Instead of using text file operation method like write, writelines, print,
we can use logging library to write to file.

We are getting below advantages
1. we can specify the level: INFO, DEBUG, WARNING, CRITICAL, ERROR
2. we have predefined varaibles like created time, filename etc
    which we can use it
"""

print("Configure logging library")
print("-"*20)
# -------------

import logging
my_logger = logging.getLogger(__name__) # __name__ will be filename

logging.basicConfig(filename="my_program.log",
                    filemode="w", #a -> append
                    level=logging.DEBUG,
                    format="%(levelname)s : %(asctime)s : %(filename)s : %(message)s"
                     )

print("Configuration is DONE")

print("#"*40, end="\n\n")
##########################

print("Using logger in our programs")
print("-"*20)
# -------------

try:
    my_logger.info("Reached try block")
    my_logger.info("Opening file")
    my_file_handle = open(r"D/asdsa/wewrw.txt", "w")
    my_logger.info("File open success")
except Exception as e:
    my_logger.info("Reached except block")
    my_logger.error(f"Not able to open file and Reason: {e}")
else:
    my_logger.info("Reached 'else' block")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
finally:
    my_logger.info("Reached finally block")
    try:
        my_file_handle.close()
        my_logger.info("File handle closed")
    except Exception as e:
        my_logger.error(f"Not able to close file handle and the reason is:{e}")


print("""
Captured log in my_program.log, Please check
""")

print("#"*40, end="\n\n")
##########################
