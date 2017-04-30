/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : chttp

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2017-04-20 20:19:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add tasksdata', '7', 'add_tasksdata');
INSERT INTO `auth_permission` VALUES ('20', 'Can change tasksdata', '7', 'change_tasksdata');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete tasksdata', '7', 'delete_tasksdata');
INSERT INTO `auth_permission` VALUES ('22', 'Can add user', '8', 'add_user');
INSERT INTO `auth_permission` VALUES ('23', 'Can change user', '8', 'change_user');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete user', '8', 'delete_user');
INSERT INTO `auth_permission` VALUES ('25', 'Can add task state', '9', 'add_taskmeta');
INSERT INTO `auth_permission` VALUES ('26', 'Can change task state', '9', 'change_taskmeta');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete task state', '9', 'delete_taskmeta');
INSERT INTO `auth_permission` VALUES ('28', 'Can add saved group result', '10', 'add_tasksetmeta');
INSERT INTO `auth_permission` VALUES ('29', 'Can change saved group result', '10', 'change_tasksetmeta');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete saved group result', '10', 'delete_tasksetmeta');
INSERT INTO `auth_permission` VALUES ('31', 'Can add interval', '11', 'add_intervalschedule');
INSERT INTO `auth_permission` VALUES ('32', 'Can change interval', '11', 'change_intervalschedule');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete interval', '11', 'delete_intervalschedule');
INSERT INTO `auth_permission` VALUES ('34', 'Can add crontab', '12', 'add_crontabschedule');
INSERT INTO `auth_permission` VALUES ('35', 'Can change crontab', '12', 'change_crontabschedule');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete crontab', '12', 'delete_crontabschedule');
INSERT INTO `auth_permission` VALUES ('37', 'Can add periodic tasks', '13', 'add_periodictasks');
INSERT INTO `auth_permission` VALUES ('38', 'Can change periodic tasks', '13', 'change_periodictasks');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete periodic tasks', '13', 'delete_periodictasks');
INSERT INTO `auth_permission` VALUES ('40', 'Can add periodic task', '14', 'add_periodictask');
INSERT INTO `auth_permission` VALUES ('41', 'Can change periodic task', '14', 'change_periodictask');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete periodic task', '14', 'delete_periodictask');
INSERT INTO `auth_permission` VALUES ('43', 'Can add worker', '15', 'add_workerstate');
INSERT INTO `auth_permission` VALUES ('44', 'Can change worker', '15', 'change_workerstate');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete worker', '15', 'delete_workerstate');
INSERT INTO `auth_permission` VALUES ('46', 'Can add task', '16', 'add_taskstate');
INSERT INTO `auth_permission` VALUES ('47', 'Can change task', '16', 'change_taskstate');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete task', '16', 'delete_taskstate');
INSERT INTO `auth_permission` VALUES ('49', 'Can add queue', '17', 'add_queue');
INSERT INTO `auth_permission` VALUES ('50', 'Can change queue', '17', 'change_queue');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete queue', '17', 'delete_queue');
INSERT INTO `auth_permission` VALUES ('52', 'Can add message', '18', 'add_message');
INSERT INTO `auth_permission` VALUES ('53', 'Can change message', '18', 'change_message');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete message', '18', 'delete_message');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for celery_taskmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_taskmeta`;
CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `result` longtext,
  `date_done` datetime NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `celery_taskmeta_662f707d` (`hidden`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of celery_taskmeta
-- ----------------------------

-- ----------------------------
-- Table structure for celery_tasksetmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_tasksetmeta`;
CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) NOT NULL,
  `result` longtext NOT NULL,
  `date_done` datetime NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taskset_id` (`taskset_id`),
  KEY `celery_tasksetmeta_662f707d` (`hidden`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of celery_tasksetmeta
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'scantool', 'tasksdata');
INSERT INTO `django_content_type` VALUES ('8', 'scantool', 'user');
INSERT INTO `django_content_type` VALUES ('9', 'djcelery', 'taskmeta');
INSERT INTO `django_content_type` VALUES ('10', 'djcelery', 'tasksetmeta');
INSERT INTO `django_content_type` VALUES ('11', 'djcelery', 'intervalschedule');
INSERT INTO `django_content_type` VALUES ('12', 'djcelery', 'crontabschedule');
INSERT INTO `django_content_type` VALUES ('13', 'djcelery', 'periodictasks');
INSERT INTO `django_content_type` VALUES ('14', 'djcelery', 'periodictask');
INSERT INTO `django_content_type` VALUES ('15', 'djcelery', 'workerstate');
INSERT INTO `django_content_type` VALUES ('16', 'djcelery', 'taskstate');
INSERT INTO `django_content_type` VALUES ('17', 'kombu_transport_django', 'queue');
INSERT INTO `django_content_type` VALUES ('18', 'kombu_transport_django', 'message');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-04-20 12:17:56');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-04-20 12:17:56');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-04-20 12:17:57');
INSERT INTO `django_migrations` VALUES ('12', 'djcelery', '0001_initial', '2017-04-20 12:17:58');
INSERT INTO `django_migrations` VALUES ('13', 'kombu_transport_django', '0001_initial', '2017-04-20 12:17:58');
INSERT INTO `django_migrations` VALUES ('14', 'scantool', '0001_initial', '2017-04-20 12:17:58');
INSERT INTO `django_migrations` VALUES ('15', 'scantool', '0002_delete_httpdata', '2017-04-20 12:17:58');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2017-04-20 12:17:58');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for djcelery_crontabschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_crontabschedule`;
CREATE TABLE `djcelery_crontabschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) NOT NULL,
  `hour` varchar(64) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(64) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_crontabschedule
-- ----------------------------

-- ----------------------------
-- Table structure for djcelery_intervalschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_intervalschedule`;
CREATE TABLE `djcelery_intervalschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_intervalschedule
-- ----------------------------

-- ----------------------------
-- Table structure for djcelery_periodictask
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictask`;
CREATE TABLE `djcelery_periodictask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime DEFAULT NULL,
  `total_run_count` int(10) unsigned NOT NULL,
  `date_changed` datetime NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `djcelery_periodictask_f3f0d72a` (`crontab_id`),
  KEY `djcelery_periodictask_1dcd7040` (`interval_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_periodictask
