/*
SQLyog Professional v12.08 (64 bit)
MySQL - 5.7.29-log : Database - operbench
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


/*Data for the table `alembic_version` */



/*Data for the table `api_permission` */

INSERT  INTO `api_permission`(`api_permission_id`,`api_permission_url`,`api_permission_method_type`,`note`,`create_at`,`update_at`,`status`) VALUES (1,'/api/v1/cmdb/servers/','GET',NULL,NULL,NULL,NULL),(2,'/api/v1/user/','GET',NULL,NULL,NULL,NULL);

/*Data for the table `api_token` */

INSERT  INTO `api_token`(`api_token_id`,`api_token_appid`,`api_token_secretkey`,`user_profile_id`,`note`,`create_at`,`update_at`,`status`) VALUES (1,'Appid00002','ThisIsSecuretKey0002',1,NULL,NULL,NULL,NULL);

/*Data for the table `api_token_permissions` */

INSERT  INTO `api_token_permissions`(`api_token_id`,`api_permission_id`) VALUES (1,1);

/*Data for the table `asset` */

INSERT  INTO `asset`(`asset_id`,`asset_asset_type`,`asset_hostname`,`asset_sn`,`manufactory_id`,`asset_model`,`asset_warranty`,`business_unit_id`,`admin_id`,`idc_id`,`asset_floor`,`asset_cabinet_num`,`asset_cabinet_order`,`asset_status`,`asset_maintain_record`,`note`,`create_at`,`update_at`,`status`) VALUES (1,'NETWORK','host134','sn1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'NETWORK','host135','sn2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,NULL,'123','-1814222737109052736',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,NULL,'123','5945199289917090229',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Data for the table `business_unit` */

/*Data for the table `business_unit_users` */

/*Data for the table `disk` */

/*Data for the table `idc` */

/*Data for the table `manufactory` */

/*Data for the table `memory` */

/*Data for the table `nic` */

INSERT  INTO `nic`(`nic_id`,`nic_name`,`nic_model`,`server_id`,`nic_ipaddr`,`nic_mac`,`nic_netmask`,`note`,`create_at`,`update_at`,`status`) VALUES (1,'eth0',NULL,3,'123',NULL,NULL,NULL,NULL,NULL,NULL),(2,'eth0',NULL,4,'222',NULL,NULL,NULL,NULL,NULL,NULL);

/*Data for the table `os` */

/*Data for the table `role` */

INSERT  INTO `role`(`role_id`,`role_name`) VALUES (1,'admin'),(2,'cmdb');

/*Data for the table `role_permissions` */

INSERT  INTO `role_permissions`(`role_id`,`api_permission_id`) VALUES (1,1),(2,1),(1,2);

/*Data for the table `server` */

INSERT  INTO `server`(`server_id`,`asset_id`,`server_cpu_count`,`server_cpu_cour_count`,`server_cpu_model`,`server_raid_type`,`server_ram_size`,`server_os`,`note`,`create_at`,`update_at`,`status`) VALUES (1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Data for the table `tasklog` */

INSERT  INTO `tasklog`(`tasklog_id`,`task_id`,`tasklog_tid`,`tasklog_result`,`tasklog_create_time`,`user`) VALUES (1,NULL,'xxxx',NULL,'2020-03-25 22:40:19',NULL),(2,2,'48610096-ba1d-4db0-b7b0-d3e9322ac281',NULL,'2020-03-29 23:35:05',1),(3,2,'33d1fa06-9611-44f9-af6a-a716dcc0dceb',NULL,'2020-03-29 23:35:11',1),(4,3,'ca325956-2982-452b-823c-e4b130aaa640',NULL,'2020-03-29 23:35:14',1),(5,4,'10873296-34e5-48fb-b0a1-c38629d9d05b',NULL,'2020-03-29 23:36:43',1),(6,2,'204e31fa-b3e3-4f0b-8e94-d6fd82d8f1d3',NULL,'2020-03-29 23:53:05',1),(7,3,'56166b0f-bf2e-4b4e-9443-9b932d73591c',NULL,'2020-03-29 23:53:15',1);

/*Data for the table `tasks` */

INSERT  INTO `tasks`(`task_id`,`task_name`,`task_command`,`task_args`,`task_host`) VALUES (2,'yum ','yum install nginx','','192.168.0.2'),(3,'ls','ls -l','','192.168.0.1'),(4,'ls','ls','','101.37.24.87');

/*Data for the table `user_profile` */

INSERT  INTO `user_profile`(`user_profile_id`,`user_profile_name`,`user_profile_email`,`user_profile_mobile`,`password`,`note`,`create_at`,`update_at`,`status`,`role_id`) VALUES (1,'tlpYtxZS','cali@sl.com',NULL,'pbkdf2:sha256:150000$7kYJWSGF$14e9b8d0e91e9669297a5a8ce2b39d5a28e94533ec2b04ea10b9b6e14c8f040a',NULL,NULL,NULL,NULL,1),(2,'cali2@sl.com','cali2@sl.com',NULL,'pbkdf2:sha256:150000$81y7imuk$1a03bd4031114e3e2855ac2cd092940c1bd442d47d4cef57319a7273b8cfa942',NULL,NULL,NULL,NULL,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
