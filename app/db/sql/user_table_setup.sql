
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    country_iso_3166  VARCHAR(2) not null,
    timezone VARCHAR(50) NOT NULL
);

INSERT INTO users (first_name, last_name, country_iso_3166, timezone) VALUES
('Hanna', 'Lyon', 'AU', 'Australia/Sydney'),
('Hansu', 'Lee', 'KR', 'Asia/Seoul');


CREATE TYPE reminder_type AS ENUM ('one_time', 'daily', 'weekly_specific_days');
CREATE TYPE week_days as enum ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN');
create type reminder_status as enum ('active', 'cancelled', 'completed');

drop type if exists reminder_type cascade;
drop type if exists week_days cascade;
drop type if exists reminder_status cascade;

CREATE TABLE reminders (
    id SERIAL PRIMARY KEY, 
    user_id INT NOT NULL REFERENCES users(id) ON DELETE cascade,
    type_of_reminder reminder_type NOT null default 'one_time',
    time_at_request_utc TIMESTAMP WITH TIME ZONE NOT NULL,
    time_reminder_utc TIMESTAMP with TIME zone not NULL,
    days week_days[], 
	status reminder_status not null default 'active',
	request_message VARCHAR(300) NOT null,
	
	CONSTRAINT days_not_null_when_weekly CHECK (
        type_of_reminder <> 'weekly_specific_days' OR (days IS NOT null and array_length(days, 1) >= 1 and array_length(days, 1) <= 7)
    ),

    CONSTRAINT days_null_for_daily CHECK (
        type_of_reminder <> 'one_time' OR days IS not NULL
    )
);


    
	--! write contraints for weekly_specific_days and daily. in which case, we need to store hours and minutes separately

-- fix below according to the new table above

INSERT INTO reminders (
    user_id,
    type_of_reminder,
    time_at_request_utc,
    time_reminder_utc,
    days,
    status,
    request_message
) VALUES (
    2,  
    'daily',  
    '2024-10-01T22:05:00+09',
    '2024-10-02T09:15:00+09',
    NULL,
    'active',
    'You are helping Ted to wake up in the morning. Say some motivational quotes to start the day. And say good morning.'  -- todo_message
);


