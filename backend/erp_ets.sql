-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: erp_ets
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add simple user',6,'add_simpleuser'),(22,'Can change simple user',6,'change_simpleuser'),(23,'Can delete simple user',6,'delete_simpleuser'),(24,'Can view simple user',6,'view_simpleuser'),(25,'Can add area',7,'add_area'),(26,'Can change area',7,'change_area'),(27,'Can delete area',7,'delete_area'),(28,'Can view area',7,'view_area'),(29,'Can add dds',8,'add_dds'),(30,'Can change dds',8,'change_dds'),(31,'Can delete dds',8,'delete_dds'),(32,'Can view dds',8,'view_dds'),(33,'Can add event',9,'add_event'),(34,'Can change event',9,'change_event'),(35,'Can delete event',9,'delete_event'),(36,'Can view event',9,'view_event'),(37,'Can add location',10,'add_location'),(38,'Can change location',10,'change_location'),(39,'Can delete location',10,'delete_location'),(40,'Can view location',10,'view_location'),(41,'Can add patrol quest',11,'add_patrolquest'),(42,'Can change patrol quest',11,'change_patrolquest'),(43,'Can delete patrol quest',11,'delete_patrolquest'),(44,'Can view patrol quest',11,'view_patrolquest'),(45,'Can add plant',12,'add_plant'),(46,'Can change plant',12,'change_plant'),(47,'Can delete plant',12,'delete_plant'),(48,'Can view plant',12,'view_plant'),(49,'Can add possible answer',13,'add_possibleanswer'),(50,'Can change possible answer',13,'change_possibleanswer'),(51,'Can delete possible answer',13,'delete_possibleanswer'),(52,'Can view possible answer',13,'view_possibleanswer'),(53,'Can add profile service',14,'add_profileservice'),(54,'Can change profile service',14,'change_profileservice'),(55,'Can delete profile service',14,'delete_profileservice'),(56,'Can view profile service',14,'view_profileservice'),(57,'Can add ssm type',15,'add_ssmtype'),(58,'Can change ssm type',15,'change_ssmtype'),(59,'Can delete ssm type',15,'delete_ssmtype'),(60,'Can view ssm type',15,'view_ssmtype'),(61,'Can add system',16,'add_system'),(62,'Can change system',16,'change_system'),(63,'Can delete system',16,'delete_system'),(64,'Can view system',16,'view_system'),(65,'Can add team',17,'add_team'),(66,'Can change team',17,'change_team'),(67,'Can delete team',17,'delete_team'),(68,'Can view team',17,'view_team'),(69,'Can add team event',18,'add_teamevent'),(70,'Can change team event',18,'change_teamevent'),(71,'Can delete team event',18,'delete_teamevent'),(72,'Can view team event',18,'view_teamevent'),(73,'Can add ssm',19,'add_ssm'),(74,'Can change ssm',19,'change_ssm'),(75,'Can delete ssm',19,'delete_ssm'),(76,'Can view ssm',19,'view_ssm'),(77,'Can add patrol week',20,'add_patrolweek'),(78,'Can change patrol week',20,'change_patrolweek'),(79,'Can delete patrol week',20,'delete_patrolweek'),(80,'Can view patrol week',20,'view_patrolweek'),(81,'Can add patrol answer',21,'add_patrolanswer'),(82,'Can change patrol answer',21,'change_patrolanswer'),(83,'Can delete patrol answer',21,'delete_patrolanswer'),(84,'Can view patrol answer',21,'view_patrolanswer'),(85,'Can add access level',22,'add_accesslevel'),(86,'Can change access level',22,'change_accesslevel'),(87,'Can delete access level',22,'delete_accesslevel'),(88,'Can view access level',22,'view_accesslevel'),(89,'Can add Token',23,'add_token'),(90,'Can change Token',23,'change_token'),(91,'Can delete Token',23,'delete_token'),(92,'Can view Token',23,'view_token'),(93,'Can add token',24,'add_tokenproxy'),(94,'Can change token',24,'change_tokenproxy'),(95,'Can delete token',24,'delete_tokenproxy'),(96,'Can view token',24,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_home_simpleuser_id` FOREIGN KEY (`user_id`) REFERENCES `home_simpleuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_home_simpleuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_home_simpleuser_id` FOREIGN KEY (`user_id`) REFERENCES `home_simpleuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-05-18 13:08:53.899191','1','Location object (1)',1,'[{\"added\": {}}]',10,1),(2,'2022-05-18 13:18:04.296261','1','Event object (1)',1,'[{\"added\": {}}]',9,1),(3,'2022-05-18 13:18:59.516152','2','Event object (2)',1,'[{\"added\": {}}]',9,1),(4,'2022-05-18 13:23:35.725312','1','Engineering Technical School',1,'[{\"added\": {}}]',7,1),(5,'2022-05-18 13:23:56.873070','1','Campinas',1,'[{\"added\": {}}]',12,1),(6,'2022-05-18 13:24:08.020958','1','Smart Automation 1',1,'[{\"added\": {}}]',17,1),(7,'2022-05-18 13:25:25.939745','1','TeamEvent object (1)',1,'[{\"added\": {}}]',18,1),(8,'2022-05-18 13:26:52.776513','1','AMA',1,'[{\"added\": {}}]',15,1),(9,'2022-05-18 13:26:55.565021','2','BAST',1,'[{\"added\": {}}]',15,1),(10,'2022-05-18 13:27:15.548250','1','AMA 1',1,'[{\"added\": {}}]',19,1),(11,'2022-05-18 13:27:31.362002','2','AMA 2',1,'[{\"added\": {}}]',19,1),(12,'2022-05-18 13:27:47.803203','3','BAST 1',1,'[{\"added\": {}}]',19,1),(13,'2022-05-20 11:01:32.182029','1','Wiki ETS',1,'[{\"added\": {}}]',16,1),(14,'2022-05-20 11:02:51.862322','2','Patrulhamento',1,'[{\"added\": {}}]',16,1),(15,'2022-05-20 11:03:37.575565','3','Agenda',1,'[{\"added\": {}}]',16,1),(16,'2022-05-20 11:04:36.199413','4','Espaço SGI',1,'[{\"added\": {}}]',16,1),(17,'2022-05-20 11:05:19.971322','1','1',1,'[{\"added\": {}}]',11,1),(18,'2022-05-20 11:05:37.360137','2','2',1,'[{\"added\": {}}]',11,1),(19,'2022-05-20 11:05:47.798921','3','3',1,'[{\"added\": {}}]',11,1),(20,'2022-05-20 11:06:00.444001','4','4',1,'[{\"added\": {}}]',11,1),(21,'2022-05-20 11:06:10.059863','5','5',1,'[{\"added\": {}}]',11,1),(22,'2022-05-20 11:06:20.363300','6','6',1,'[{\"added\": {}}]',11,1),(23,'2022-05-20 11:06:29.967686','7','7',1,'[{\"added\": {}}]',11,1),(24,'2022-05-20 11:06:42.101902','8','8',1,'[{\"added\": {}}]',11,1),(25,'2022-05-20 11:06:56.984783','9','9',1,'[{\"added\": {}}]',11,1),(26,'2022-05-20 11:07:10.919091','10','10',1,'[{\"added\": {}}]',11,1),(27,'2022-05-20 11:07:24.294784','11','11',1,'[{\"added\": {}}]',11,1),(28,'2022-05-20 11:07:34.280308','12','12',1,'[{\"added\": {}}]',11,1),(29,'2022-05-20 11:07:47.976921','13','13',1,'[{\"added\": {}}]',11,1),(30,'2022-05-20 11:07:57.057894','14','14',1,'[{\"added\": {}}]',11,1),(31,'2022-05-20 11:08:07.350870','15','15',1,'[{\"added\": {}}]',11,1),(32,'2022-05-20 11:08:17.149352','16','16',1,'[{\"added\": {}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(23,'authtoken','token'),(24,'authtoken','tokenproxy'),(4,'contenttypes','contenttype'),(22,'home','accesslevel'),(7,'home','area'),(8,'home','dds'),(9,'home','event'),(10,'home','location'),(21,'home','patrolanswer'),(11,'home','patrolquest'),(20,'home','patrolweek'),(12,'home','plant'),(13,'home','possibleanswer'),(14,'home','profileservice'),(6,'home','simpleuser'),(19,'home','ssm'),(15,'home','ssmtype'),(16,'home','system'),(17,'home','team'),(18,'home','teamevent'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-05-18 12:42:31.249545'),(2,'contenttypes','0002_remove_content_type_name','2022-05-18 12:42:32.791629'),(3,'auth','0001_initial','2022-05-18 12:42:36.890629'),(4,'auth','0002_alter_permission_name_max_length','2022-05-18 12:42:38.406820'),(5,'auth','0003_alter_user_email_max_length','2022-05-18 12:42:38.526716'),(6,'auth','0004_alter_user_username_opts','2022-05-18 12:42:38.684783'),(7,'auth','0005_alter_user_last_login_null','2022-05-18 12:42:38.724856'),(8,'auth','0006_require_contenttypes_0002','2022-05-18 12:42:38.764336'),(9,'auth','0007_alter_validators_add_error_messages','2022-05-18 12:42:38.834232'),(10,'auth','0008_alter_user_username_max_length','2022-05-18 12:42:38.876254'),(11,'auth','0009_alter_user_last_name_max_length','2022-05-18 12:42:38.916868'),(12,'auth','0010_alter_group_name_max_length','2022-05-18 12:42:39.048865'),(13,'auth','0011_update_proxy_permissions','2022-05-18 12:42:39.093214'),(14,'auth','0012_alter_user_first_name_max_length','2022-05-18 12:42:39.141822'),(15,'home','0001_initial','2022-05-18 12:43:16.528029'),(16,'admin','0001_initial','2022-05-18 12:43:19.445000'),(17,'admin','0002_logentry_remove_auto_add','2022-05-18 12:43:19.595374'),(18,'admin','0003_logentry_add_action_flag_choices','2022-05-18 12:43:19.695852'),(19,'authtoken','0001_initial','2022-05-18 12:43:21.996656'),(20,'authtoken','0002_auto_20160226_1747','2022-05-18 12:43:22.130766'),(21,'authtoken','0003_tokenproxy','2022-05-18 12:43:22.213786'),(22,'sessions','0001_initial','2022-05-18 12:43:23.065482'),(23,'home','0002_event_event_responsible','2022-05-18 13:16:58.273602'),(24,'home','0002_remove_patrolanswer_fk_patroweek_delete_patrolweek','2022-05-20 13:23:15.868045'),(25,'home','0003_possibleanswer_answerbool','2022-05-20 13:25:48.955336'),(26,'home','0004_patrolanswer_fk_patrol','2022-05-20 13:38:35.079990'),(27,'home','0005_remove_patrolanswer_fk_answer_patrolanswer_answer_and_more','2022-05-20 14:15:39.320037');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('e16kjref73h4zte0507cgkdsxq4mu52b','.eJxVjMEOwiAQRP-FsyGwWwQ8eu83kN0ulappk9KejP-uJD1o5jbvzbxUon0raa95TZOoi7Lq9NsxDY88NyB3mm-LHpZ5WyfWTdEHrbpfJD-vh_t3UKiW7_rMaDoYrQHobIeGIuTRRusD59iCGGAkATAOSbwLIkwYxRlC9qLeH7iQN2M:1ns0Ll:MJfoV0pcvpp362X6WRrn-PdigJ4hIodW3Xmcmv3hB1E','2022-06-03 10:59:17.625304'),('evufz5goz8j6aufvdymzd7c3u1tmlyj3','.eJxVjMEOwiAQRP-FsyGwWwQ8eu83kN0ulappk9KejP-uJD1o5jbvzbxUon0raa95TZOoi7Lq9NsxDY88NyB3mm-LHpZ5WyfWTdEHrbpfJD-vh_t3UKiW7_rMaDoYrQHobIeGIuTRRusD59iCGGAkATAOSbwLIkwYxRlC9qLeH7iQN2M:1nrJA9:p34xqG2gGW8KZSjnJ8tvRMYDuFC0sANjQJJic-rdpes','2022-06-01 12:52:25.857018'),('gl8rl22safsm2r6aaat6eew7xuv30939','.eJxVjMEOwiAQRP-FsyGwWwQ8eu83kN0ulappk9KejP-uJD1o5jbvzbxUon0raa95TZOoi7Lq9NsxDY88NyB3mm-LHpZ5WyfWTdEHrbpfJD-vh_t3UKiW7_rMaDoYrQHobIeGIuTRRusD59iCGGAkATAOSbwLIkwYxRlC9qLeH7iQN2M:1nrJ2b:rbnpkV9l1kU-OANN4SwK_wwQPJlgUG8MqOLNzkbjCd8','2022-06-01 12:44:37.205303');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_accesslevel`
--

DROP TABLE IF EXISTS `home_accesslevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_accesslevel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `level` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_accesslevel`
--

LOCK TABLES `home_accesslevel` WRITE;
/*!40000 ALTER TABLE `home_accesslevel` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_accesslevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_accesslevel_profiles`
--

