# s3basher.sh
User parallel for concurrency
```
parallel -j 100 "bash s3basher.sh {} paytm" :::: ./wordlist.txt
```

# s3Forcer
Multi-threaded S3 Bucket  brute forcer

```
usage: s3forcer.py [-h] [-t THREADS] [-w WORDLIST] [-o OUTF] [-p POSITION]
                   company_name

S3 Bucket Brute force with threading

positional arguments:
  company_name  Specify Company name

optional arguments:
  -h, --help    show this help message and exit
  -t THREADS    Specify threads
  -w WORDLIST   Specify wordlist
  -o OUTF       Specify output file
  -p POSITION   Word Position

```


## Example

```
python3 s3forcer.py acme -t 50 -w list.txt -o out.txt -p 1 
```
