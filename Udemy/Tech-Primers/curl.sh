while true
do
    response=$(curl -o -I -L --write-out %{http_code} http://34.70.194.178:8080/lazy)
echo "\nResponseCoder..."$response
echo "\nDone ...\n\n"
sleep 1
done