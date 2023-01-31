-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2023 at 05:32 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vertex_crm`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_category`
--

CREATE TABLE `tbl_category` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `status` int(1) NOT NULL,
  `datetime` datetime NOT NULL,
  `ip` varchar(250) NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_leads`
--

CREATE TABLE `tbl_leads` (
  `id` int(11) NOT NULL,
  `companyname` varchar(250) NOT NULL,
  `address` text NOT NULL,
  `email` varchar(250) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `priority` int(1) NOT NULL COMMENT '0-cold, 1-hot',
  `expected_closing_date` date NOT NULL,
  `expected_value` varchar(50) NOT NULL,
  `lead_status` int(11) NOT NULL COMMENT '0-lead, 1-opportunity, 2-client',
  `lead_to_opportunity_date` datetime NOT NULL,
  `opportunity_to_client_date` datetime NOT NULL,
  `status` int(11) NOT NULL COMMENT '0-active, 1-deleted',
  `ip` varchar(250) NOT NULL,
  `datetime` datetime NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_leads_contacts`
--

CREATE TABLE `tbl_leads_contacts` (
  `id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `contact_name` varchar(250) NOT NULL,
  `designation` varchar(250) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `email` varchar(250) NOT NULL,
  `status` int(11) NOT NULL COMMENT '0-active, 1-deleted',
  `ip` varchar(250) NOT NULL,
  `datetime` datetime NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_leads_updates`
--

CREATE TABLE `tbl_leads_updates` (
  `id` int(11) NOT NULL,
  `lead_id` int(11) NOT NULL,
  `description` text NOT NULL,
  `status` int(1) NOT NULL COMMENT '0-active, 1-deleted',
  `datetime` datetime NOT NULL,
  `ip` varchar(250) NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_products`
--

CREATE TABLE `tbl_products` (
  `id` int(11) NOT NULL,
  `product_title` varchar(250) NOT NULL,
  `category_id` int(11) NOT NULL,
  `product_price` varchar(20) NOT NULL,
  `status` int(11) NOT NULL COMMENT '0-active, 1-deleted, 2-hidden',
  `datetime` datetime NOT NULL,
  `ip` varchar(250) NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_sales_target`
--

CREATE TABLE `tbl_sales_target` (
  `id` int(11) NOT NULL,
  `user_id` int(5) NOT NULL,
  `month` varchar(250) NOT NULL,
  `target_amount` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `ip` varchar(250) NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_users`
--

CREATE TABLE `tbl_users` (
  `id` int(11) NOT NULL,
  `usrname24` varchar(250) NOT NULL,
  `pswrd97` text NOT NULL,
  `name` varchar(250) NOT NULL,
  `designation` int(11) NOT NULL,
  `email` varchar(250) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `address` text NOT NULL,
  `country` varchar(100) NOT NULL,
  `usertype` int(1) NOT NULL COMMENT '0-admin, 1-user',
  `status` int(1) NOT NULL COMMENT '0-active, 1-deleted, 2-blocked',
  `datetime` datetime NOT NULL,
  `ip` varchar(250) NOT NULL,
  `added_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_category`
--
ALTER TABLE `tbl_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_leads`
--
ALTER TABLE `tbl_leads`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_leads_contacts`
--
ALTER TABLE `tbl_leads_contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_leads_updates`
--
ALTER TABLE `tbl_leads_updates`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_products`
--
ALTER TABLE `tbl_products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_sales_target`
--
ALTER TABLE `tbl_sales_target`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_users`
--
ALTER TABLE `tbl_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_category`
--
ALTER TABLE `tbl_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_leads`
--
ALTER TABLE `tbl_leads`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_leads_contacts`
--
ALTER TABLE `tbl_leads_contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_leads_updates`
--
ALTER TABLE `tbl_leads_updates`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_products`
--
ALTER TABLE `tbl_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_sales_target`
--
ALTER TABLE `tbl_sales_target`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_users`
--
ALTER TABLE `tbl_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
