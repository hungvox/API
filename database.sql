CREATE TABLE `User` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `password` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `Island` (
  `id` integer PRIMARY KEY,
  `longitude` float,
  `latitude` float,
  `area` float,
  `detected_time` timestamp
);

CREATE TABLE `Comment` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `island_id` integer,
  `comment_text` text,
  `created_at` timestamp
);

CREATE TABLE `Media` (
  `id` integer PRIMARY KEY,
  `comment_id` integer,
  `media_type` varchar(255),
  `media_data` text,
  `created_at` timestamp
);

ALTER TABLE `Comment` ADD FOREIGN KEY (`user_id`) REFERENCES `User` (`id`);

ALTER TABLE `Comment` ADD FOREIGN KEY (`island_id`) REFERENCES `Island` (`id`);

ALTER TABLE `Media` ADD FOREIGN KEY (`comment_id`) REFERENCES `Comment` (`id`);
