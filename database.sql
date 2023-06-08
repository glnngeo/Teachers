--teacher info 1st to copy and paste

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `year_grad` varchar(255) NOT NULL,
  `rank` varchar(255) NOT NULL,
  `expe` varchar(255) NOT NULL,
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


INSERT INTO `teachers` (`id`, `name`, `year_grad`, `rank`, `expe`) VALUES
(23, 'motech noel', '2012', 'teacher 1', '2 years'),
(24, 'Thiago moses', '2020', 'teacher 2', '3 years'),
(25, 'Saratex Marie', '2021', 'teacher 3', '4 years'),
(26, 'Kamonyo Kiiza', '2022', 'teacher 4', '5 years');

ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;


--accounts 2nd to copy and paste


CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `users` (`username`, `password`)
VALUES
  ('motech', 'motech123'),
  ('Thiago', 'moses321'),
  ('Saratex', 'Saratex456'),
  ('Kamonyo', 'Kamonyo654');

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;