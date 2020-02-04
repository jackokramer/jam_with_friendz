-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema jam
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `jam` ;

-- -----------------------------------------------------
-- Schema jam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `jam` DEFAULT CHARACTER SET utf8 ;
USE `jam` ;

-- -----------------------------------------------------
-- Table `jam`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jam`.`users` ;

CREATE TABLE IF NOT EXISTS `jam`.`users` (
  `user_id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `c_password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `jam`.`extras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jam`.`extras` ;

CREATE TABLE IF NOT EXISTS `jam`.`extras` (
  `extra_id` INT(11) NOT NULL AUTO_INCREMENT,
  `college` VARCHAR(255) NULL DEFAULT NULL,
  `city` VARCHAR(255) NULL DEFAULT NULL,
  `instrument` VARCHAR(255) NULL DEFAULT NULL,
  `about` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`extra_id`),
  INDEX `fk_extras_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_extras_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `jam`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `jam`.`jams_sessions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jam`.`jams_sessions` ;

CREATE TABLE IF NOT EXISTS `jam`.`jams_sessions` (
  `jam_id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `number_of` TINYINT(9) NULL,
  `date` DATETIME NULL,
  `location` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`jam_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jam`.`users_jams`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jam`.`users_jams` ;

CREATE TABLE IF NOT EXISTS `jam`.`users_jams` (
  `users_user_id` INT(11) NOT NULL,
  `jams_sessions_jam_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`users_user_id`, `jams_sessions_jam_id`),
  INDEX `fk_users_has_jams_sessions_jams_sessions1_idx` (`jams_sessions_jam_id` ASC) VISIBLE,
  INDEX `fk_users_has_jams_sessions_users1_idx` (`users_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_jams_sessions_users1`
    FOREIGN KEY (`users_user_id`)
    REFERENCES `jam`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_jams_sessions_jams_sessions1`
    FOREIGN KEY (`jams_sessions_jam_id`)
    REFERENCES `jam`.`jams_sessions` (`jam_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
