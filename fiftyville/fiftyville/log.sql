-- Keep track of your investigation here.

-- 1. Find the earliest flight leaving Fiftyville on July 29, 2025 to find the escape city
SELECT flights.id, hour, minute, city FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
WHERE year = 2025 AND month = 7 AND day = 29
ORDER BY hour, minute LIMIT 1;

-- 2. Find the list of passengers on that flight (Flight ID 36)
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE passengers.flight_id = 36;

-- 3. Check callers who made short phone calls (< 60s) on the day of the theft
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2025 AND month = 7 AND day = 28 AND duration < 60;

-- 4. Check ATM cash withdrawals on Leggett Street on the day of the theft
SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2025 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- 5. Check bakery parking lot exits within 10 minutes of the theft to identify Bruce as the thief
SELECT name FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2025 AND month = 7 AND day = 28
AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = 'exit';

-- 6. Find the accomplice who received Bruce's phone call
SELECT name FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls
    WHERE year = 2025 AND month = 7 AND day = 28
    AND duration < 60
    AND caller = (SELECT phone_number FROM people WHERE name = 'Bruce')
);
