-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2019 at 03:48 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `techietech`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `srno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_no` varchar(50) NOT NULL,
  `message` varchar(50) NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`srno`, `name`, `email`, `phone_no`, `message`, `date`) VALUES
(1, 'Test', 'test@test.com', '123456', 'test test test', '2019-05-31 20:49:00'),
(2, 'meet thakkar', 'meetthakkar05@gmail.com', '8850662725', 'hey your blogs are awesome.', '2019-06-01 13:03:39'),
(3, 'Hiral Thakkar', 'hiralthakkar04@gmail.com', '9769322492', 'Hey i love your blogs!!!!!!!1', '2019-06-03 12:15:44');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `srno` int(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` varchar(180) NOT NULL,
  `caption` varchar(60) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `img_file` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`srno`, `title`, `slug`, `content`, `caption`, `date`, `img_file`) VALUES
(1, '1st post!', 'firstpost', 'This is my first Blog happy to see you here Welcome Aboard!!!!!', 'first', '2019-06-04 16:13:27', 'contact-bg.jpg'),
(2, '2nd post', 'second', 'I love Blogging', 'blogger', '2019-06-04 16:24:28', 'meet.png'),
(16, 'eryerueruy', 'eryerye', 'eryeryery', 'reyery', '2019-06-04 18:38:46', 'eruerureu'),
(17, 'eruerueu', 'euerueru', 'erueueu', 'eruetuery', '2019-06-04 18:39:01', ''),
(18, 'euerueru', 'eruerueur', ' yery reyrey ery rey', 'eytjjrt', '2019-06-04 18:39:15', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `srno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `srno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
