-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Vært: mariadb
-- Genereringstid: 28. 09 2026 kl. 20:35:42
-- Serverversion: 10.6.20-MariaDB-ubu2004
-- PHP-version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodhead`
--

-- --------------------------------------------------------

--
-- Struktur-dump for tabellen `countries`
--

CREATE TABLE `countries` (
  `country_id` char(32) NOT NULL,
  `country_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Data dump for tabellen `countries`
--

INSERT INTO `countries` (`country_id`, `country_name`) VALUES
('1', 'Denmark'),
('2', 'Germany');

-- --------------------------------------------------------

--
-- Struktur-dump for tabellen `ingridients`
--

CREATE TABLE `ingridients` (
  `ingridient_id` char(32) NOT NULL,
  `recipe_fk` char(32) NOT NULL,
  `ingridient_names` varchar(50) NOT NULL,
  `ingridient_amounts` varchar(10) NOT NULL,
  `ingridient_units` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Data dump for tabellen `ingridients`
--

INSERT INTO `ingridients` (`ingridient_id`, `recipe_fk`, `ingridient_names`, `ingridient_amounts`, `ingridient_units`) VALUES
('021d659a0f9745968b8d918bc9c7b3b8', '03cbad3980e64bf6923fcd20bf2605cb', 'DD', '222', 'g'),
('04499c22d7d74039b4b42a9fd3e94479', '6389e0182fe14449a82ded0bb695f015', 'DD', '222', 'g'),
('0459b1d4946442239adff4e15e49c5d3', '12ca42a69c334fae817bae027c3286fb', 'Cornstarch', '15', 'g'),
('0a6a048fb3d6404bb01a6bfcc3c4383b', '5ed583affc8f412f82ca266a0f0c08cb', 'DD', '222', 'g'),
('1', '', '', '', ''),
('1088eebd5f9e4874b22236a2682ef8cf', '912d1260b6fa4525820c19e5dfe64ed0', 'Rucola', '1', 'pcs'),
('128c7d00fcf4409198e9160a237aa7ed', '12ca42a69c334fae817bae027c3286fb', 'Eggs', '2', ''),
('132afe819d2b4c2eb6202727e4867490', '9a135cc0fb4b4cf29644d6ab2077a4be', 'DD', '222', 'g'),
('134803ea57f54a1aa415f8f1bad5c14f', '5e021f48e9ae4f6eb67ed9f7041a1ee2', 'DD', '222', 'g'),
('1579ad1211194cfb9af0ace5a31f70b9', '912d1260b6fa4525820c19e5dfe64ed0', 'Tomatoe', '1', 'pcs'),
('18f37921c0b24c5fb473b2566c1b4fa3', '12ca42a69c334fae817bae027c3286fb', 'Salt', '1', 'pinch'),
('1e316713b46d4a668b100d7a8fca7f8f', 'a64cf46c0cb34210a27744e7e2ee7698', 'DD', '222', 'g'),
('1facc4ab6441442e93c86ceede79eece', '12ca42a69c334fae817bae027c3286fb', 'Ice cold water (if necessary)', '50', 'ml'),
('1fc7e124f5c64179a0cebf7123b4ede0', 'bc71b34e67b1492994a39d262e7399c7', 'DD', '222', 'g'),
('2', '', '', '', ''),
('212d7ad711e8486dbedfaab587a1f79c', '03cbad3980e64bf6923fcd20bf2605cb', 'CC', '111', 'L'),
('2a0b3640419440da919953a63b499bd7', 'e37a01921b5b424a97adc03cd720c70a', 'CC', '111', 'L'),
('34442f2c47204e378e67fcfb9b53a17f', '12ca42a69c334fae817bae027c3286fb', 'Cold butter', '120', 'g'),
('37687efd113c44829a5e50e973885be8', 'eaf3abc030ef4501afd7922f20c48c17', '', '222', 'g'),
('3cc30c5372a1478f9a0eff0ba84cef5e', '89c3c23908814e0a9409aa3dcba90c5e', 'DD', '222', 'g'),
('44f9ebc097f9464fa36f8c1f94264faa', 'ee7a0b3dd2af4603a27758afa4f7701a', 'DD', '222', 'g'),
('457a2d63ac3547b4a1114ab6af723321', 'b43f2ad34fb146a0894594d3748bab4c', 'CC', '111', 'L'),
('46c4d5996d4343169a7f6f01627b3b57', '4c3ae7de4533480eba020e8d3e1dade9', 'CC', '111', 'L'),
('48c3375e14fb41f2b100a6092ad77cf7', 'a82afb5213b14221a35aa628688dc459', 'CC', '111', 'L'),
('4dbf066c58b849f28e6143b9ae79b404', '12ca42a69c334fae817bae027c3286fb', 'Egg', '1', ''),
('5b8af210799c40f1aea1058e73fc3afe', '83ab6c184cfe4e8c88e858bd74062e3b', 'CC', '111', 'L'),
('5d499b91277641528fa69ee8a02c05d1', 'a64cf46c0cb34210a27744e7e2ee7698', 'CC', '111', 'L'),
('5d7632c3fec648e68ed8cf8d1e9fb114', '692324440b19407a8771da6ed0d209d9', 'DD', '222', 'g'),
('5f7435f15a914551a4e04648c3cb9f22', 'ee7a0b3dd2af4603a27758afa4f7701a', 'CC', '111', 'L'),
('6544991464e14678a7af24f90352bd5f', 'eaf3abc030ef4501afd7922f20c48c17', '', '111', 'L'),
('66c4129b345b4ca99b983d8c71d9c8e2', '6389e0182fe14449a82ded0bb695f015', 'CC', '111', 'L'),
('6e5e0e88c9084b04be0d2d0de4a653ba', '692324440b19407a8771da6ed0d209d9', 'CC', '111', 'L'),
('7b6c2103e27e4a638527f4a3d633f2f3', '4429c1500b68443ba5e75e56d3115ac0', 'CC', '111', 'L'),
('7ed868af909448a2b0a21a72802173c0', '12ca42a69c334fae817bae027c3286fb', 'Lemon', '1', ''),
('8273585e9c82416cbeab1bd3ed3fac20', 'bc71b34e67b1492994a39d262e7399c7', 'CC', '111', 'L'),
('8a33946794be47fb9933cd304edcd6c7', '5e021f48e9ae4f6eb67ed9f7041a1ee2', 'CC', '111', 'L'),
('8dc94bea209d458086bba3a33357822f', '12ca42a69c334fae817bae027c3286fb', 'White sugar', '125', 'g'),
('90a7e12f75ee49b8b660111e37478fa4', 'f6b3d89a11b64ba59531e659853fb6e6', 'DD', '222', 'g'),
('94ea91364658428ab8bc00aa90078f09', '096f4354068e4c168d6d2b9bf7ae968c', 'CC', '111', 'L'),
('9cefef03630849b3bafb10063a28fdbb', '912d1260b6fa4525820c19e5dfe64ed0', 'Mozarella Cheese', '50', 'g'),
('9f190236907340639bb19d8b934703a5', '89c3c23908814e0a9409aa3dcba90c5e', 'CC', '111', 'L'),
('a291e74d86ec413d9c4fffe947362629', '12ca42a69c334fae817bae027c3286fb', 'Eggyolk', '2', ''),
('a49501fd47c34438a705dfb16f9faf7e', 'b43f2ad34fb146a0894594d3748bab4c', 'DD', '222', 'g'),
('a703e22d0a744fbab4e33cf9fe9c9df8', '096f4354068e4c168d6d2b9bf7ae968c', 'DD', '222', 'g'),
('a788aaa2586147a0b2d4e40ea6a6474a', '9dd8be7b998f47a6b42f4bba0a2f9555', '', '111', 'L'),
('a80727ed46c246d58acc06743ae08a5a', '690a0954fed74f5988dffe487d13c8cb', 'CC', '111', 'L'),
('b532e3d3eae441748e4f2e7418ef8e11', 'ec8c73a2a4e74169b763a0fffcc8c106', 'DD', '222', 'g'),
('b972dcf3240b470c8920b8aa28a60a36', '690a0954fed74f5988dffe487d13c8cb', 'DD', '222', 'g'),
('bb62250f65644d80870c199e9ba7605f', 'a82afb5213b14221a35aa628688dc459', 'DD', '222', 'g'),
('bdafba1110364490b87af07aba0bb42d', '12ca42a69c334fae817bae027c3286fb', 'Cold diced butter', '50', 'g'),
('bdff531ae37e43248f94b7e7b6d139a9', '9a135cc0fb4b4cf29644d6ab2077a4be', 'CC', '111', 'L'),
('c097a7778fa94138991c282184996ec7', '5ed583affc8f412f82ca266a0f0c08cb', 'CC', '111', 'L'),
('c127cdd19f104d17a4960cef911a3126', '4c3ae7de4533480eba020e8d3e1dade9', 'DD', '222', 'g'),
('c890af79127e4f36b0c9e12d865c1efa', '12ca42a69c334fae817bae027c3286fb', 'Lemonjuice', '150', 'ml'),
('cb0deb2a306d4836b93f7f9d509dd78b', 'e37a01921b5b424a97adc03cd720c70a', 'DD', '222', 'g'),
('e0b9b0791aaa45119dce8b34899fa721', '4429c1500b68443ba5e75e56d3115ac0', 'DD', '222', 'g'),
('e2e22246382844548df4af8ded63cbfb', 'ec8c73a2a4e74169b763a0fffcc8c106', 'CC', '111', 'L'),
('e39172c29ee74a1199b26c112eb53a70', '12ca42a69c334fae817bae027c3286fb', 'Cakeflour', '240', 'g'),
('ed29851549d342108c5ce182978b35b1', 'e71d8cfea6074e15a6afd56847fc3f36', 'DD', '222', 'g'),
('ee473b7a08d14ecba8545f7dbc66d4b6', '12ca42a69c334fae817bae027c3286fb', 'Powdered sugar', '50', 'g'),
('f3dc102448b2454fa119655651dd17ba', 'e71d8cfea6074e15a6afd56847fc3f36', 'CC', '111', 'L'),
('f50067d8d104460fa8be0561542ccbeb', '912d1260b6fa4525820c19e5dfe64ed0', 'Serrano ham', '1', ''),
('f8c67b28662b49caaba6b724c6f27f43', '83ab6c184cfe4e8c88e858bd74062e3b', 'DD', '222', 'g'),
('fc3fb9c204c440ec8ea9522baa12f8a4', 'f6b3d89a11b64ba59531e659853fb6e6', 'CC', '111', 'L');

-- --------------------------------------------------------

--
-- Struktur-dump for tabellen `instructions`
--

CREATE TABLE `instructions` (
  `instruction_id` char(32) NOT NULL,
  `recipe_fk` char(32) NOT NULL,
  `instruction` varchar(500) NOT NULL,
  `instruction_step_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Data dump for tabellen `instructions`
--

INSERT INTO `instructions` (`instruction_id`, `recipe_fk`, `instruction`, `instruction_step_number`) VALUES
('062f6ef7719b41e1a80c12c8c6e263dc', '12ca42a69c334fae817bae027c3286fb', 'Grease a 24 cm tart tin with butter and when ready place the dough into the tart tin and gently press it into the bottom and sides.\r\nTrim the edges neatly to create an even finish. Prick the bottom of the tart crust several times with a fork.', 4),
('1858012254574e25a486e138531797ef', '912d1260b6fa4525820c19e5dfe64ed0', 'Cut the bought sourdough in half and toast both sides', 1),
('33961387645543d482771aa03daf93b8', '12ca42a69c334fae817bae027c3286fb', 'Roll out the dough between two sheets of baking paper and refrigerate the dough for 30 minutes.', 3),
('35f23987ab2e4edd977df4dbe7e51a69', '12ca42a69c334fae817bae027c3286fb', 'Add the water and sugar to a saucepan.\r\nBring the mixture to a boil and heat it to exactly 118°C. Use a sugar thermometer to monitor the temperature.', 9),
('3615dc91e1d9499ca8ea9411c5b4f654', 'e71d8cfea6074e15a6afd56847fc3f36', 'Aaaah', 1),
('37eda8227bf648578b7b924a4fd344b5', '12ca42a69c334fae817bae027c3286fb', 'Cover the dough with baking paper and fill the tart with dried beans for blind baking and blind bake in a preheated 175°C fan oven for approximately 15 minutes.', 5),
('43f0caa5be644577a3a07f4632f45a3a', '12ca42a69c334fae817bae027c3286fb', 'Add the flour, icing sugar, salt, and butter to a food processor. Process until the mixture is smooth and evenly combined.', 1),
('4e1e31b531fa490591dec3e1f27018a3', '12ca42a69c334fae817bae027c3286fb', 'Remove the saucepan from the heat.\r\nGradually whisk in the butter, a little at a time, until completely incorporated.\r\nPour the lemon cream into the baked tart crust and spread it evenly.\r\nPlace the tart in the refrigerator to chill.', 8),
('68ad2750090c4bd6b4f7f743a69e9a6c', '4c3ae7de4533480eba020e8d3e1dade9', 'Sweet', 1),
('70f14682080549af981f1eb935bb9ba6', '12ca42a69c334fae817bae027c3286fb', 'Add the eggs, egg yolks, sugar, lemon juice, lemon zest, and cornstarch to a saucepan.\r\nWhisk everything together.\r\nSlowly heat the mixture over medium heat, stirring constantly, until the mixture thickens.', 7),
('8a2bdd57414342f0a4e4ffe60879a356', '9a135cc0fb4b4cf29644d6ab2077a4be', 'Woooow', 1),
('a4e42d747ea84ef88d66b4a83290a9dd', '12ca42a69c334fae817bae027c3286fb', 'Transfer the meringue to a piping bag fitted with a large star nozzle.\r\nPipe many closely spaced meringue peaks over the surface of the tart.\r\nUse a kitchen blowtorch to carefully toast the meringue peaks until they are beautifully golden.', 11),
('a54075bf620c44aa8288cc8165a5b2ed', '12ca42a69c334fae817bae027c3286fb', 'Remove the tart from the oven. Carefully remove the baking paper and dried beans. Return the tart to the oven and bake for another 5–8 minutes, until the crust is lightly golden. Remove from the oven and allow the tart crust to cool slightly.', 6),
('b3562020eca2429d9c6e8654236376c8', '12ca42a69c334fae817bae027c3286fb', 'Serve (:', 12),
('b95b60daa6b64bb7b30425492d9dc6d3', '912d1260b6fa4525820c19e5dfe64ed0', 'Slightly flame the op of the open half the cheese', 3),
('c01c5b6f494e414dafb5b01a20ba8a72', '912d1260b6fa4525820c19e5dfe64ed0', 'Finish by putting the other half on top of the sandwich', 4),
('c07ee331caa0407ab75ef9a42750aa68', '12ca42a69c334fae817bae027c3286fb', 'Transfer the mixture to a bowl. Add the beaten egg and mix until the dough comes together. Add a little cold water if necessary.', 2),
('d13e444ae9994499b397b879fadb84cf', '12ca42a69c334fae817bae027c3286fb', 'Meanwhile, whisk the egg whites until they are light, fluffy, and stiff.\r\nSlowly pour the hot sugar syrup into the egg whites in a thin, steady stream while continuing to whisk.\r\nAdd the salt and lemon juice and whisk until incorporated.', 10),
('e53c0192c23441f7a9984634d095daa8', 'a64cf46c0cb34210a27744e7e2ee7698', 'Wowsa', 1),
('e7cabb1a9ae946919910e3bf45bfe9ba', '096f4354068e4c168d6d2b9bf7ae968c', 'Yummy', 1),
('f40310fed761432ca1f570bddcbc6851', '912d1260b6fa4525820c19e5dfe64ed0', 'Add rucola, serrano, tomatoe and mozarella cheese in this order', 2),
('f630ee1848f44e8098332afc93716498', '690a0954fed74f5988dffe487d13c8cb', 'mmmmmh', 1),
('f87b0d4f746d4933a5a104a508d8b17b', '6389e0182fe14449a82ded0bb695f015', 'Woooo', 1);

-- --------------------------------------------------------

--
-- Struktur-dump for tabellen `recipes`
--

CREATE TABLE `recipes` (
  `recipe_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  `recipe_title` varchar(50) NOT NULL,
  `recipe_description` varchar(255) NOT NULL,
  `recipe_img_key` text NOT NULL,
  `recipe_servings` int(11) NOT NULL,
  `recipe_prep_time` int(11) NOT NULL,
  `recipe_cook_time` int(11) NOT NULL,
  `recipe_created_at` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Data dump for tabellen `recipes`
--

INSERT INTO `recipes` (`recipe_id`, `user_id`, `recipe_title`, `recipe_description`, `recipe_img_key`, `recipe_servings`, `recipe_prep_time`, `recipe_cook_time`, `recipe_created_at`) VALUES
('096f4354068e4c168d6d2b9bf7ae968c', '4713bf5f3bff4c288caeb69152db26ae', 'Sourdoughbuns', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '5b4872ac59914b0589164410e581862d.webp', 4, 60, 30, 1773412357),
('12ca42a69c334fae817bae027c3286fb', '4713bf5f3bff4c288caeb69152db26ae', 'Lemon Meringue Pie', 'This lemon meringue pie is perfect for sharing. The homemade lemon curd filling is flavored with lemon juice and zest. It’s tart, smooth, and pairs perfectly with the sweet and fluffy meringue topping.', '1917975f922d471cb5c1017a7b0ff0d8.png', 10, 30, 10, 1773413744),
('4c3ae7de4533480eba020e8d3e1dade9', '4713bf5f3bff4c288caeb69152db26ae', 'Cardamombuns', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '48fa4a40bdb047c190673d3629a55ae1.webp', 4, 60, 30, 1773412357),
('6389e0182fe14449a82ded0bb695f015', '4713bf5f3bff4c288caeb69152db26ae', 'Elderflowermouse cake with lemoncurd', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'd780684c550d478e9339ae968945cb6f.webp', 4, 60, 30, 1773412357),
('690a0954fed74f5988dffe487d13c8cb', '4713bf5f3bff4c288caeb69152db26ae', 'Birthdaycake', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '43a6262288344926810269c10c6bf786.webp', 4, 60, 30, 1773412357),
('912d1260b6fa4525820c19e5dfe64ed0', '4713bf5f3bff4c288caeb69152db26ae', 'Serrano Sandwich with Sourdoughbread', 'This recipe is an easy and quick way to make some lunch on a summer day.', '1d532eb6d08c4750a690d298ff3df869.jpg', 1, 10, 0, 1773414011),
('9a135cc0fb4b4cf29644d6ab2077a4be', '4713bf5f3bff4c288caeb69152db26ae', 'Raspberrymouse cake with chocolate ganache', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'e9e315c9c6d747d992e4161460b8016a.webp', 4, 60, 30, 1773413393),
('a64cf46c0cb34210a27744e7e2ee7698', '4713bf5f3bff4c288caeb69152db26ae', 'Chocolate Chip Cookies', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'fae7b48ba04c4b29a952e8d7eb6924ac.webp', 4, 60, 30, 1773413412),
('e71d8cfea6074e15a6afd56847fc3f36', '4713bf5f3bff4c288caeb69152db26ae', 'Chocolatemouse cake with raspberry &  licorice', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '2c7864f0970240f48893d8844181a40e.webp', 4, 60, 30, 1773412529);

-- --------------------------------------------------------

--
-- Struktur-dump for tabellen `recipes_ingridients`
--

CREATE TABLE `recipes_ingridients` (
  `recipe_fk` char(32) NOT NULL,
  `ingridient_fk` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur-dump for tabellen `users`
--

CREATE TABLE `users` (
  `user_id` char(32) NOT NULL,
  `user_username` varchar(20) NOT NULL,
  `user_first_name` varchar(20) NOT NULL,
  `user_last_name` varchar(20) NOT NULL,
  `user_country_id` char(32) NOT NULL,
  `user_phone` varchar(20) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `user_created_at` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Data dump for tabellen `users`
--

INSERT INTO `users` (`user_id`, `user_username`, `user_first_name`, `user_last_name`, `user_country_id`, `user_phone`, `user_password`, `user_email`, `user_created_at`) VALUES
('4713bf5f3bff4c288caeb69152db26ae', 'Test', 'Food', 'Head', '1', '12345678', 'scrypt:32768:8:1$fpHrStCWC0JK8tQO$a57dfd6d9669d574d66aa81c77e7c1411bc95ee029ded02b518fb025a49fa0b17309768ec4d5850dc6980ef4d5d18a4c4090ddca52d2811463173e93f06d28e7', 'test@123.com', 1773265128);

--
-- Begrænsninger for dumpede tabeller
--

--
-- Indeks for tabel `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_id`),
  ADD UNIQUE KEY `country_name` (`country_name`);

--
-- Indeks for tabel `ingridients`
--
ALTER TABLE `ingridients`
  ADD PRIMARY KEY (`ingridient_id`);

--
-- Indeks for tabel `instructions`
--
ALTER TABLE `instructions`
  ADD PRIMARY KEY (`instruction_id`),
  ADD KEY `recipe_fk` (`recipe_fk`);

--
-- Indeks for tabel `recipes`
--
ALTER TABLE `recipes`
  ADD PRIMARY KEY (`recipe_id`);

--
-- Indeks for tabel `recipes_ingridients`
--
ALTER TABLE `recipes_ingridients`
  ADD PRIMARY KEY (`recipe_fk`,`ingridient_fk`),
  ADD KEY `ingridient_fk` (`ingridient_fk`);

--
-- Indeks for tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD UNIQUE KEY `user_username` (`user_username`),
  ADD KEY `user_country_id` (`user_country_id`);

--
-- Begrænsninger for dumpede tabeller
--

--
-- Begrænsninger for tabel `instructions`
--
ALTER TABLE `instructions`
  ADD CONSTRAINT `instructions_ibfk_1` FOREIGN KEY (`recipe_fk`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE;

--
-- Begrænsninger for tabel `recipes_ingridients`
--
ALTER TABLE `recipes_ingridients`
  ADD CONSTRAINT `recipes_ingridients_ibfk_1` FOREIGN KEY (`ingridient_fk`) REFERENCES `ingridients` (`ingridient_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `recipes_ingridients_ibfk_2` FOREIGN KEY (`recipe_fk`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE;

--
-- Begrænsninger for tabel `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_country_id`) REFERENCES `countries` (`country_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
