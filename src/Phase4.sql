-- Hydrohomies Phase 4

DROP DATABASE IF EXISTS `AMUSEMENT_PARK`;
CREATE SCHEMA `AMUSEMENT_PARK`;
USE `AMUSEMENT_PARK`;

-- CREATING TABLES

DROP TABLE IF EXISTS `RIDE`;
CREATE TABLE `RIDE`(
    `ID` INT(11) NOT NULL,
    `NAME` VARCHAR(30) NOT NULL,
    `VIP` VARCHAR(3) NOT NULL,
    `COST` INT(7) NOT NULL,
    PRIMARY KEY(`ID`),
    UNIQUE KEY `NAME` (`NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `MESS`;
CREATE TABLE `MESS`(
    `NAME` VARCHAR(30) NOT NULL,
    `PRICE` INT(11) NOT NULL,
    `VEGETARIAN` VARCHAR(3) NOT NULL,
    PRIMARY KEY(`NAME`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `MESS_FOOD`;
CREATE TABLE `MESS_FOOD`(
    `NAME` VARCHAR(30) NOT NULL,
    `ITEM` VARCHAR(30) NOT NULL,
    PRIMARY KEY (`NAME`,`ITEM`),
    CONSTRAINT `MESS_FOOD_ibfk_1` FOREIGN KEY (`NAME`) REFERENCES `MESS` (`NAME`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;   

DROP TABLE IF EXISTS `VISITOR`;
CREATE TABLE `VISITOR`(
    `NUMBER` INT(11) NOT NULL,
    `NAME` VARCHAR(30) NOT NULL,
    `AGE` INT(3) ,
    `EATS_AT` VARCHAR(30) NOT NULL,
    PRIMARY KEY(`NUMBER`),
    CONSTRAINT `VISITOR_idfk_1` FOREIGN KEY (`EATS_AT`) REFERENCES `MESS` (`NAME`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `EMP_AGE`;
CREATE TABLE `EMP_AGE`(
    `BIRTHDATE` VARCHAR(30) NOT NULL,
    `AGE` INT(3) NOT NULL,
    PRIMARY KEY (`BIRTHDATE`) 
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `EMPLOYEE`;
CREATE TABLE `EMPLOYEE`(
    `SSN` INT(11) NOT NULL,
    `NAME` VARCHAR(30),
    `BIRTHDATE` VARCHAR(30),
    `STREET` VARCHAR(30),
    `AREA`  VARCHAR(30),
    `CITY`  VARCHAR(30),
    `ASSIGNED_MESS` VARCHAR(30),
    `ASSIGNED_RIDE_ID` INT(11),
    `JOB_TYPE` VARCHAR(30) NOT NULL,
    PRIMARY KEY (`SSN`),
    CONSTRAINT `EMPLOYEE_idfk_1` FOREIGN KEY (`ASSIGNED_RIDE_ID`) REFERENCES `RIDE` (`ID`),
    CONSTRAINT `EMPLOYEE_idfk_2` FOREIGN KEY (`ASSIGNED_MESS`) REFERENCES `MESS` (`NAME`),
    CONSTRAINT `EMPLOYEE_idfk_3` FOREIGN KEY (`BIRTHDATE`) REFERENCES `EMP_AGE` (`BIRTHDATE`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `SHOP`;
CREATE TABLE `SHOP`(
    `SHOP_LICENSE` VARCHAR(11) NOT NULL,
    `NAME` VARCHAR(30) NOT NULL,
    `OPEN` VARCHAR(3) NOT NULL,
    `TYPE` VARCHAR(30) NOT NULL,
    `OWNER_SSN` INT(11) NOT NULL,
    PRIMARY KEY (`SHOP_LICENSE`),
    CONSTRAINT `SHOP_ibfk_1` FOREIGN KEY (`OWNER_SSN`) REFERENCES `EMPLOYEE` (`SSN`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `BUYS`;
CREATE TABLE `BUYS`(
    `VISITOR_NUMBER` INT(11) NOT NULL,
    `SHOP_LICENSE` VARCHAR(11) NOT NULL,
    PRIMARY KEY(`VISITOR_NUMBER`,`SHOP_LICENSE`),
    CONSTRAINT `BUYS_idfk_1` FOREIGN KEY (`VISITOR_NUMBER`) REFERENCES `VISITOR` (`NUMBER`),
    CONSTRAINT `BUYS_idfk_2` FOREIGN KEY (`SHOP_LICENSE`) REFERENCES `SHOP` (`SHOP_LICENSE`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `ENJOYS`;
CREATE TABLE `ENJOYS`(
    `VISITOR_NUMBER` INT(11) NOT NULL,
    `RIDE_ID` INT(11) NOT NULL,
    PRIMARY KEY(`VISITOR_NUMBER`,`RIDE_ID`),
    CONSTRAINT `ENJOYS_idfk_1` FOREIGN KEY (`VISITOR_NUMBER`) REFERENCES `VISITOR` (`NUMBER`),
    CONSTRAINT `ENJOYS_idfk_2` FOREIGN KEY (`RIDE_ID`) REFERENCES `RIDE` (`ID`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `FEEDBACK`;
CREATE TABLE `FEEDBACK`(
    `VISITOR_NUMBER` INT(11) NOT NULL,
    `FEEDBACK_NUMBER` VARCHAR(11) NOT NULL,
    `RATING` INT(1),
    `REVIEW` VARCHAR(200),
    PRIMARY KEY(`VISITOR_NUMBER`,`FEEDBACK_NUMBER`),
    -- UNIQUE KEY `FEEDBACK_NUMBER` (`FEEDBACK_NUMBER`),
    CONSTRAINT `FEEDBACK_idfk_1` FOREIGN KEY (`VISITOR_NUMBER`) REFERENCES `VISITOR` (`NUMBER`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `CARD`;
CREATE TABLE `CARD`(
    `VISITOR_NUMBER` INT(11) NOT NULL,
    `CARD_ID` VARCHAR(11) NOT NULL,
    `BALANCE` INT(7) NOT NULL,
    `VIP` VARCHAR(3) NOT NULL,
    PRIMARY KEY(`VISITOR_NUMBER`,`CARD_ID`),
    -- UNIQUE KEY `CARD_ID` (`CARD_ID`),
    CONSTRAINT `CARD_idfk_1` FOREIGN KEY (`VISITOR_NUMBER`) REFERENCES `VISITOR` (`NUMBER`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `USES`;
CREATE TABLE `USES`(
    `VISITOR_NUMBER` INT(11) NOT NULL,
    `CARD_ID` VARCHAR(11) NOT NULL,
    `FEEDBACK_NUMBER` VARCHAR(11) NOT NULL,
    `RIDE_ID` INT(11) NOT NULL,   
    PRIMARY KEY(`VISITOR_NUMBER`,`CARD_ID`,`FEEDBACK_NUMBER`,`RIDE_ID`),
    CONSTRAINT `USES_idfk_1` FOREIGN KEY (`VISITOR_NUMBER`,`FEEDBACK_NUMBER`) REFERENCES `FEEDBACK` (`VISITOR_NUMBER`,`FEEDBACK_NUMBER`),
    CONSTRAINT `USES_idfk_2` FOREIGN KEY (`RIDE_ID`) REFERENCES `RIDE` (`ID`),
    -- CONSTRAINT `USES_idfk_3` FOREIGN KEY (`FEEDBACK_NUMBER`) REFERENCES `FEEDBACK` (`FEEDBACK_NUMBER`),
    CONSTRAINT `USES_idfk_3` FOREIGN KEY (`VISITOR_NUMBER`,`CARD_ID`) REFERENCES `CARD` (`VISITOR_NUMBER`,`CARD_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATING TABLES OVER

-- INSERTING INTO TABLES


LOCK TABLES `EMP_AGE` WRITE;
INSERT INTO `EMP_AGE` VALUES ('31/01/1955',	'64'),
('23/03/1965',	'54'),
('01/01/1977',	'42'),
('08/08/1974',	'45'),
('19/02/1978',	'41'),
('29/02/1980',	'39'),
('21/04/1988',	'31'),
('30/06/2000',	'19'),
('20/05/1999',	'20');
;
UNLOCK TABLES;

LOCK TABLES `RIDE` WRITE;
INSERT INTO `RIDE` VALUES ('1',	'Roller Coaster',	'Yes',	'10'),
('2',	'Water Ride 1',	'No',	'2'),
('3',	'Water Ride 2',	'No',	'2'),
('4',	'Water Ride 3',	'Yes',	'5'),
('5',	'Hurricane',	'Yes',	'10'),
('6',	'Insanity',	'No',	'3');
;
UNLOCK TABLES;

LOCK TABLES `MESS` WRITE;
INSERT INTO `MESS` VALUES ('Chutneys',	'10',	'Yes'),
('Paradise',	'10',	'No'),
('Bawarchi',	'8',	'No'),
('Dominos',	'12',	'No');
;
UNLOCK TABLES;

LOCK TABLES `MESS_FOOD` WRITE;
INSERT INTO `MESS_FOOD` VALUE ('Chutneys'	,'Veg Thali'),
('Chutneys'	,'Panner Butter Masala'),
('Chutneys'	,'Rotis'),
('Paradise'	,'Chicken Biryani'),
('Paradise'	,' Mutton Biryani'),
('Paradise'	,'Rotis'),
('Paradise'	,'Chill Chicken Curry'),
('Paradise'	,'Coca-Cola'),
('Bawarchi'	,'Chicken Biryani'),
('Bawarchi'	,' Mutton Biryani'),
('Bawarchi'	,'Rotis'),
('Bawarchi'	,'Chill Chicken Curry'),
('Bawarchi'	,'Coca-Cola'),
('Dominos'	,'Veg Pizza Mania'),
('Dominos'	,'Non-Veg Pizza Mania'),
('Dominos'	,'Garlic Breads'),
('Dominos'	,'Pepsi');
;
UNLOCK TABLES;

LOCK TABLES `EMPLOYEE` WRITE;
INSERT INTO `EMPLOYEE` VALUES ('3921832',	'Ravi Shastri',	'31/01/1955',	'Prof. CR Rao',	'Gachibowli',	'Hyderabad',	NULL,	'1',	'Manager'),
('3213233',	'Ganguly',	'23/03/1965',	'Nizampet',	'Kukatpally',	'Hyderabad',	'Bawarchi',	'1',	'Technician'),
('3214321',	'Anil Kumble',	'01/01/1977',	'Yousufguda',	'Ameerpet',	'Hyderabad',	NULL,	NULL ,	'Manager'),
('3124321',	'Bajji',	'08/08/1974',	'Krishna Nagar',	'S.R.Nagar',	'Hyderabad',	NULL,	NULL ,	'Manager'),
('3123444',	'Shane Warner',	'19/02/1978',	'Street-1',	'Jubliee Hills',	'Hyderabad',	'Paradise',	'2',	'Janitor'),
('3354213',	'Anushka Sharma',	'29/02/1980',	'Street-1',	'Banjara Hills',	'Hyderabad',	NULL,	NULL ,	'Manager'),
('3356666',	'Deepthi Sunaina',	'29/02/1980',	'Street-1',	'Banjara Hills',	'Hyderabad',	NULL,	NULL ,	'Manager'),
('3902394',	'Mahesh',	'21/04/1988',	'LB Nagar',	'Coca Cola Industry',	'Secunderabad',	'Dominos',	'4',	'Attendee'),
('3783938',	'Padma',	'30/06/2000',	'CB street',	'Big Time',	'Secunderabad',	'Paradise',	'3',	'Manager'),
('3783939',	'Warner',	'30/06/2000',	'CB street',	'Big Time',	'Secunderabad',	'Paradise',	'5',	'Janitor'),
('3783940',	'steve',	'20/05/1999',	'Street-18',	'kool_cart',	'Hyderabad',	'Chutneys',	'1',	'Manager'),
('3783941',	'Maxwell',	'20/05/1999',	'Street-19',	'kool_cart',	'Hyderabad',	'Bawarchi',	'2',	'Attendee'),
('3783942',	'Bisky',	'29/02/1980',	'Yousufguda',	'Banjara Hills',	'Hyderabad',	'Bawarchi',	'6',	'Technician');
;
UNLOCK TABLES;

LOCK TABLES `VISITOR` WRITE;
INSERT INTO `VISITOR` VALUES ('2018000',	'Sachin',	'43',	'Paradise'),
('2018001',	'Sehwag',	'41',	'Chutneys'),
('2018002',	'Dhoni',	'37',	'Bawarchi'),
('2018003',	'Kohli',	'30',	'Dominos'),
('2018004',	'Bumrah',	'25',	'Chutneys'),
('2018005',	'Umesh',	'27',	'Bawarchi'),
('2018006',	'Ishant',	'29',	'Chutneys');
;
UNLOCK TABLES;

LOCK TABLES `SHOP` WRITE;
INSERT INTO `SHOP` VALUES ('SH101',	'Sachin Gift Shop',	'Yes',	'Gifts,Novelties',	'3356666'),
('SH102',	'Virat chappals',	'Yes',	'Footwear',	'3354213'),
('SH103',	'Kumble Klothing',	'Yes',	'Clothing',	'3214321'),
('SH104',	'Bajji Sweets',	'No',	'Sweet Shop',	'3124321'),
('SH105',	'Ravi Wines',	'Yes',	'Exclusive imported wine',	'3921832');
;
UNLOCK TABLES;

LOCK TABLES `BUYS` WRITE;
INSERT INTO `BUYS` VALUES ('2018003',	'SH105'),
('2018004',	'SH102'),
('2018005',	'SH102'),
('2018005',	'SH103');
;
UNLOCK TABLES;

LOCK TABLES `ENJOYS` WRITE;
INSERT INTO `ENJOYS` VALUES ('2018001',	'1'),
('2018001',	'2'),
('2018002',	'6'),
('2018005',	'2'),
('2018006',	'3');
;
UNLOCK TABLES;

LOCK TABLES `FEEDBACK` WRITE;
INSERT INTO `FEEDBACK` VALUES ('2018001',	'F001',	'2',	'Had to wait 30 mins to get into the ride.'),
('2018001',	'F002',	'5',	'Awesome experience!'),
('2018002',	'F001',	'3',	'Decent.'),
('2018005',	'F001',	'4',	'Great Ride'),
('2018006',	'F001',	'4',	'Cheap and fun.');
;
UNLOCK TABLES;

LOCK TABLES `CARD` WRITE;
INSERT INTO `CARD` VALUES ('2018001',	'C001',	'20',	'Yes'),
('2018001',	'C002',	'10',	'No'),
('2018002',	'C001',	'15',	'No'),
('2018003',	'C001',	'12',	'No'),
('2018005',	'C001',	'18',	'Yes'),
('2018006',	'C001',	'20',	'No');
;
UNLOCK TABLES;

LOCK TABLES `USES` WRITE;
INSERT INTO `USES` VALUES ('2018001',	'C001',	'F001',	'1'),
('2018001',	'C002',	'F002',	'2'),
('2018002',	'C001',	'F001',	'6'),
('2018005',	'C001',	'F001',	'2'),
('2018006',	'C001',	'F001',	'4');
;
UNLOCK TABLES;