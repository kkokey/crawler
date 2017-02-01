#!/bin/zsh

PW="(rootpw)"
SCRAPY_PATH="/usr/local/virtualenv/ENV/bin/scapy"

if [ -d $SCRAPY_PATH ]; then
	echo -e $PW+"\n" | sudo -S /usr/local/virtualenv/ENV/bin/scrapy crawl crawl_page
else
	echo -e $PW+"\n" | sudo -S scrapy crawl crawl_page
fi


## Add Log
if [ -d "/usr/local/crawl/crawler/crawl/spiders/data" ]; then
	echo "Make log file"
	if [ -f "/usr/local/crawl/crawler/crawl/spiders/data/cron.log" ]; then
		date >> ./data/cron.log
	fi
fi

