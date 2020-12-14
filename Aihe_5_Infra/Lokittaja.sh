if [[ ! -e /home/joel/Desktop/testKansio/loki.log ]]
then
touch /home/joel/Desktop/testKansio/loki.log
fi

now=$(date)

echo "heippa $now" >> /home/joel/Desktop/testKansio/loki.log
