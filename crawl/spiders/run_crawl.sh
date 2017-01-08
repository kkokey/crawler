#!/bin/zsh

PW="(rootpw)"


echo -e $PW+"\n" | sudo -S /usr/local/virtualenv/ENV/bin/scrapy crawl crawl_page
