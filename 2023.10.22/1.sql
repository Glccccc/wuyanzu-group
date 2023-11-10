use world;
-- Запросы к таблице country:

-- 1. Вывести названия всех стран Евразии
select  name
 from country
where continent = 'Asia' or continent = 'Europe';

-- +-------------------------------+
-- | name                          |
-- +-------------------------------+
-- | Afghanistan                   |
-- | Albania                       |
-- | Andorra                       |
-- | United Arab Emirates          |
-- | Armenia                       |
-- | Austria                       |
-- | Azerbaijan                    |
-- | Belgium                       |
-- | Bangladesh                    |
-- | Bulgaria                      |
-- | Bahrain                       |
-- | Bosnia and Herzegovina        |

-- | Uzbekistan                    |
-- | Holy See (Vatican City State) |
-- | Vietnam                       |
-- | Yemen                         |
-- | Yugoslavia                    |
-- +-------------------------------+
-- 97 rows in set (0.0007 sec)


-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
select region, name
 from country
where LifeExpectancy < 50;


-- +---------------------------+---------------------------------------+
-- | region                    | name                                  |
-- +---------------------------+---------------------------------------+
-- | Southern and Central Asia | Afghanistan                           |
-- | Central Africa            | Angola                                |
-- | Eastern Africa            | Burundi                               |
-- | Western Africa            | Burkina Faso                          |
-- | Southern Africa           | Botswana                              |
-- | Central Africa            | Central African Republic              |
-- | Western Africa            | Côte d’Ivoire                         |
-- | Central Africa            | Congo, The Democratic Republic of the |
-- | Central Africa            | Congo                                 |
-- | Northern Africa           | Western Sahara                        |
-- | Eastern Africa            | Ethiopia                              |
-- | Western Africa            | Guinea                                |
-- | Western Africa            | Guinea-Bissau                         |
-- | Caribbean                 | Haiti                                 |
-- | Eastern Africa            | Kenya                                 |
-- | Western Africa            | Mali                                  |
-- | Eastern Africa            | Mozambique                            |
-- | Eastern Africa            | Malawi                                |
-- | Southern Africa           | Namibia                               |
-- | Western Africa            | Niger                                 |
-- | Eastern Africa            | Rwanda                                |
-- | Western Africa            | Sierra Leone                          |
-- | Eastern Africa            | Somalia                               |
-- | Southern Africa           | Swaziland                             |
-- | Southeast Asia            | East Timor                            |
-- | Eastern Africa            | Uganda                                |
-- | Eastern Africa            | Zambia                                |
-- | Eastern Africa            | Zimbabwe                              |
-- +---------------------------+---------------------------------------+
-- 28 rows in set (0.0009 sec)


-- 3. Вывести название самой крупной по площади страны Африки
select name
 from country
where SurfaceArea = (
	select max(SurfaceArea)
	from country
	where continent = "Africa"
);

-- +-------+
-- | name  |
-- +-------+
-- | Sudan |
-- +-------+
-- 1 row in set (0.0043 sec)


-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
select name
 from country
where continent = "Asia"
order by population / surfacearea limit 5;

-- +--------------+
-- | name         |
-- +--------------+
-- | Mongolia     |
-- | Kazakstan    |
-- | Oman         |
-- | Turkmenistan |
-- | Saudi Arabia |
-- +--------------+
-- 5 rows in set (0.0032 sec)

-- Запросы к таблице city

-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек

select CountryCode, name
 from city
where population > 5000000
order by population;

-- +-------------+-------------------+
-- | CountryCode | name              |
-- +-------------+-------------------+
-- | PAK         | Lahore            |
-- | COD         | Kinshasa          |
-- | CHN         | Tianjin           |
-- | BRA         | Rio de Janeiro    |
-- | COL         | Santafé de Bogotá |
-- | THA         | Bangkok           |
-- | CHN         | Chongqing         |
-- | PER         | Lima              |
-- | IRN         | Teheran           |
-- | EGY         | Cairo             |
-- | IND         | Delhi             |
-- | GBR         | London            |
-- | CHN         | Peking            |
-- | JPN         | Tokyo             |
-- | USA         | New York          |
-- | RUS         | Moscow            |
-- | MEX         | Ciudad de México  |
-- | TUR         | Istanbul          |
-- | PAK         | Karachi           |
-- | IDN         | Jakarta           |
-- | CHN         | Shanghai          |
-- | BRA         | São Paulo         |
-- | KOR         | Seoul             |
-- | IND         | Mumbai (Bombay)   |
-- +-------------+-------------------+
-- 24 rows in set (0.0030 sec)


-- 6. Вывести название города в Индии с самым длинным названием

select name, countrycode
 from city
where countrycode = 'IND'
    and char_length(name) = (
	select max(char_length(name))
	from city
	where countrycode = 'IND'
	);

-- +--------------------------------+-------------+
-- | name                           | countrycode |
-- +--------------------------------+-------------+
-- | Thiruvananthapuram (Trivandrum | IND         |
-- +--------------------------------+-------------+
-- 1 row in set (0.0026 sec)

select name
 from city
where countrycode = 'IND'
order by length(name) desc limit 1;

-- +--------------------------------+
-- | name                           |
-- +--------------------------------+
-- | Thiruvananthapuram (Trivandrum |
-- +--------------------------------+
-- 1 row in set (0.0018 sec)