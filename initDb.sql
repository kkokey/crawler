CREATE DATABASE `crawl` /*!40100 DEFAULT CHARACTER SET latin1 */;


CREATE TABLE `crawl_category` (
	`c_idx` int(11) NOT NULL AUTO_INCREMENT,
	`c_name` varchar(200) NOT NULL,
	`c_kind` varchar(45) DEFAULT NULL,
	PRIMARY KEY (`c_idx`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Table of category';


CREATE TABLE `crawl_product` (
	`p_idx` int(11) NOT NULL AUTO_INCREMENT,
	`p_category` int(11) DEFAULT '0',
	`p_name` varchar(200) NOT NULL DEFAULT '',
	`p_price` varchar(50) NOT NULL DEFAULT '0',
	`p_crawl_date` datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`p_idx`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

