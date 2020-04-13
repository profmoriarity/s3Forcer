import requests
import threading
from queue import Queue
import argparse
import sys
requests.packages.urllib3.disable_warnings() 


parser = argparse.ArgumentParser(description="S3 Bucket Brute force with threading")
parser.add_argument("company_name", help="Specify Company name")
parser.add_argument('-t', action='store', dest='threads',help='Specify threads')
parser.add_argument('-w', action='store', dest='wordlist',help='Specify wordlist')
parser.add_argument('-o', action='store', dest='outf',help='Specify output file')

parser.add_argument('-p', action='store', dest='position',help='Word Position')
args = parser.parse_args()

fi = open(args.outf,'a')
print("Started S3 Brute Force...")

def checkBucket(word):
	print(f'\rScanning bucket: {word}', end='', flush=True)
	try:
		ss = "https://"+word+".s3.amazonaws.com/"
		responseXml = requests.get(ss,verify=False).text
		if 'ListBucketResult ' in responseXml:
			fi.write(ss)
	except:
		pass

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

position = args.position
company = args.company_name.strip()
for s in seps:
	with open(args.wordlist.strip()) as f:
		for bucket in f.readlines():
			if int(position)==1:
				q.put(company+s+bucket.strip())
			else:
				q.put(s+bucket.strip()+company)
q.join()