-- ----------------------------

-- ----------------------------
-- Table structure for djcelery_periodictasks
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictasks`;
CREATE TABLE `djcelery_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_periodictasks
-- ----------------------------

-- ----------------------------
-- Table structure for djcelery_taskstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_taskstate`;
CREATE TABLE `djcelery_taskstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) NOT NULL,
  `task_id` varchar(36) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `tstamp` datetime NOT NULL,
  `args` longtext,
  `kwargs` longtext,
  `eta` datetime DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `result` longtext,
  `traceback` longtext,
  `runtime` double DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `djcelery_taskstate_9ed39e2e` (`state`),
  KEY `djcelery_taskstate_b068931c` (`name`),
  KEY `djcelery_taskstate_863bb2ee` (`tstamp`),
  KEY `djcelery_taskstate_662f707d` (`hidden`),
  KEY `djcelery_taskstate_ce77e6ef` (`worker_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_taskstate
-- ----------------------------

-- ----------------------------
-- Table structure for djcelery_workerstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_workerstate`;
CREATE TABLE `djcelery_workerstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) NOT NULL,
  `last_heartbeat` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  KEY `djcelery_workerstate_f129901a` (`last_heartbeat`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djcelery_workerstate
-- ----------------------------

-- ----------------------------
-- Table structure for djkombu_message
-- ----------------------------
DROP TABLE IF EXISTS `djkombu_message`;
CREATE TABLE `djkombu_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `visible` tinyint(1) NOT NULL,
  `sent_at` datetime DEFAULT NULL,
  `payload` longtext NOT NULL,
  `queue_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djkombu_message_46cf0e59` (`visible`),
  KEY `djkombu_message_df2f2974` (`sent_at`),
  KEY `djkombu_message_75249aa1` (`queue_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djkombu_message
-- ----------------------------

-- ----------------------------
-- Table structure for djkombu_queue
-- ----------------------------
DROP TABLE IF EXISTS `djkombu_queue`;
CREATE TABLE `djkombu_queue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of djkombu_queue
-- ----------------------------

-- ----------------------------
-- Table structure for ip_data
-- ----------------------------
DROP TABLE IF EXISTS `ip_data`;
CREATE TABLE `ip_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(500) NOT NULL,
  `port` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `header` longtext NOT NULL,
  `appname` varchar(500) NOT NULL,
  `ipaddrs` varchar(500) NOT NULL,
  `domain` varchar(500) NOT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ip_data
-- ----------------------------

-- ----------------------------
-- Table structure for scantool_tasksdata
-- ----------------------------
DROP TABLE IF EXISTS `scantool_tasksdata`;
CREATE TABLE `scantool_tasksdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(500) NOT NULL,
  `taskname` varchar(500) NOT NULL,
  `taskdata` varchar(500) NOT NULL,
  `num` int(11) NOT NULL,
  `completenum` int(11) NOT NULL,
  `taskport` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of scantool_tasksdata
-- ----------------------------

-- ----------------------------
-- Table structure for scantool_user
-- ----------------------------
DROP TABLE IF EXISTS `scantool_user`;
CREATE TABLE `scantool_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `cookie` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of scantool_user
-- ----------------------------
INSERT INTO `scantool_user` VALUES ('1', 'admin', 'admin', null);
