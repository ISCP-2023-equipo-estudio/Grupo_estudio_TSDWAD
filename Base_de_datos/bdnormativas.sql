-- MySQL Script generated by MySQL Workbench
-- Wed Jun 21 20:33:17 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bdnormativas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bdnormativas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bdnormativas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bdnormativas` ;

-- -----------------------------------------------------
-- Table `bdnormativas`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdnormativas`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdnormativas`.`organolegislativo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdnormativas`.`organolegislativo` (
  `idorganoLegislativo` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idorganoLegislativo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdnormativas`.`tipojurisdiccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdnormativas`.`tipojurisdiccion` (
  `idtipoJurisdiccion` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `idOrganoLegislativo` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idtipoJurisdiccion`),
  INDEX `idOrganoLegislativo_idx` (`idOrganoLegislativo` ASC) VISIBLE,
  CONSTRAINT `idOrganoLegislativo`
    FOREIGN KEY (`idOrganoLegislativo`)
    REFERENCES `bdnormativas`.`organolegislativo` (`idorganoLegislativo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdnormativas`.`tiponormativa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdnormativas`.`tiponormativa` (
  `idtipoNormativa` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idtipoNormativa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bdnormativas`.`normativa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdnormativas`.`normativa` (
  `nroRegistro` INT NOT NULL AUTO_INCREMENT,
  `idTipoNormativa` INT NOT NULL,
  `fecha` DATE NULL DEFAULT NULL,
  `descripcion` VARCHAR(5000) NULL DEFAULT NULL,
  `palabrasClaves` VARCHAR(1000) NULL DEFAULT NULL,
  `idTipoJurisdiccion` INT NOT NULL,
  `nroNormativa` INT NULL DEFAULT NULL,
  `idCategoria` INT NOT NULL,
  PRIMARY KEY (`nroRegistro`),
  INDEX `idTipoNormativa_idx` (`idTipoNormativa` ASC) VISIBLE,
  INDEX `idTipoJurisdiccion_idx` (`idTipoJurisdiccion` ASC) VISIBLE,
  INDEX `idCategoria_idx` (`idCategoria` ASC) VISIBLE,
  CONSTRAINT `idCategoria`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `bdnormativas`.`categoria` (`idcategoria`),
  CONSTRAINT `idTipoJurisdiccion`
    FOREIGN KEY (`idTipoJurisdiccion`)
    REFERENCES `bdnormativas`.`tipojurisdiccion` (`idtipoJurisdiccion`),
  CONSTRAINT `idTipoNormativa`
    FOREIGN KEY (`idTipoNormativa`)
    REFERENCES `bdnormativas`.`tiponormativa` (`idtipoNormativa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE bdnormativas;

insert into categoria(nombre) values
("Laboral"),
("Penal"),
("Civil"),
("Comercial"),
("Familia y Sucesiones"),
("Agrario y Ambiental"),
("Minería"),
("Derecho Informático");

insert into tipoNormativa(nombre) values
( "Ley"),
("Decreto"),
("Resolución");

insert into organolegislativo(nombre) values
("Congreso de la Nación"),
("Legislatura de Córdoba");

insert into tipojurisdiccion(nombre, idOrganoLegislativo) values 
("Nacional", "1"),
("Provincial", "2");

insert into normativa( idTipoNormativa, fecha, descripcion, palabrasClaves, idTipoJurisdiccion, nroNormativa, idCategoria) values
( "1", "1976-05-13", "La Ley de Contrato de Trabajo establece los derechos y obligaciones tanto de los empleadores como de los trabajadores.Regula cuestiones basicas de una relacion laboral,como la jornada laboral, descansos, remuneración, licencias y las modalidades del contrato de trabajo. Es una ley que tiene como objetivo garantizar condiciones justas y equitativas para el trabajador,estableciendo en su art 7 la nulidad de condiciones menos favorables para este a las establecidas en esta ley, y en caso de duda prevalecera la mas favorable al trabajador (art 9).  A los efectos de esta ley,se considera relacion de trabajo cuando una persona realice actos, ejecute obras o presteservicio en favor de otra, bajo la dependencia de ésta en forma voluntaria y mediante el pago de una remuneración, cualquiera sea el acto que le dé origen.", "trabajo,empleadores,trabajadores,contrato laboral,licencias,modalidades,condiciones laborales,trabajador, relacion,servicio laboral,trabajo,nacional", "1", "20744", "1"),
("1","1987-11-21", "La ley de ejercicio profesional en ciencias informaticas es una ley que regula todo lo atinente al desenvolvimiento de la actividad informatica en la provincia de Córdoba.Establece como condicion para el ejercicio de la profesion en la provincia la matriculacion obligatoria, imponiendo como requisito contar con título oficial reconocido a nivel nacional o provincial en carreras de Ciencias Informáticas de nivel terciario como mínimo. Ademas establece la constitucion y funciones del CONSEJO PROFESIONAL,quien estara a cargo del gobierno de la matricula,y de dar cumplimiento a todo lo dispuesto por esta ley.", "profesional ciencias informáticas,actividad informatica,cordoba,matricula,matriculacion,titulo,oficial,carreras,consejo,profesional", "2","7642", "8"),
("1", "2020-08-14", "La ley de teletrabajo es una normativa que regula los derechos y obligaciones de las partes(empleador y trabajador) cuando la actividad laboral se desarrolla a distancia,ya sea de manera total o parcial en el domicilio del trabajador,o en lugares distintos al del establecimiento del empleador,por medio de tecnologías de la información y comunicación.Establece los derechos y garantías para los trabajadores que desempeñan su actividad bajo esta modalidad,como el derecho a la desconexión digital(art 5), a la intimidad, a la capacitación, a la igualdad de trato y oportunidades, a la protección de la salud y seguridad laboral.", "teletrabajo,trabajador a Distancia,actividad laboral,domicilio,derecho desconexion digital,nacional", "1", "27555", "1"),
("1","1993-09-23", "La ley del Sistema Integrado de Jubilaciones y Pensiones establece las disposiciones legales y regulaciones relacionadas con el otorgamiento y el cálculo de las jubilaciones y pensiones para los ciudadanos argentinos. La ley aborda varios aspectos importantes, como los requisitos para acceder a una jubilación o pensión, los beneficios y derechos de los beneficiarios, el cálculo de los montos de jubilación o pensión, los mecanismos de actualización y ajuste de los montos, y las condiciones para la otorgación de pensiones por invalidez, entre otros temas relacionados.", "jubilaciones,pensiones,otorgamiento argentinos,beneficios,jubilacion,pension,actualizacion,ajuste,invalidez,nacional,congreso,social", "1", "24241", "3"),
("1","2008-06-04", "La ley de delitos informaticos es una ley que ordena la modificacion de diversos articulos del codigo penal,regulando y estableciendo una nueva escala penal para aquellos delitos cometidos con el uso de tecnologias., ya sea a través de medios electrónicos, informáticos o telemáticos,como tambien a los delitos que afecten la confidencialidad, integridad y disponibilidad de los datos y sistemas informáticos,entre otros.", "delito informático,penal,nacional,delitos tecnologia,confidencialidad,integridad", "1", "26388", "2"),
("1","2000-10-04", "La ley de protección de datos personales establece los principios y normas que deben seguir tanto los organismos públicos como las empresas privadas al recolectar, almacenar, utilizar y compartir datos personales. Garantiza el derecho de las personas a conocer qué información se recopila, para qué se utiliza y quiénes tienen acceso a ella. También establece la obligación de obtener el consentimiento de los individuos para el uso de sus datos personales.
Además, la ley establece medidas de seguridad para proteger los datos personales de posibles filtraciones, pérdidas o accesos no autorizados. También establece la creación de un ente de control, la Agencia de Acceso a la Información Pública, encargada de velar por el cumplimiento de esta ley.", "datos personales,información,almacenamiento,consentimiento,seguridad,informática,filtracion,no autorizados,derecho informatico,nacional", "1", "25326", "8");


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
