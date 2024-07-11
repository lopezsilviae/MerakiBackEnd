CREATE DATABASE  IF NOT EXISTS `meraki` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `meraki`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: meraki
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pedidosproductos`
--

DROP TABLE IF EXISTS `pedidosproductos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidosproductos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_solicitante` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `cp` int NOT NULL,
  `producto` varchar(45) NOT NULL,
  `cantidad` int NOT NULL DEFAULT '1',
  `estado` varchar(10) NOT NULL DEFAULT 'pedido',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidosproductos`
--

LOCK TABLES `pedidosproductos` WRITE;
/*!40000 ALTER TABLE `pedidosproductos` DISABLE KEYS */;
insert into pedidosproductos 
values (1,'Analia', 'analia@hotmail.com',1231234545,'san martin 4589',1245,'llavero',50,'pedido'),(2,'luis','luis@gmail.com','23456789','casa 897',2345,'lampara',7,'realizado'),(3,'ana','luis@gmail.com','23456789','casa 897',2345,'llavero',10,'pedido'),(6,'pepe','fff@ppp.com','4545454123','jose per 345',1234,'portaretrato',3,'realizado'),(7,'pedro','pedro@gmail.com','7823234534','castell 67899',2335,'lampara',4,'realizado'),(8,'juan','fff@ppp.com','4545454545','la fayette 12345',4567,'portaretrato',10,'pedido');


/*!40000 ALTER TABLE `pedidosproductos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-09  9:23:24
