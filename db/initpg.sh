#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE main;
    CREATE DATABASE support;
    CREATE DATABASE auth;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "main" <<-EOSQL
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR NOT NULL DEFAULT 'Guest',
        context JSONB NOT NULL DEFAULT '{}'::jsonb,
        email_verified BOOL NOT NULL DEFAULT FALSE,
        telegram_user_id INTEGER UNIQUE,
        email VARCHAR,
        password VARCHAR
    );

    -- Creating events table
    CREATE TABLE events (
        event_id SERIAL PRIMARY KEY,
        event_name VARCHAR NOT NULL,
        event_description VARCHAR NOT NULL,
        user_id INTEGER NOT NULL,
        goal_id INTEGER NOT NULL,
        is_complete BOOLEAN NOT NULL DEFAULT false
    );

    -- Creating notifications table
    CREATE TABLE notifications (
        notification_id SERIAL PRIMARY KEY,
        event_id INTEGER NOT NULL,
        time TIMESTAMP NOT NULL,
        is_complete BOOLEAN NOT NULL DEFAULT false
    );

    -- Creating messages_metadata table
    CREATE TABLE messages_metadata (
        message_id INTEGER UNIQUE PRIMARY KEY,
        sent_time TIMESTAMP NOT NULL,
        user_id INTEGER NOT NULL,
        model_id INTEGER
    );

    -- Creating models table
    CREATE TABLE models (
        model_id SERIAL PRIMARY KEY,
        model_name VARCHAR NOT NULL UNIQUE,
        model_size INT NOT NULL
    );

    -- Creating user_goals table
    CREATE TABLE user_goals (
        goal_id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        goal_details JSONB NOT NULL,
        is_active BOOLEAN NOT NULL DEFAULT false
    );

    -- Creating daily_reports table
    CREATE TABLE daily_reports (
        report_id SERIAL PRIMARY KEY,
        report_date TIMESTAMP NOT NULL,
        user_id INTEGER NOT NULL,
        report JSONB NOT NULL
    );

    -- Adding foreign keys
    -- Foreign keys for events table
    ALTER TABLE events ADD FOREIGN KEY (user_id) REFERENCES users (user_id);
    ALTER TABLE events ADD FOREIGN KEY (goal_id) REFERENCES user_goals (goal_id);

    -- Foreign key for notifications table
    ALTER TABLE notifications ADD FOREIGN KEY (event_id) REFERENCES events (event_id);

    -- Foreign keys for messages_metadata table
    ALTER TABLE messages_metadata ADD FOREIGN KEY (user_id) REFERENCES users (user_id);
    ALTER TABLE messages_metadata ADD FOREIGN KEY (model_id) REFERENCES models (model_id);

    -- Foreign key for user_goals table
    ALTER TABLE user_goals ADD FOREIGN KEY (user_id) REFERENCES users (user_id);

    -- Foreign key for daily_reports table
    ALTER TABLE daily_reports ADD FOREIGN KEY (user_id) REFERENCES users (user_id);

    -- Adding indexes
    CREATE INDEX idx_events_user_id ON events USING btree (user_id);
    CREATE INDEX idx_events_goal_id ON events USING btree (goal_id);
    CREATE INDEX idx_notifications_event_id ON notifications USING btree (event_id);
    CREATE INDEX idx_user_goals_user_id ON user_goals USING btree (user_id);
    CREATE INDEX idx_messages_metadata_user_id ON messages_metadata USING btree (user_id);
    CREATE INDEX idx_messages_metadata_model_id ON messages_metadata USING btree (model_id);
EOSQL