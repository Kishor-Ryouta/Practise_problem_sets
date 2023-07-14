-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND Street = "Humphrey Street";
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |

SELECT transcript
FROM interviews
WHERE month = 7 AND day = 28 AND transcript LIKE "%bakery%";

--(Clues from interviews):
--Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.|
--I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money. |
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

--(Following the breadcrumbs based on interviewees statements)
SELECT name FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE month = 7 AND day = 28 AND year = 2021 AND activity = "exit"
AND hour = 10 AND minute >= 15 AND minute <= 25; -- Possible suspects = Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey. (According to witness 1)

SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.transaction_type = "withdraw"
AND year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28;
-- possible suspects after filtration (Based on witness 2 statement) = Bruce, Iman, Luca, Diana.

SELECT name FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (
    SELECT id FROM flights
    WHERE year = 2021 AND month = 7 AND day = 29
    ORDER BY hour, minute
        LIMIT 1);
    --suspects(Based on Witness) = Doris, Sofia, Bruce, Edward, Kelsey, Taylor, Kenny, Luca.


SELECT name FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE month = 7 AND day = 28 AND duration < 60;

-- Sofia ,Kelsey, Bruce, Taylor, Diana, Carina, Kenny, Benista

--Clearly the thief is Bruce = "Bruce"

SELECT city FROM airports
WHERE id = (
    SELECT destination_airport_id FROM flights
    WHERE month = 7 AND day = 29 AND year = 2021 ORDER BY hour, minute LIMIT 1);

--Escaped city = New York City

SELECT phone_number FROM people
WHERE name = "Bruce";
-- (367) 555-5533

SELECT name FROM people WHERE phone_number = (
    SELECT receiver FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND caller = "(367) 555-5533" AND duration < 60);
--Accomplice: Robin