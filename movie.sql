-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2024 at 07:43 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `movie`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `uname` varchar(20) NOT NULL,
  `seat` varchar(50) NOT NULL,
  `amount` varchar(10) NOT NULL,
  `movie` varchar(5) NOT NULL,
  `total_seats` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`uname`, `seat`, `amount`, `movie`, `total_seats`) VALUES
('aanchal8', 'A1,A2,A3,A4,A5,A6,B1,B2,B3,B4,B5,', '2090', '1', '11'),
('aman23', 'C9,C10,C11,D9,D10,D11,E9,E10,E11,', '1650', '2', '9'),
('rashmi89', 'A12,A13,A14,A15,B12,B13,B14,B15,C12,C13,C14,D12,D1', '2630', '3', '14'),
('devs34', 'F9,F10,F11,G9,G10,H9,H10,', '1220', '2', '7'),
('hi7890', 'D7,D8,E7,E8,F7,F8,F9,', '1260', '1', '7'),
('aman1306', 'B7,B8,B9,C7,C8,C9,D7,D8,E7,E8,', '1860', '2', '10'),
('prachi10', 'H9,H10,H11,I9,I10,', '850', '1', '5'),
('varun78', 'H17,H18,H19,I17,I18,I19,J18,J19,', '1360', '2', '8'),
('rajm89', 'G8,G9,G10,H9,H10,', '850', '3', '5'),
('jass45', 'D3,D4,E3,E4,E5,F3,F4,F5,', '1440', '1', '8'),
('aradhya01', 'A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,', '2090', '1', '11'),
('varu_123', 'A1,A2,A3,A4,', '760', '2', '4'),
('im_deepakkumar', 'J1,J2,J3,J4,', '680', '1', '4'),
('ram_123', 'D5,D6,D7,E5,E6,E7,', '1080', '1', '6'),
('rajs456', 'C8,C9,C10,D8,D9,D10,', '1110', '2', '6'),
('rajs123', 'D16,D17,D18,D19,E17,E18,E19,', '1260', '3', '7'),
('rajesh123', 'D14,D15,D16,E14,E15,E16,', '1080', '2', '6'),
('archna85', 'A17,A18,A19,A20,A21,A22,', '1140', '1', '6');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `mobile` varchar(13) NOT NULL,
  `fullname` varchar(30) NOT NULL,
  `name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`mobile`, `fullname`, `name`, `password`) VALUES
('8307571895', 'Aanchal Jain', 'aanchal8', '123456'),
('7410852963', 'Amandeep Singh', 'aman23', '124578'),
('8307556926', 'rashmi', 'rashmi89', '7410852'),
('7410852369', 'Dev Sharma', 'devs34', '147852'),
('7418529630', 'Himashi', 'hi7890', '8520'),
('7854123690', 'amandeep singh', 'aman1306', 'aman13'),
('78945612300', 'Prachi Dhiman', 'prachi10', '45612'),
('7415986230', 'Varun Shah', 'varun78', 'varu78'),
('8945673012', 'Raj Malik', 'rajm89', 'rajm8'),
('1598743602', 'Jaismeen Kaur', 'jass45', 'jass89'),
('8520147963', 'Aradhya Jain', 'aradhya01', '1470'),
('6239431703', 'Varun Shah', 'varu_123', 'varun08'),
('8053022989', 'Deepak Kumar', 'im_deepakkumar', 'Deeapk@123'),
('7894561237', 'raman', 'ram_123', 'ram123'),
('7412589630', 'Rajni Sharma', 'rajni456', 'rajni@456'),
('7458961234', 'Rajni Sharma', 'rajni789', 'rajni@789'),
('7458123697', 'Raman Kumar', 'raman123', 'Raman@123'),
('7412589630', 'Rajesh Kumar', 'rajesh123', 'raj@123'),
('7458963218', 'Archna Jain', 'archna85', 'archna@85');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
