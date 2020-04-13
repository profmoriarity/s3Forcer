import requests
import threading
from queue import Queue
import argparse
requests.packages.urllib3.disable_warnings() 


parser = argparse.ArgumentParser(description="S3 Bucket Brute force with threading")
parser.add_argument("company_name", help="Specify Company name")
parser.add_argument('-t', action='store', dest='threads',help='Specify threads')
parser.add_argument('-w', action='store', dest='wordlist',help='Specify wordlist')
args = parser.parse_args()

def checkBucket(word):
    sys.stdout.write("\rScanning For Bucket: {0}".format(word))
    sys.stdout.flush()
    ss = "https://"+word+".s3.amazonaws.com/"
    responseXml = requests.get(ss,verify=False).text
    if 'ListBucketResult ' in responseXml:
        print(word)
    

seps = ["", "-", ".","_"] 

def threader():
    while True:
        worker = q.get()
        checkBucket(worker)
        q.task_done()
    

q = Queue()

threads = int(args.threads.strip())
for x in range(threads):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


company = args.company_name.strip()
for s in seps:
    with open(args.wordlist.strip()) as f:
        for bucket in f.readlines():
            q.put(company+s+bucket.strip())


q.join()