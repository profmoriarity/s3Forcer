sep=("." "_" "-")
for s in ${sep[*]}; do
word=$2$s$1;
r=$(curl "http://"$word".s3.amazonaws.com/asasdasdd" -s);
#echo $r;
if [[ $r == *"AccessDenied"* ]]; then
echo "Access Denied: "$word".s3.amazonaws.com"
fi;
if [[ $r == *"NoSuchKey"* ]]; then
echo "Public Bucket: "$word".s3.amazonaws.com"
fi;

done;