DROP TABLE IF EXISTS `home_accesslevel_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_accesslevel_profiles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `accesslevel_id` bigint(20) NOT NULL,
  `profileservice_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_accesslevel_profile_accesslevel_id_profilese_ad485fc3_uniq` (`accesslevel_id`,`profileservice_id`),
  KEY `home_accesslevel_pro_profileservice_id_149e239b_fk_home_prof` (`profileservice_id`),
  CONSTRAINT `home_accesslevel_pro_accesslevel_id_138526f7_fk_home_acce` FOREIGN KEY (`accesslevel_id`) REFERENCES `home_accesslevel` (`id`),
  CONSTRAINT `home_accesslevel_pro_profileservice_id_149e239b_fk_home_prof` FOREIGN KEY (`profileservice_id`) REFERENCES `home_profileservice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_accesslevel_profiles`
--

LOCK TABLES `home_accesslevel_profiles` WRITE;
/*!40000 ALTER TABLE `home_accesslevel_profiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_accesslevel_profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_area`
--

DROP TABLE IF EXISTS `home_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_area` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `area` varchar(40) NOT NULL,
  `areaAbrv` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_area`
--

LOCK TABLES `home_area` WRITE;
/*!40000 ALTER TABLE `home_area` DISABLE KEYS */;
INSERT INTO `home_area` VALUES (1,'Engineering Technical School','ETS');
/*!40000 ALTER TABLE `home_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_dds`
--

DROP TABLE IF EXISTS `home_dds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_dds` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `frontImg` varchar(100) DEFAULT NULL,
  `frontText` varchar(1000) DEFAULT NULL,
  `backImg` varchar(100) DEFAULT NULL,
  `backText` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_dds`
--

LOCK TABLES `home_dds` WRITE;
/*!40000 ALTER TABLE `home_dds` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_dds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_event`
--

DROP TABLE IF EXISTS `home_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_event` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `date` date NOT NULL,
  `startTime` time(6) NOT NULL,
  `endTime` time(6) NOT NULL,
  `location_id` bigint(20) NOT NULL,
  `event_responsible` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `home_event_location_id_a9d5e4cd_fk_home_location_id` (`location_id`),
  CONSTRAINT `home_event_location_id_a9d5e4cd_fk_home_location_id` FOREIGN KEY (`location_id`) REFERENCES `home_location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_event`
--

LOCK TABLES `home_event` WRITE;
/*!40000 ALTER TABLE `home_event` DISABLE KEYS */;
INSERT INTO `home_event` VALUES (1,'Aula Java 1','Aulão de java do 0 ao ABSOLUTO','2022-05-18','10:15:00.000000','10:45:00.000000',1,'Clebinho'),(2,'Aula Python 1','Aulão de Python Master','2022-05-18','11:00:00.000000','13:00:00.000000',1,'Francielle');
/*!40000 ALTER TABLE `home_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_location`
--

DROP TABLE IF EXISTS `home_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_location` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `localName` varchar(80) NOT NULL,
  `businessPoint` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_location`
--

LOCK TABLES `home_location` WRITE;
/*!40000 ALTER TABLE `home_location` DISABLE KEYS */;
INSERT INTO `home_location` VALUES (1,'ETS','CA149');
/*!40000 ALTER TABLE `home_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_patrolanswer`
--

DROP TABLE IF EXISTS `home_patrolanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_patrolanswer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `answerDay` date NOT NULL,
  `fk_patrolquest_id` bigint(20) NOT NULL,
  `fk_patrol_id` int(11) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL,
  `answerBool` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `home_patrolanswer_fk_patrolquest_id_67981338_fk_home_patr` (`fk_patrolquest_id`),
  KEY `home_patrolanswer_fk_patrol_id_e24a5746_fk_home_simpleuser_id` (`fk_patrol_id`),
  CONSTRAINT `home_patrolanswer_fk_patrol_id_e24a5746_fk_home_simpleuser_id` FOREIGN KEY (`fk_patrol_id`) REFERENCES `home_simpleuser` (`id`),
  CONSTRAINT `home_patrolanswer_fk_patrolquest_id_67981338_fk_home_patr` FOREIGN KEY (`fk_patrolquest_id`) REFERENCES `home_patrolquest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_patrolanswer`
--

LOCK TABLES `home_patrolanswer` WRITE;
/*!40000 ALTER TABLE `home_patrolanswer` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_patrolanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_patrolquest`
--

DROP TABLE IF EXISTS `home_patrolquest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_patrolquest` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `question` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_patrolquest`
--

LOCK TABLES `home_patrolquest` WRITE;
/*!40000 ALTER TABLE `home_patrolquest` DISABLE KEYS */;
INSERT INTO `home_patrolquest` VALUES (1,'O piso está em boas condições?'),(2,'Berços, Pallets, Caixas estão respeitando os limites dos corredores e estão organizados em seus lugares conforme demarcação?'),(3,'Há vazamento de ar comprimido?'),(4,'Os extintores e portas de emergência estão desobstruidas e sinalizadas?'),(5,'Os painéis elétricos estão trancados e sinalizados?'),(6,'A fiação elétrica está em bom estado de conservação?'),(7,'Há vazamento de óleo/produtos químicos?'),(8,'Os armários de produtos químicos estão limpos, organizados e fechados?'),(9,'Os produtos químicos (todos) estão armazenados em recipientes adequados e identificados com norma, nome e simbologia de risco?'),(10,'Os produtos químicos tóxicos e explosivos estão armazenados em armários de acesso restrito e estão identificados, trancados/chaveados?'),(11,'Existem bandejas nos locais de armazenamento de produtos químicos (armários TPM ou tambores)?'),(12,'Os colaboradores estão usando os EPI\'s e isentos de adornos?'),(13,'A Coleta Seletiva esta sendo realizada de forma correta?'),(14,'Existem garrafas de água ou alimentos nos postos de trabalho?'),(15,'As ferramentas manuais estão em bom estado de conservação e sem improvisação?'),(16,'Os armários dos vestiários estão fechados adequadamente');
/*!40000 ALTER TABLE `home_patrolquest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_plant`
--

DROP TABLE IF EXISTS `home_plant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_plant` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `plant` varchar(25) NOT NULL,
  `plantAbrv` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_plant`
--

LOCK TABLES `home_plant` WRITE;
/*!40000 ALTER TABLE `home_plant` DISABLE KEYS */;
INSERT INTO `home_plant` VALUES (1,'Campinas','CaP');
/*!40000 ALTER TABLE `home_plant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_profileservice`
--

DROP TABLE IF EXISTS `home_profileservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_profileservice` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `profile` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_profileservice`
--

LOCK TABLES `home_profileservice` WRITE;
/*!40000 ALTER TABLE `home_profileservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_profileservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_simpleuser`
--

DROP TABLE IF EXISTS `home_simpleuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_simpleuser` (
  `last_login` datetime(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `username` varchar(8) NOT NULL,
  `email` varchar(80) NOT NULL,
  `edv` varchar(12) NOT NULL,
  `password` varchar(500) NOT NULL,
  `birthDate` date DEFAULT NULL,
  `user_img` varchar(100) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `currentLevel_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `home_simpleuser_currentLevel_id_1f1ee84b_fk_home_accesslevel_id` (`currentLevel_id`),
  CONSTRAINT `home_simpleuser_currentLevel_id_1f1ee84b_fk_home_accesslevel_id` FOREIGN KEY (`currentLevel_id`) REFERENCES `home_accesslevel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_simpleuser`
--

LOCK TABLES `home_simpleuser` WRITE;
/*!40000 ALTER TABLE `home_simpleuser` DISABLE KEYS */;
INSERT INTO `home_simpleuser` VALUES ('2022-05-20 10:59:17.611329',1,'','','admin','admin@email.com','','pbkdf2_sha256$320000$k3O0poXWPAHP8NZuw531L7$WPeF297dbXO/o5RG7xSO1EhojnanLVw5YCyVndrPpBk=','2022-05-18','users/default_user.png',1,1,NULL);
/*!40000 ALTER TABLE `home_simpleuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_simpleuser_fk_team`
--

DROP TABLE IF EXISTS `home_simpleuser_fk_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_simpleuser_fk_team` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `simpleuser_id` int(11) NOT NULL,
  `team_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_simpleuser_fk_team_simpleuser_id_team_id_20498187_uniq` (`simpleuser_id`,`team_id`),
  KEY `home_simpleuser_fk_team_team_id_b8dc4670_fk_home_team_id` (`team_id`),
  CONSTRAINT `home_simpleuser_fk_t_simpleuser_id_e83f517c_fk_home_simp` FOREIGN KEY (`simpleuser_id`) REFERENCES `home_simpleuser` (`id`),
  CONSTRAINT `home_simpleuser_fk_team_team_id_b8dc4670_fk_home_team_id` FOREIGN KEY (`team_id`) REFERENCES `home_team` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_simpleuser_fk_team`
--

LOCK TABLES `home_simpleuser_fk_team` WRITE;
/*!40000 ALTER TABLE `home_simpleuser_fk_team` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_simpleuser_fk_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_simpleuser_groups`
--

DROP TABLE IF EXISTS `home_simpleuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_simpleuser_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `simpleuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_simpleuser_groups_simpleuser_id_group_id_94ed030d_uniq` (`simpleuser_id`,`group_id`),
  KEY `home_simpleuser_groups_group_id_abc560fa_fk_auth_group_id` (`group_id`),
  CONSTRAINT `home_simpleuser_grou_simpleuser_id_85ad577b_fk_home_simp` FOREIGN KEY (`simpleuser_id`) REFERENCES `home_simpleuser` (`id`),
  CONSTRAINT `home_simpleuser_groups_group_id_abc560fa_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_simpleuser_groups`
--

LOCK TABLES `home_simpleuser_groups` WRITE;
/*!40000 ALTER TABLE `home_simpleuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_simpleuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_simpleuser_user_permissions`
--

DROP TABLE IF EXISTS `home_simpleuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_simpleuser_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `simpleuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_simpleuser_user_per_simpleuser_id_permission_4f5e5f1e_uniq` (`simpleuser_id`,`permission_id`),
  KEY `home_simpleuser_user_permission_id_7293b696_fk_auth_perm` (`permission_id`),
  CONSTRAINT `home_simpleuser_user_permission_id_7293b696_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `home_simpleuser_user_simpleuser_id_edcb2756_fk_home_simp` FOREIGN KEY (`simpleuser_id`) REFERENCES `home_simpleuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_simpleuser_user_permissions`
--

LOCK TABLES `home_simpleuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `home_simpleuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_simpleuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_ssm`
--

DROP TABLE IF EXISTS `home_ssm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_ssm` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `file` varchar(100) NOT NULL,
  `miniImg` varchar(100) DEFAULT NULL,
  `fk_type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_ssm_fk_type_id_2ed012d5_fk_home_ssmtype_id` (`fk_type_id`),
  CONSTRAINT `home_ssm_fk_type_id_2ed012d5_fk_home_ssmtype_id` FOREIGN KEY (`fk_type_id`) REFERENCES `home_ssmtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_ssm`
--

LOCK TABLES `home_ssm` WRITE;
/*!40000 ALTER TABLE `home_ssm` DISABLE KEYS */;
INSERT INTO `home_ssm` VALUES (1,'AMA 1','ssm/pdfs/sample_rQjqnHP.pdf','ssm/imgs/2789a057-c5b3-4b56-a500-52da3f566ebd.jpg',1),(2,'AMA 2','ssm/pdfs/SIMULADO-PRATICO-SAEP-V1_fsrWUoP.pdf','ssm/imgs/35d8f158-81be-4040-95cb-6c6bc26e3c7d.jpg',1),(3,'BAST 1','ssm/pdfs/SIMULADO-PRATICO-SAEP-V1_BzHXqH1.pdf','ssm/imgs/86787f74-3243-4cbd-86dd-73465ee64443.jpg',2);
/*!40000 ALTER TABLE `home_ssm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_ssmtype`
--

DROP TABLE IF EXISTS `home_ssmtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_ssmtype` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_ssmtype`
--

LOCK TABLES `home_ssmtype` WRITE;
/*!40000 ALTER TABLE `home_ssmtype` DISABLE KEYS */;
INSERT INTO `home_ssmtype` VALUES (1,'AMA'),(2,'BAST');
/*!40000 ALTER TABLE `home_ssmtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_system`
--

DROP TABLE IF EXISTS `home_system`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_system` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `router_to` varchar(500) DEFAULT NULL,
  `icon` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_system`
--

LOCK TABLES `home_system` WRITE;
/*!40000 ALTER TABLE `home_system` DISABLE KEYS */;
INSERT INTO `home_system` VALUES (1,'Wiki ETS','Site para a visualização de informações da ETS, sejam internas ao setor ou externas (relacionadas a planta de Campinas).','/','info'),(2,'Patrulhamento','Página de patrulhamento do setor da ETS, para a checagem de equipamentos e estutura do ambiente.','/patrols','home'),(3,'Agenda','Página para a visualização docalendário de aulas das turmas da ETS.','/agenda','calendar'),(4,'Espaço SGI','Espaço para visualização de informações de segurança e meio ambiente vindos da HSE.','/sgi/dds','home');
/*!40000 ALTER TABLE `home_system` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_team`
--

DROP TABLE IF EXISTS `home_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_team` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `qttMates` int(11) DEFAULT NULL,
  `fk_area_id` bigint(20) DEFAULT NULL,
  `fk_plant_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `home_team_fk_area_id_662293bd_fk_home_area_id` (`fk_area_id`),
  KEY `home_team_fk_plant_id_3bbb9bd3_fk_home_plant_id` (`fk_plant_id`),
  CONSTRAINT `home_team_fk_area_id_662293bd_fk_home_area_id` FOREIGN KEY (`fk_area_id`) REFERENCES `home_area` (`id`),
  CONSTRAINT `home_team_fk_plant_id_3bbb9bd3_fk_home_plant_id` FOREIGN KEY (`fk_plant_id`) REFERENCES `home_plant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_team`
--

LOCK TABLES `home_team` WRITE;
/*!40000 ALTER TABLE `home_team` DISABLE KEYS */;
INSERT INTO `home_team` VALUES (1,'Smart Automation 1',16,1,1);
/*!40000 ALTER TABLE `home_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_teamevent`
--

DROP TABLE IF EXISTS `home_teamevent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_teamevent` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fk_event_id` bigint(20) NOT NULL,
  `fk_team_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_teamevent_fk_event_id_3ee021ed_fk_home_event_id` (`fk_event_id`),
  KEY `home_teamevent_fk_team_id_f5e4e1f9_fk_home_team_id` (`fk_team_id`),
  CONSTRAINT `home_teamevent_fk_event_id_3ee021ed_fk_home_event_id` FOREIGN KEY (`fk_event_id`) REFERENCES `home_event` (`id`),
  CONSTRAINT `home_teamevent_fk_team_id_f5e4e1f9_fk_home_team_id` FOREIGN KEY (`fk_team_id`) REFERENCES `home_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_teamevent`
--

LOCK TABLES `home_teamevent` WRITE;
/*!40000 ALTER TABLE `home_teamevent` DISABLE KEYS */;
INSERT INTO `home_teamevent` VALUES (1,1,1);
/*!40000 ALTER TABLE `home_teamevent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-20 11:17:15
