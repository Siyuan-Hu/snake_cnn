import sys  
import time  
  
# Output example: [=======   ] 75%  
# width defines bar width  
# percent defines current percentage  
  
# def progress(width, percent):  
#     #print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent),  
#     print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent),
#     sys.stdout.flush()
  
  
# print "begin"
# # Simulate doing something ...  
# for i in xrange(100):  
#     progress(100, (i + 1))  
#     time.sleep(0.1) # Slow it down for demo  

for progress in range(100):
    time.sleep(0.5)
    sys.stdout.write("Download progress: %d%%   \r" % (progress))
    sys.stdout.flush()
    print
    sys.stdout.write("Download progress: %d%%   \r" % (progress))
    sys.stdout.flush()