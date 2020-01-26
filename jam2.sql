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
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `jam`.`extras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jam`.`extras` ;

CREATE TABLE IF NOT EXISTS `jam`.`extras` (
  `extra_id` INT(11) NOT NULL AUTO_INCREMENT,
  `extrascol` VARCHAR(255) NULL DEFAULT NULL,
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
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
