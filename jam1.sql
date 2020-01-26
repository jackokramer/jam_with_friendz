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
  `user_id` INT NOT NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `c_password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jam`.`extras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jam`.`extras` ;

CREATE TABLE IF NOT EXISTS `jam`.`extras` (
  `extra_id` INT NOT NULL,
  `extrascol` VARCHAR(255) NULL,
  `college` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `instrument` VARCHAR(255) NULL,
  `about` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`extra_id`),
  INDEX `fk_extras_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_extras_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `jam`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
