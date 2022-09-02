-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bright_ideas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bright_ideas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bright_ideas` DEFAULT CHARACTER SET utf8 ;
USE `bright_ideas` ;

-- -----------------------------------------------------
-- Table `bright_ideas`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bright_ideas`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(150) NULL,
  `alias` VARCHAR(100) NULL,
  `email` VARCHAR(200) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bright_ideas`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bright_ideas`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `description` TEXT NULL,
  `users_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `bright_ideas`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bright_ideas`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bright_ideas`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `posts_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_posts1_idx` (`posts_id` ASC) VISIBLE,
  INDEX `fk_likes_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_posts1`
    FOREIGN KEY (`posts_id`)
    REFERENCES `bright_ideas`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `bright_ideas`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
