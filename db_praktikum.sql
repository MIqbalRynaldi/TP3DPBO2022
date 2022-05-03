-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2022 at 03:39 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_praktikum`
--

-- --------------------------------------------------------

--
-- Table structure for table `fasilitas_kampus`
--

CREATE TABLE `fasilitas_kampus` (
  `id_fasilitas` int(11) NOT NULL,
  `nama_fasilitas` varchar(255) DEFAULT NULL,
  `img_fasilitas` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fasilitas_kampus`
--

INSERT INTO `fasilitas_kampus` (`id_fasilitas`, `nama_fasilitas`, `img_fasilitas`) VALUES
(1, 'Ruang Perkuliahan', 'ruangbelajar.png'),
(2, 'Laboratorium', 'labolatorium.png'),
(3, 'Tempat Ibadah', 'tempatibadah.png'),
(4, 'Perpustakaan', 'perpustakaan.png'),
(5, 'Sarana Olahraga', 'saranaolahraga.png');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `id` int(11) NOT NULL,
  `nim` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jurusan` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  `hobi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `jurusan`, `jenis_kelamin`, `hobi`) VALUES
(1, '1992131', 'Asep Kurnia', 'Teknik Kedokteran', 'Laki-Laki', 'Makan'),
(2, '199233', 'Jajang ', 'Pendidikan Gaming', 'Laki-Laki', 'Makan'),
(3, '19923366', 'Ridwan Hehehe', 'Sastra Mesin', 'Perempuan', 'Bermain Game');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fasilitas_kampus`
--
ALTER TABLE `fasilitas_kampus`
  ADD PRIMARY KEY (`id_fasilitas`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fasilitas_kampus`
--
ALTER TABLE `fasilitas_kampus`
  MODIFY `id_fasilitas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
